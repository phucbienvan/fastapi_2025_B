from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.user_model import User
from fastapi import Depends
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.user_schema import UserSchema, RegisterSchema
from app.core.security import hash_password
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=DataResponse[UserSchema], tags=["user"])
async def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user = User(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return DataResponse.custom_response(data=user, code='201', message='register success')
