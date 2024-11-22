from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.orders import Order, OrderDetail
from sqlalchemy.exc import SQLAlchemyError


def create_order(db: Session, request):
    new_order = Order(
        customer_id=request.customer_id,
        total_price=request.total_price,
        tracking_number=request.tracking_number,
        status=request.status
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")

    return new_order


def get_all_orders(db: Session):
    try:
        orders = db.query(Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return orders


def get_order_by_id(db: Session, order_id: int):
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return order


def update_order(db: Session, order_id: int, request):
    try:
        order = db.query(Order).filter(Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        update_data = request.dict(exclude_unset=True)
        order.update(update_data, synchronize_session=False)
        db.commit()

        # Verify that the order was updated
        updated_order = order.first()
        if not updated_order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not updated")

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")

    return updated_order


def delete_order(db: Session, order_id: int):
    try:
        order = db.query(Order).filter(Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        order.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return {"message": "Order deleted successfully"}
