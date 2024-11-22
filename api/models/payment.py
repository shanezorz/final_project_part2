from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL, nullable=False)
    payment_type = Column(String(50), nullable=False)  # Added length
    transaction_status = Column(String(50), nullable=False)  # Added length
    transaction_date = Column(DATETIME, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="payments")

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    promo_code = Column(String(50), unique=True, nullable=False)  # Added length
    discount_percentage = Column(Integer, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)