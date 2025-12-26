import bcrypt, secrets
from passlib.context import CryptContext

password_context = CryptContext(schemes=["pbkdf2_sha256", "md5_crypt", "des_crypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return password_context.hash(password) 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return password_context.verify(plain_password, hashed_password)
    except Exception as e:
        print(f"Lỗi xác thực mật khẩu: {e}")
        return False

def generate_remember_token() -> str:
    return secrets.token_hex(32)