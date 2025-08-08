from datetime import datetime
from pydantic import BaseModel


class TrackingStatusSchema(BaseModel):
    tracking_number: str
    status: str
    last_updated: datetime

class TrackingCreate(TrackingStatusSchema):
    tracking_number: str

class TrackingUpdate:
    pass

class TrackingOut(TrackingStatusSchema):
    tracking_number: str
    created: datetime
    updated: datetime



    class Config:
        orm_mode = True
