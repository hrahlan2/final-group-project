from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas import payments as schema
from ..controllers import payments as controller

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=schema.Payment)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/{payment_id}", response_model=schema.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id)

@router.put("/{payment_id}", response_model=schema.Payment)
def update_payment(payment_id: int, request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.update(db, payment_id, request)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id)
