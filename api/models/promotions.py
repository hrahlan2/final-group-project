from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from datetime import datetime

class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    promo_code = Column(String(100), unique=True)
    expiration_date = Column(DateTime, default=datetime.utcnow)
    is_expired = Column(Boolean, default=False)
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship("Order", back_populates="promotions")
