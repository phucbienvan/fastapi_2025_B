# routers/task_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.base import get_db
from app.models.task_model import Task
from app.schemas.base_schema import DataResponse
from app.schemas.task_schema import TaskSchema, TaskSchemaCreate, TaskSchemaUpdate

router = APIRouter()


@router.get("/tasks", response_model=DataResponse[List[TaskSchema]])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return DataResponse.custom_response(data=tasks,code="200",message="get tasks success")

@router.post("/tasks",response_model=DataResponse[TaskSchema])
async def create_task(task: TaskSchemaCreate, db: Session = Depends(get_db)):
    task = Task(**task.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return DataResponse.custom_response(data=task,code="201",message="create tasks success")

@router.get("/tasks/{task_id}", response_model=DataResponse[TaskSchema])
async def get_task(task_id: int,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    return DataResponse.custom_response(data=task,code="200",message="get task success")

@router.put("/tasks/{task_id}", response_model=DataResponse[TaskSchema])
async def update_task(task_id: int,task_update: TaskSchemaUpdate,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return DataResponse.custom_response(data=None,code="404",message="task not found")

    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return DataResponse.custom_response(data=task,code="200",message="update task success")


# @router.delete("/tasks/{task_id}")
# async def delete_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#     db.delete(task)
#     db.commit()
#     return DataResponse.custom_response(data=None,code="200",message="delete task success")

@router.delete("/tasks/{task_id}")
async def soft_delete_task(task_id: int,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return DataResponse.custom_response(data=None,code="404",message="task not found")

    task.status = 0
    db.commit()

    return DataResponse.custom_response(data=None,code="200",message="delete task success")
