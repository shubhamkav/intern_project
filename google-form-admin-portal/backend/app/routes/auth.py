from fastapi import APIRouter, HTTPException
from app.core.config import ADMIN_USERNAME, ADMIN_PASSWORD

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def admin_login(data: dict):
    username = data.get("username")
    password = data.get("password")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {"status": "ok"}

    raise HTTPException(status_code=401, detail="Invalid credentials")
