import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from functools import lru_cache

load_dotenv()

class Settings(BaseSettings):
    # Database
    db_url : str

    # JWT
    SECRET_KEY : str
    ALGORITHM : str
    origins : str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    OTP_EXPIRE_SECONDS: int

    # Mail
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    MAIL_FROM_NAME: str


    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()


"""
origins = [
    "http://localhost:3000",
]
ALGORITHM = "HS256"
SECRET_KEY = "noSecretKey"
db_url= "postgresql://postgres:123456@localhost:5000/bookstore"
"""