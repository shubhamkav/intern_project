import os
from dotenv import load_dotenv

load_dotenv()

# ================================
# DATABASE CONFIGURATION
# ================================
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "google_form_admin")

# ================================
# SECURITY / ADMIN CONFIG
# ================================
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# ================================
# GOOGLE APPS SCRIPT
# ================================
GOOGLE_SCRIPT_URL = os.getenv("GOOGLE_SCRIPT_URL", "")
