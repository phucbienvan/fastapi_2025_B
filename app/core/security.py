import bcrypt
from passlib.context import CryptContext
from app.core.config import settings
from datetime import datetime, timedelta
import jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return password_context.hash(password.encode('utf-8'))

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(user_id: int):
    expired = datetime.utcnow() + timedelta(minutes=30)
    payload = {
        'user_id': user_id,
        'exp': expired
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token
