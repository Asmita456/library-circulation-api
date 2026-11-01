from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Book, Loan
from app.schemas import BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


# Create book
@router.post("/")
def create_book(data: BookCreate, session: Session = Depends(get_session)):

    book = Book(
        title=data.title,
        author=data.author,
        category=data.category,
        total_copies=data.total_copies,
        available_copies=data.total_copies
    )

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# Get all books
@router.get("/")
def get_books(session: Session = Depends(get_session)):

    return session.exec(select(Book)).all()


# Get book by ID
@router.get("/{book_id}")
def get_book(book_id: int, session: Session = Depends(get_session)):

    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# Update book
@router.patch("/{book_id}")
def update_book(book_id: int, data: BookUpdate, session: Session = Depends(get_session)):

    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if data.title is not None:
        book.title = data.title

    if data.author is not None:
        book.author = data.author

    if data.category is not None:
        book.category = data.category

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# Delete book
@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):

    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    loan = session.exec(
        select(Loan).where(Loan.book_id == book_id)
    ).first()

    if loan:
        raise HTTPException(status_code=409, detail="Book has loan history")

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}