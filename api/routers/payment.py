from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers.payment import create_payment, get_all_payments, create_promotion
from ..schemas.payment import PaymentCreate, Payment, PromotionCreate, Promotion
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/", response_model=Payment)
def create_payment_route(request: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db=db, request=request)

@router.get("/", response_model=list[Payment])
def get_all_payments_route(db: Session = Depends(get_db)):
    return get_all_payments(db=db)

@router.post("/promotions/", response_model=Promotion)
def create_promotion_route(request: PromotionCreate, db: Session = Depends(get_db)):
    return create_promotion(db=db, request=request)