from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    status: int

    class Config:
        from_attributes = True

class TaskSchemaCreate(BaseModel):
    title: str
    description: str
    status: int
