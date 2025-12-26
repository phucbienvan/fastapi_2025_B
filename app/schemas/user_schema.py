from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
        
class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str
    
class LoginSchema(BaseModel):
    email: str
    password: str
