from typing import Optional
from pydantic import BaseModel



class PaymentBase(BaseModel):
    order: int
    card_details: str
    payment_type: str
    transaction_status: str

class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True