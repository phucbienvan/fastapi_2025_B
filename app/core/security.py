import bcrypt
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super-secret-key-change-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password.encode('utf-8'), hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)