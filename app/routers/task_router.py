from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.task_model import Task
from app.schemas.task_schemas import (
    TaskSchema,
    CreateTaskSchema, 
    UpdateTaskSchema
)
from typing import List
from app.schemas.base_schema import DataResponse
from app.schemas.task_schema import TaskSchema, TaskSchemaCreate, TaskSchemaUpdate
from datetime import datetime
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
@router.get("/", response_model=List[TaskSchema])
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    tasks = db.query(Task)\
        .filter(Task.status != -1)\
        .offset(skip)\
        .limit(limit)\
        .all()
    return tasks

@router.get("/{task_id}", response_model=TaskSchema)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task)\
        .filter(Task.id == task_id, Task.status != -1)\
        .first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task với id {task_id} không tồn tại"
        )
    return task

@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: CreateTaskSchema, db: Session = Depends(get_db)):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{task_id}", response_model=TaskSchema)
async def update_task(
    task_id: int, 
    task_data: UpdateTaskSchema, 
    db: Session = Depends(get_db)
):
    task = db.query(Task)\
        .filter(Task.id == task_id, Task.status != -1)\
        .first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task với id {task_id} không tồn tại"
        )

    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
async def soft_delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task)\
        .filter(Task.id == task_id, Task.status != -1)\
        .first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task với id {task_id} không tồn tại"
        )
    task.status = -1
    db.commit()
    return {
        "message": "Task đã được xóa mềm thành công",
        "task_id": task_id
    }

    return DataResponse.custom_response(data=task, code='200', message='update task success')
    


