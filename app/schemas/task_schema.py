from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, description="Tiêu đề task")
    description: Optional[str] = Field(None, description="Mô tả task")
    status: int = Field(default=0, description="Trạng thái task")
    is_deleted: bool = Field(default=False, description="Trạng thái xóa")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    status: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    is_deleted: bool

    class Config:
        from_attributes = True
