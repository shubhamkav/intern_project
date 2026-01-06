from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class FormResponse(Base):
    __tablename__ = "form_responses"

    id = Column(Integer, primary_key=True, index=True)

    # Google Form fields
    full_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(50), nullable=True)
    nationality = Column(String(100), nullable=True)
    mobile = Column(String(20), nullable=True)
    email = Column(String(255), nullable=False, index=True)

    # Multi-city & multi-form support
    city = Column(String(100), nullable=False)
    form_id = Column(String(100), nullable=False)

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
