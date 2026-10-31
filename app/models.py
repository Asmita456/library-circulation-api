from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(min_length=3, max_length=120)
    author: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=1)
    total_copies: int = Field(ge=1)
    available_copies: int = Field(ge=0)


class BookCreate(SQLModel):
    title: str = Field(min_length=3, max_length=120)
    author: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=1)
    total_copies: int = Field(ge=1)


class BookUpdate(SQLModel):
    title: str | None = Field(default=None, min_length=3, max_length=120)
    author: str | None = Field(default=None, min_length=2, max_length=80)
    category: str | None = Field(default=None, min_length=1)
    total_copies: int | None = Field(default=None, ge=1)