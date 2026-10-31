from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_db
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(title="Library Management API", lifespan=lifespan)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to Library Management API"}