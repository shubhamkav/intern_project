import requests
from fastapi import APIRouter, HTTPException
from app.core.config import GOOGLE_SCRIPT_URL

router = APIRouter(prefix="/forms", tags=["Forms"])

@router.post("/close-all")
def close_all_forms():
    res = requests.post(
        GOOGLE_SCRIPT_URL,
        params={"action": "close"},
        timeout=30
    )

    if not res.ok:
        raise HTTPException(status_code=500, detail="Failed to close forms")

    return res.json()


@router.post("/open-all")
def open_all_forms():
    res = requests.post(
        GOOGLE_SCRIPT_URL,
        params={"action": "open"},
        timeout=30
    )

    if not res.ok:
        raise HTTPException(status_code=500, detail="Failed to open forms")

    return res.json()
