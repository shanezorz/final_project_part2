from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL, nullable=False)
    calories = Column(Integer)

    order_details = relationship("OrderDetail", back_populates="sandwich")
    ingredients = relationship("Ingredient", secondary="sandwich_ingredients")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    unit = Column(String(100), nullable=False)


class SandwichIngredient(Base):
    __tablename__ = "sandwich_ingredients"

    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    quantity = Column(DECIMAL, nullable=False)
    unit = Column(String(100), nullable=False)

    ingredient = relationship("Ingredient")
