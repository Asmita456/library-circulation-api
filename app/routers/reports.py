from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import Book, Loan

router = APIRouter(prefix="/reports", tags=["Reports"])


# Library summary
@router.get("/summary")
def get_summary(session: Session = Depends(get_session)):

    books = session.exec(select(Book)).all()
    loans = session.exec(select(Loan)).all()

    total_books = len(books)
    total_copies = 0
    available_copies = 0
    active_loans = 0

    for book in books:
        total_copies += book.total_copies
        available_copies += book.available_copies

    for loan in loans:
        if not loan.is_returned:
            active_loans += 1

    return {
        "total_books": total_books,
        "total_copies": total_copies,
        "available_copies": available_copies,
        "active_loans": active_loans
    }