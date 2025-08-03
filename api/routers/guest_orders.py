from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import guest_orders as controller
from ..schemas import order_schemas as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Guest Orders"],
    prefix="/guest-orders"
)

@router.post("/", response_model=schema.OrderOut, status_code=201)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderOut])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.OrderOut)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
