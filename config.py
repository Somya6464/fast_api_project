import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    db_url = os.getenv("db_url")
    ALGORITHM = os.getenv("ALGORITHM")
    origins = os.getenv("origins")

settings = Settings()


"""
origins = [
    "http://localhost:3000",
]
ALGORITHM = "HS256"
SECRET_KEY = "noSecretKey"
db_url= "postgresql://postgres:123456@localhost:5000/bookstore"
"""