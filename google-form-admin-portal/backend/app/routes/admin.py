from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.form_response import FormResponse

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/responses/{city}")
def get_city_responses(city: str, db: Session = Depends(get_db)):
    rows = (
        db.query(FormResponse)
        .filter(FormResponse.city == city)
        .order_by(FormResponse.id.desc())
        .all()
    )

    return [
        {
            "full_name": r.full_name,
            "email": r.email,
            "mobile": r.mobile,
            "gender": r.gender,
            "nationality": r.nationality
        }
        for r in rows
    ]
