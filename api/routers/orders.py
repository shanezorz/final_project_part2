from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..controllers.orders import create_order, get_all_orders, get_order_by_id, update_order, delete_order
from ..schemas.orders import OrderCreate, OrderUpdate, Order
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=Order)
def create_order_route(request: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, request=request)

@router.get("/", response_model=list[Order])
def get_all_orders_route(db: Session = Depends(get_db)):
    return get_all_orders(db=db)

@router.get("/{order_id}", response_model=Order)
def get_order_by_id_route(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(db=db, order_id=order_id)

@router.put("/{order_id}", response_model=Order)
def update_order_route(order_id: int, request: OrderUpdate, db: Session = Depends(get_db)):
    return update_order(db=db, order_id=order_id, request=request)

@router.delete("/{order_id}", response_model=dict)
def delete_order_route(order_id: int, db: Session = Depends(get_db)):
    return delete_order(db=db, order_id=order_id)
