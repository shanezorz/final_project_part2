from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers.menu import create_sandwich, get_all_sandwiches, get_sandwich_by_id, update_sandwich, delete_sandwich
from ..schemas.menu import SandwichCreate, SandwichUpdate, Sandwich
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/sandwiches",
    tags=["Sandwiches"]
)

@router.post("/", response_model=Sandwich)
def create_sandwich_route(request: SandwichCreate, db: Session = Depends(get_db)):
    return create_sandwich(db=db, request=request)

@router.get("/", response_model=list[Sandwich])
def get_all_sandwiches_route(db: Session = Depends(get_db)):
    return get_all_sandwiches(db=db)

@router.get("/{sandwich_id}", response_model=Sandwich)
def get_sandwich_by_id_route(sandwich_id: int, db: Session = Depends(get_db)):
    return get_sandwich_by_id(db=db, sandwich_id=sandwich_id)

@router.put("/{sandwich_id}", response_model=Sandwich)
def update_sandwich_route(sandwich_id: int, request: SandwichUpdate, db: Session = Depends(get_db)):
    return update_sandwich(db=db, sandwich_id=sandwich_id, request=request)

@router.delete("/{sandwich_id}", response_model=dict)
def delete_sandwich_route(sandwich_id: int, db: Session = Depends(get_db)):
    return delete_sandwich(db=db, sandwich_id=sandwich_id)