from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class DeliveryOption(Base):
    __tablename__ = "delivery_options"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    method = Column(String(20), nullable=False)  # "delivery" or "takeout"
