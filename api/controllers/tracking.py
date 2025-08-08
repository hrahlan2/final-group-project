
from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models import tracking
from api.schemas import tracking as tracking_schemas

def get_tracking_by_number(db: Session, tracking_number: str):
    tracking_entry = db.query(tracking.Tracking).filter(tracking.Tracking.tracking_number == tracking_number).first()
    return tracking_entry

def update_tracking(db: Session, tracking_number: str, update_data: tracking_schemas.TrackingUpdate):
    tracking_entry = db.query(tracking.Tracking).filter(tracking.Tracking.tracking_number == tracking_number).first()
    if not tracking_entry:
        return None
    if update_data.status is not None:
        tracking_entry.status = update_data.status
    if update_data.estimated_delivery is not None:
        tracking_entry.estimated_delivery = update_data.estimated_delivery

    db.commit()
    db.refresh(tracking_entry)
    return tracking_entry
