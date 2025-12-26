from fastapi import FastAPI
from app.db.base import get_db
from app.models import Base
from app.db.base import engine
from app.routers.task_router import router as task_router
<<<<<<< HEAD
=======
from app.routers.user_router import router as user_router
>>>>>>> e6345e271988d41db266fe35c6a4de4ed9a3e48e

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_router)
<<<<<<< HEAD
=======
app.include_router(user_router)
>>>>>>> e6345e271988d41db266fe35c6a4de4ed9a3e48e

@app.get("/")
async def root():
    return {"message": "Hello World"}
