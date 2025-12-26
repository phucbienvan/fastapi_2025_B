from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.user_model import User
from fastapi import Depends
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.user_schema import LoginSchema, UserSchema, RegisterSchema
from app.core.security import hash_password
from datetime import datetime
from app.core.security import verify_password, generate_remember_token

router = APIRouter()

@router.post("/register", response_model=DataResponse[UserSchema], tags=["user"])
async def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user = User(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return DataResponse.custom_response(data=user, code='201', message='register success')

@router.post("/login", tags=["user"])
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai thông tin email hoặc mật khẩu"
        )

    token = generate_remember_token()
    
    user.remember_token = token
    db.commit()
    db.refresh(user)

    return {
        "message": "Đăng nhập thành công",
        "remember_token": token, 
        "user_id": user.id
    }