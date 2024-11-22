from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.payment import Payment, Promotion
from sqlalchemy.exc import SQLAlchemyError

def create_payment(db: Session, request):
    new_payment = Payment(
        amount=request.amount,
        payment_type=request.payment_type,
        transaction_status=request.transaction_status,
        transaction_date=request.transaction_date,
        order_id=request.order_id
    )

    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_payment

def get_all_payments(db: Session):
    try:
        payments = db.query(Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payments

def create_promotion(db: Session, request):
    new_promotion = Promotion(
        promo_code=request.promo_code,
        discount_percentage=request.discount_percentage,
        expiration_date=request.expiration_date
    )

    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_promotion
