from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.base import get_db
from fastapi import Depends
from app.models.task_model import Task
from typing import List

router = APIRouter()

@router.get("/tasks",)
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.post("/tasks")
async def create_task():
    return {"message": "Task created"}

@router.put("/tasks/{task_id}")
async def update_task(task_id: int):
    return {"message": "Task updated"}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"message": "Task deleted"}
