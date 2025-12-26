from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.core.config import settings
from app.db.base import get_db
from sqlalchemy.orm import Session
from app.models.user_model import User
import jwt

reusable_oauth = HTTPBearer(
    scheme_name="JWT Authentication"
)

def authenticate_user(http_authorization_credentials=Depends(reusable_oauth), db: Session = Depends(get_db)):
    try:
        token = http_authorization_credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        
        print("payloadddd: ", payload)
        
        user = db.query(User).filter(User.id == payload.get('user_id')).first()
        print("user", user)
        if not user:
            raise HTTPException(status_code=401, detail='User not found')
        return user
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    