from pydantic import BaseModel

class DeliveryOptionBase(BaseModel):
    order_id: int
    method: str

class DeliveryOptionCreate(DeliveryOptionBase):
    pass

class DeliveryOption(DeliveryOptionBase):
    id: int

    class Config:
        orm_mode = True
