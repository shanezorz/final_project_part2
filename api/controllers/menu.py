from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.menu import Sandwich, Ingredient, Resource
from sqlalchemy.exc import SQLAlchemyError


def create_sandwich(db: Session, request):
    new_sandwich = Sandwich(
        name=request.name,
        price=request.price,
        calories=request.calories
    )

    try:
        db.add(new_sandwich)
        db.commit()
        db.refresh(new_sandwich)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")

    return new_sandwich


def get_all_sandwiches(db: Session):
    try:
        sandwiches = db.query(Sandwich).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return sandwiches


def get_sandwich_by_id(db: Session, sandwich_id: int):
    try:
        sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
        if sandwich is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return sandwich


def update_sandwich(db: Session, sandwich_id: int, request):
    try:
        sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id)
        if not sandwich.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

        update_data = request.dict(exclude_unset=True)
        sandwich.update(update_data, synchronize_session=False)
        db.commit()

        # Verify that the sandwich was updated
        updated_sandwich = sandwich.first()
        if not updated_sandwich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not updated")

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")

    return updated_sandwich


def delete_sandwich(db: Session, sandwich_id: int):
    try:
        sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id)
        if not sandwich.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
        sandwich.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database error: {error}")
    return {"message": "Sandwich deleted successfully"}