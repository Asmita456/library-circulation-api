from sqlmodel import SQLModel, Field

class Book(SQLModel, table =True):
    id:int | None = Field(default=None, primary_key=True)
    title:str
    author: str
    category:str
    total_copies:int
    available_copies:int | None = Field(default=None)

class BookCreate(SQLModel):
    title:str
    author: str
    category:str
    total_copies:int

class BookUpdate(SQLModel):
    title:str | None = None
    author: str | None = None
    category:str | None = None
    total_copies:int | None = None