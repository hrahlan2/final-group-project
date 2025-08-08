from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"
    promo_code = Column(String(50), primary_key=True, index=True)
    Expiration_date = Column(DATETIME, default=datetime.now(), nullable=False)
    is_expired = Column(String(5), default="NO")
