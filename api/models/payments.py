from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order = Column(Integer, ForeignKey('orders.id'), nullable=False)
    card_details = Column(String, nullable=False)
    payment_type = Column(String, nullable=False)
    transaction_status = Column(String, nullable=False)