from apscheduler.schedulers.background import BackgroundScheduler
from app.services.google_forms import fetch_city_form_data
from app.core.database import SessionLocal
from app.models.form_response import FormResponse
from datetime import datetime

CITIES = ["Patna", "Mumbai"]  # add more later


def sync_all_cities():
    db = SessionLocal()
    try:
        for city in CITIES:
            payload = fetch_city_form_data(city)
            responses = payload.get("responses", [])

            for r in responses:
                email = r.get("Email Address") or r.get("Email")
                name = r.get("Full Legal Name") or r.get("Full Name")

                if not email or not name:
                    continue

                exists = db.query(FormResponse).filter(
                    FormResponse.email == email,
                    FormResponse.city == city
                ).first()

                if exists:
                    continue

                record = FormResponse(
                    full_name=name,
                    email=email.lower(),
                    city=city,
                    form_id=payload.get("form_id", "")
                )
                db.add(record)

            db.commit()
    finally:
        db.close()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_all_cities, "interval", hours=1)
    scheduler.start()
