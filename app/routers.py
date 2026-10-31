from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import Book, BookCreate, BookUpdate

router = APIRouter()

@router.post("/books")
def create_book(
    data:BookCreate,
    session:Session = Depends(get_session)
):
    book = Book.model_validate(
    data,
    update={"available_copies": data.total_copies}
    )

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


@router.get("/books")
def get_books(
    session:Session = Depends(get_session)
):
    return session.exec(select(Book)).all()


@router.get("/books/{book_id}")
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.patch("/books/{book_id}")
def update_book(
    book_id: int,
    data: BookUpdate,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.sqlmodel_update(data.model_dump(exclude_unset=True))

    session.add(book)
    session.commit()
    session.refresh(book)

    return book



@router.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}

