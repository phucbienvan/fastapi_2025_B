from fastapi import FastAPI
from app.db.base import get_db
from app.models import Base
from app.db.base import engine
from app.routers.task_router import router as task_router
from app.routers.user_router import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
