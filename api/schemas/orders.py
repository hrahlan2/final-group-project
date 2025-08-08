from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int

class OrderBase(BaseModel):
    guest_name: Optional[str]
    guest_phone: Optional[str]
    guest_address: Optional[str]
    items: List[OrderItemCreate]

class OrderCreate(OrderBase):
    total_price: float  # calculated client-side or server-side

class OrderOut(BaseModel):
    id: int
    guest_name: Optional[str]
    guest_phone: Optional[str]
    guest_address: Optional[str]
    tracking_number: Optional[str]
    tracking_status: str
    total_price: float
    order_date: str


class TrackingStatusSchema(BaseModel):
    tracking_number: str
    status: str
    last_updated: datetime

    class Config:
        orm_mode = True
