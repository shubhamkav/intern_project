from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.models.form_response import FormResponse

# ROUTES
from app.routes.sync import router as sync_router
from app.routes.auth import router as auth_router
from app.routes.admin import router as admin_router
from app.routes.forms import router as forms_router  # 🔒 form open/close

# 🔁 AUTO-SYNC SCHEDULER
from app.services.scheduler import start_scheduler

app = FastAPI(title="Google Form Admin Portal")

# ================================
# CORS CONFIGURATION
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# CREATE DATABASE TABLES + START SCHEDULER
# ================================
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    start_scheduler()  # ⏱️ auto sync every 1 hour

# ================================
# ROUTERS
# ================================
app.include_router(auth_router)    # admin login
app.include_router(sync_router)    # manual city sync
app.include_router(admin_router)   # admin data APIs
app.include_router(forms_router)   # 🔴 open / close all Google Forms

# ================================
# ROOT ENDPOINT
# ================================
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "FastAPI backend running | auto-sync enabled | form control enabled"
    }
