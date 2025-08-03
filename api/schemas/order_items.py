from pydantic import BaseModel


class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
