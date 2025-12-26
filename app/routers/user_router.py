from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.user_model import User
from fastapi import Depends
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.user_schema import UserSchema, RegisterSchema, LoginSchema
from app.core.security import hash_password, verify_password
from fastapi import HTTPException, status
from datetime import datetime
from app.core.security import hash_password, verify_password, create_access_token   
from app.schemas.user_schema import TokenSchema


router = APIRouter()

@router.post("/register", response_model=DataResponse[UserSchema], tags=["user"])
async def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user = User(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return DataResponse.custom_response(data=user, code='201', message='register success')

@router.post("/login", response_model=DataResponse[TokenSchema], tags=["user"])
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password incorrect"
        )

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return DataResponse.custom_response(
        data={
            "access_token": access_token,
            "token_type": "bearer"
        },
        code="200",
        message="login success"
    )
