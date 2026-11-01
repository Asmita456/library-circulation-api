
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import Book, Loan
from app.schemas import LoanCreate

router = APIRouter(prefix="/loans", tags=["Loans"])


# Borrow book
@router.post("/", status_code=status.HTTP_201_CREATED)
def borrow_book(
    data: LoanCreate,
    session: Session = Depends(get_session)
):
    book = session.get(Book, data.book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if book.available_copies < 1:
        raise HTTPException(
            status_code=409,
            detail="No copies available"
        )

    try:
        book.available_copies -= 1

        loan = Loan(
            book_id=data.book_id,
            borrower_name=data.borrower_name,
            is_returned=False
        )

        session.add(loan)
        session.add(book)
        session.commit()
        session.refresh(loan)

        return loan

    except Exception:
        session.rollback()
        raise


# Get loans with active_only filter
@router.get("/")
def get_loans(
    active_only: bool = False,
    session: Session = Depends(get_session)
):
    statement = select(Loan)

    if active_only:
        statement = statement.where(
            Loan.is_returned == False
        )

    return session.exec(statement).all()


# Return book
@router.patch("/{loan_id}/return")
def return_book(
    loan_id: int,
    session: Session = Depends(get_session)
):
    loan = session.get(Loan, loan_id)

    if not loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    if loan.is_returned:
        raise HTTPException(
            status_code=409,
            detail="Book already returned"
        )

    book = session.get(Book, loan.book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    try:
        loan.is_returned = True
        book.available_copies += 1

        session.add(loan)
        session.add(book)
        session.commit()
        session.refresh(loan)

        return loan

    except Exception:
        session.rollback()
        raise
