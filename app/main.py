from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db
from app.routers import books, loans, reports


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(title="Library Circulation API", lifespan=lifespan)

app.include_router(books.router)
app.include_router(loans.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {"message": "Welcome to Library Circulation API"}