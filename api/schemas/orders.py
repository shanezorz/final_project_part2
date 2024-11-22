from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderDetailBase(BaseModel):
    amount: int

class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int

class OrderDetailUpdate(OrderDetailBase):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    total_price: float
    tracking_number: str
    status: str
    order_date: datetime

class OrderCreate(OrderBase):
    customer_id: int

class OrderUpdate(OrderBase):
    total_price: Optional[float] = None
    tracking_number: Optional[str] = None
    status: Optional[str] = None
    order_date: Optional[datetime] = None

class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True
