
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session, select
from sqlalchemy import or_

from app.database import get_session
from app.models import Book, Loan
from app.schemas import BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


# Create book
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(
    data: BookCreate,
    session: Session = Depends(get_session)
):
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


# Get books with filters
@router.get("/")
def get_books(
    search: str | None = None,
    category: str | None = None,
    available_only: bool = False,
    session: Session = Depends(get_session)
):
    statement = select(Book)

    # Search title or author
    if search:
        statement = statement.where(
            or_(
                Book.title.ilike(f"%{search}%"),
                Book.author.ilike(f"%{search}%")
            )
        )

    # Filter by category
    if category:
        statement = statement.where(
            Book.category == category
        )

    # Show only available books
    if available_only:
        statement = statement.where(
            Book.available_copies > 0
        )

    return session.exec(statement).all()


# Get book by ID
@router.get("/{book_id}")
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# Update book
@router.patch("/{book_id}")
def update_book(
    book_id: int,
    data: BookUpdate,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

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
@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    loan = session.exec(
        select(Loan).where(Loan.book_id == book_id)
    ).first()

    if loan:
        raise HTTPException(
            status_code=409,
            detail="Book has loan history"
        )

    session.delete(book)
    session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
