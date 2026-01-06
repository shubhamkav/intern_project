import requests
from app.core.config import GOOGLE_SCRIPT_URL


def fetch_city_form_data(city: str):
    if not GOOGLE_SCRIPT_URL:
        raise ValueError("GOOGLE_SCRIPT_URL not set in .env")

    response = requests.get(
        GOOGLE_SCRIPT_URL,
        params={"city": city},
        timeout=30
    )

    response.raise_for_status()
    return response.json()
