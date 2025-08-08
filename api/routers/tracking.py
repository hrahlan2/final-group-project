from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.schemas import tracking as tracking_schemas


router = APIRouter(prefix="/tracking", tags=["tracking"])

@router.get("/{tracking_number}", response_model=tracking_schemas.TrackingOut)
def get_tracking(tracking_number: str, db: Session = Depends(get_db), tracking_controller=None):
    tracking = tracking_controller.get_tracking_by_number(db, tracking_number)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking info not found")
    return tracking

@router.put("/{tracking_number}", response_model=tracking_schemas.TrackingOut)
def update_tracking(tracking_number: str, update_data: tracking_schemas.TrackingUpdate, db: Session = Depends(get_db),
                    tracking_controller=None):
    updated = tracking_controller.update_tracking(db, tracking_number, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Tracking info not found")
    return updated

