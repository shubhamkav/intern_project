from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# ================================
# LOAD ENVIRONMENT VARIABLES
# ================================
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_HOST, DB_USER, DB_NAME]):
    raise RuntimeError("Database environment variables are not set correctly")

# ================================
# DATABASE URL
# ================================
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

print("[DB] Connected to:", DATABASE_URL)

# ================================
# SQLALCHEMY ENGINE
# ================================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=280,
    echo=False
)

# ================================
# SESSION FACTORY
# ================================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ================================
# BASE MODEL
# ================================
Base = declarative_base()


# ================================
# DATABASE DEPENDENCY
# ================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
