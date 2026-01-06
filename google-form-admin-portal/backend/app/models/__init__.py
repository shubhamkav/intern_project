"""
Model package initializer
Ensures all SQLAlchemy models are registered
"""

from app.models.form_response import FormResponse

__all__ = [
    "FormResponse",
]
