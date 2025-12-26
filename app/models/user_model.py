from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer
import datetime

class User(BaseModel):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    email: str = Column(String, index=True)
    password: str = Column(String, index=True)
    created_at: datetime.datetime = Column(DateTime, index=True)
    updated_at: datetime.datetime = Column(DateTime, index=True)
