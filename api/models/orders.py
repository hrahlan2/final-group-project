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
    total_price = Column(Float)
    tracking_number = Column(String, unique=True, nullable=True, index=True)

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderItem", back_populates="order", cascade="all, delete")
    payment = relationship("Payment", back_populates="order", uselist=False)
    promotions = relationship("Promotion", back_populates="order")

    order_items = relationship("OrderItem", back_populates="order")
    tracking = relationship("TrackingStatus", backpopulates="order", uselist=False)


class TrackingStatus(Base):
    __tablename__ = 'tracking_statuses'

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, ForeignKey("orders.tracking_number"), unique=True, nullable=True)
    tracking_status = Column(String, default="placed")
    last_updated = Column(DATETIME, default=datetime.now())

    orders = relationship("Order", back_populates="tracking_status")