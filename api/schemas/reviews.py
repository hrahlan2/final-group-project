from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None  # Optional for flexibility

class ReviewCreate(ReviewBase):
    customer_id: int
    order_id: int

class Review(ReviewBase):
    id: int
    customer_id: int
    order_id: int

    class Config:
        orm_mode = True  # Needed to convert from SQLAlchemy model to Pydantic
