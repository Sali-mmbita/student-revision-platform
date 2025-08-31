# config.py
import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret")

    # Use DATABASE_URL for easy local sqlite testing: e.g. sqlite:///dev.db
    DATABASE_URL = os.getenv("DATABASE_URL", None)

    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        DB_USER = os.getenv("DB_USER", "root")
        DB_PASS = quote_plus(os.getenv("DB_PASS", ""))
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_NAME = os.getenv("DB_NAME", "student_revision")
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
