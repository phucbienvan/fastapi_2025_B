from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.user_model import User
from fastapi import Depends
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.user_schema import UserSchema, RegisterSchema, LoginSchema, LoginResponseSchema
from app.core.security import hash_password, verify_password, create_access_token
from app.middleware.authenticate import authenticate_user
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=DataResponse[UserSchema], tags=["user"])
async def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user = User(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return DataResponse.custom_response(data=user, code='201', message='register success')

@router.post("/login",  tags=["user"], response_model=DataResponse[LoginResponseSchema])
async def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    
    if not user:
        return DataResponse.custom_response(data=None, code='401', message='Email or password is incorrect')
    
    if not verify_password(data.password, user.password):
        return DataResponse.custom_response(data=None, code='401', message='Email or password is incorrect')
    
    access_token = create_access_token(user.id)
    
    print("access_token: ", access_token)
    return DataResponse.custom_response(data=LoginResponseSchema(access_token=access_token, token_type="Bearer"), code='200', message='login success')

@router.get("/me", tags=["user"], response_model=DataResponse[UserSchema], dependencies=[Depends(authenticate_user)])
async def get_me(user: int = Depends(authenticate_user)):
    return DataResponse.custom_response(data=user, code='200', message='get me success')
