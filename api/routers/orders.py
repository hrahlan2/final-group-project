from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from api.schemas.orders import TrackingStatusSchema
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from ..schemas.orders import OrderOut

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=schema.OrderOut)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderOut])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.OrderOut)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.get("/track/{tracking_number}", response_model=TrackingStatusSchema)
def get_tracking_status(tracking_number: int, db: Session = Depends(get_db)):
    status = db.query(TrackingStatusSchema).filter(TrackingStatusSchema.tracking_number == tracking_number.first())
    if not status:
        raise HTTPException(status_code=404, detail="Tracking number not found")
    return status

@router.put("/{item_id}", response_model=schema.OrderOut)
def update(item_id: int, request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

