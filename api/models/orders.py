from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(String, nullable=False)
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_details")
