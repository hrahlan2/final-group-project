from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    promo_code: str
    expiration_date: datetime
    is_expired: bool

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    promo_code: str
    class Config:
        orm_mode = True
