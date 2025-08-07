from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas import delivery_options as schema
from ..controllers import delivery_options as controller

router = APIRouter(prefix="/delivery-options", tags=["Delivery/Takeout"])

@router.post("/", response_model=schema.DeliveryOption)
def create_delivery_option(request: schema.DeliveryOptionCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/{order_id}", response_model=schema.DeliveryOption)
def get_delivery_option(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id)

@router.put("/{order_id}", response_model=schema.DeliveryOption)
def update_delivery_option(order_id: int, request: schema.DeliveryOptionCreate, db: Session = Depends(get_db)):
    return controller.update(db, order_id, request)

@router.delete("/{order_id}")
def delete_delivery_option(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, order_id)
