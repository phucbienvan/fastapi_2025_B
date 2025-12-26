from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer
<<<<<<< HEAD
from datetime import datetime
=======
import datetime
>>>>>>> e6345e271988d41db266fe35c6a4de4ed9a3e48e

class User(BaseModel):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    email: str = Column(String, index=True)
    password: str = Column(String, index=True)
<<<<<<< HEAD
    status: int = Column(Integer, index=True, default=1)
    created_at: datetime = Column(DateTime, index=True, default=datetime.now)
    updated_at: datetime = Column(DateTime, index=True, default=datetime.now)
=======
    created_at: datetime.datetime = Column(DateTime, index=True)
    updated_at: datetime.datetime = Column(DateTime, index=True)
>>>>>>> e6345e271988d41db266fe35c6a4de4ed9a3e48e
