from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    card_details = Column(String(100), nullable=False)
    payment_type = Column(String(30), nullable=False)
    transaction_status = Column(String(30), nullable=False)

    order = relationship("Order", back_populates="payment")