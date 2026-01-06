from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models.form_response import FormResponse
from app.services.google_forms import fetch_city_form_data

router = APIRouter(prefix="/sync", tags=["Sync"])


def get_any(record: dict, keys: list[str]):
    """Return first non-empty value for possible keys"""
    for k in keys:
        if k in record and record[k]:
            return str(record[k]).strip()
    return None


@router.post("/{city}")
def sync_city(city: str, db: Session = Depends(get_db)):
    payload = fetch_city_form_data(city)
    responses = payload.get("responses", [])

    inserted = 0
    skipped = 0

    for r in responses:
        # ---------------- EMAIL (MANDATORY) ----------------
        email = get_any(r, [
            "Personal Email Address",
            "Email Address",
            "Email address",
            "Email",
            "Personal Email"
        ])

        if not email:
            skipped += 1
            continue

        email = email.lower()

        # ---------------- FULL NAME (MANDATORY) ----------------
        full_name = get_any(r, [
            "Full Legal Name",
            "Full Name",
            "Full legal name",
            "Name",
            "Your Name"
        ])

        if not full_name:
            skipped += 1
            continue  # ❌ DO NOT INSERT

        # ---------------- DUPLICATE CHECK ----------------
        exists = db.query(FormResponse).filter(
            FormResponse.email == email,
            FormResponse.city == city
        ).first()

        if exists:
            skipped += 1
            continue

        # ---------------- OPTIONAL FIELDS ----------------
        mobile = get_any(r, [
            "Contact Number (Mobile)",
            "Contact Number",
            "Mobile",
            "Phone Number"
        ])

        gender = get_any(r, ["Gender"])
        nationality = get_any(r, ["Nationality"])

        dob = None
        raw_dob = get_any(r, ["Date of Birth", "DOB"])
        if raw_dob:
            for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
                try:
                    dob = datetime.strptime(raw_dob, fmt).date()
                    break
                except:
                    pass

        record = FormResponse(
            full_name=full_name,
            date_of_birth=dob,
            gender=gender,
            nationality=nationality,
            mobile=mobile,
            email=email,
            city=city,
            form_id=payload.get("form_id", "")
        )

        db.add(record)
        db.flush()  # forces SQL execution
        inserted += 1

    db.commit()

    return {
        "city": city,
        "fetched": len(responses),
        "inserted": inserted,
        "skipped": skipped
    }
