from pydantic import BaseModel
from typing import List, Optional

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int

class OrderBase(BaseModel):
    guest_name: Optional[str]
    guest_phone: Optional[str]
    guest_address: Optional[str]
    status: Optional[str] = "placed"
    items: List[OrderItemCreate]

class OrderCreate(OrderBase):
    total_price: float  # calculated client-side or server-side

class OrderOut(BaseModel):
    id: int
    guest_name: Optional[str]
    guest_phone: Optional[str]
    guest_address: Optional[str]
    tracking_number: Optional[str]
    status: str
    total_price: float
    order_date: str

    class Config:
        orm_mode = True
