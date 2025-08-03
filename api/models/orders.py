from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True) # nullable for guest order
    guest_name = Column(String, nullable=True)
    guest_phone = Column(String, nullable=True)
    guest_address = Column(String, nullable=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String, unique=True)
    status = Column(String, default="placed")
    total_price = Column(Float)

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderItem", back_populates="order", cascade="all, delete")
    payment = relationship("Payment", back_populates="order", uselist=False)
    promotions = relationship("Promotion", back_populates="order")

    order_items = relationship("OrderItem", back_populates="order")