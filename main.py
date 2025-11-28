from fastapi import FastAPI
from app.db.base import get_db
from app.models import Base
from app.db.base import engine
from app.routers.task_router import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
