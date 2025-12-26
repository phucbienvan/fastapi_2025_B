from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import TypeVar, Generic, Optional


T = TypeVar("T")

class ResponseSchemaBase(BaseModel):
    __abstract__ = True

    code: str = ''
    message: str = ''

    def custom_response(self, code: str, message: str):
        self.code = code
        self.message = message
        return self
    
class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def custom_response(cls, code: str, message: str, data: T):
        return cls(code=code, message=message, data=data)
    
    @classmethod
    def success_response(cls, data: T):
<<<<<<< HEAD
        return cls(code='000', message='thành công', data=data)
=======
        return cls(code='000', message='success', data=data)
>>>>>>> e6345e271988d41db266fe35c6a4de4ed9a3e48e
