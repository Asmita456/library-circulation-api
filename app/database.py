import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./library.db"
)

connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=True
)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session