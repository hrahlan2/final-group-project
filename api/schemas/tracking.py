from datetime import datetime
from pydantic import BaseModel


class trackingStatusSchema(BaseModel):
    tracking_number: str
    status: str
    last_updated: datetime

    class config:
        orm_mode = True