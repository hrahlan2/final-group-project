from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    tracking_number: Optional[str] = None
    status: Optional[str] = "placed"
    total_price: float


class OrderCreate(OrderBase):
    customer_id: int


class OrderUpdate(BaseModel):
        tracking_number: Optional[str] = None
        status: Optional[str] = None
        total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    customer_id: int

    class ConfigDict:
        from_attributes = True
