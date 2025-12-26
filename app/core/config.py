import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")
    EXPIRE_MINUTES: int = int(os.getenv("EXPIRE_MINUTES", 30))
settings = Settings()
