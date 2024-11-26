from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

# Ingredient Enum for Unit Validation
class UnitType(str, Enum):
    grams = 'grams'
    ounces = 'ounces'
    ml = 'ml'

class IngredientBase(BaseModel):
    name: str
    unit: UnitType

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(IngredientBase):
    name: Optional[str] = None
    unit: Optional[UnitType] = None

class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True

class SandwichBase(BaseModel):
    name: str
    price: float
    calories: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(SandwichBase):
    name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None

class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True
