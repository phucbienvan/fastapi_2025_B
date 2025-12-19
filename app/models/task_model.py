from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer, Text, Boolean
import datetime


class Task(BaseModel):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(255), index=True, nullable=False)
    description: str = Column(Text, nullable=True)
    status: int = Column(Integer, default=0, nullable=False)
    is_deleted: bool = Column(Boolean, default=False, nullable=False, index=True)
