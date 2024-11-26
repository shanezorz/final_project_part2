from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    amount: float
    payment_type: str
    transaction_status: str
    transaction_date: datetime

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(PaymentBase):
    amount: Optional[float] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    transaction_date: Optional[datetime] = None

class Payment(PaymentBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True

class PromotionBase(BaseModel):
    promo_code: str
    discount_percentage: int
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    promo_code: Optional[str] = None
    discount_percentage: Optional[int] = None
    expiration_date: Optional[datetime] = None

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
