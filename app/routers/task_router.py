from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.base import get_db
from fastapi import Depends
from app.models.task_model import Task
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.task_schema import TaskSchema, TaskSchemaCreate

router = APIRouter()

@router.get("/tasks", response_model=DataResponse[List[TaskSchema]])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return DataResponse.custom_response(data=tasks, code='200', message='get tasks success')

@router.post("/tasks", response_model=DataResponse[TaskSchema])
async def create_task(task: TaskSchemaCreate, db: Session = Depends(get_db)):
    task = Task(**task.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return DataResponse.custom_response(data=task, code='201', message='create task success')

@router.get("/tasks/{task_id}", response_model=DataResponse[TaskSchema])
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    return DataResponse.custom_response(data=task, code='200', message='get task success')

@router.put("/tasks/{task_id}")
async def update_task(task_id: int):
    return {"message": "Task updated"}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return DataResponse.custom_response(data=None, code='200', message='delete task success')
