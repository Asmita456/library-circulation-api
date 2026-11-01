from typing import Optional
from sqlmodel import SQLModel, Field


class BookCreate(SQLModel):
    title: str = Field(min_length=3, max_length=120)
    author: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=1)
    total_copies: int = Field(ge=1)


class BookUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=120)
    author: Optional[str] = Field(default=None, min_length=2, max_length=80)
    category: Optional[str] = Field(default=None, min_length=1)


class BookRead(SQLModel):
    id: int
    title: str
    author: str
    category: str
    total_copies: int
    available_copies: int


class LoanCreate(SQLModel):
    book_id: int
    borrower_name: str = Field(min_length=2, max_length=80)


class LoanRead(SQLModel):
    id: int
    book_id: int
    borrower_name: str
    is_returned: bool


class SummaryRead(SQLModel):
    total_books: int
    total_copies: int
    available_copies: int
    active_loans: int
