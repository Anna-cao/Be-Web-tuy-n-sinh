
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:lookatme@localhost:5432/DuAn"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
