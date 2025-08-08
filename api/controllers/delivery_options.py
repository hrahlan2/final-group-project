from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models.delivery_options import DeliveryOption

def create(db: Session, request):
    existing = db.query(DeliveryOption).filter(DeliveryOption.order_id == request.order_id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Delivery option for this order already set")
    new_option = DeliveryOption(order_id=request.order_id, method=request.method)
    db.add(new_option)
    db.commit()
    db.refresh(new_option)
    return new_option

def read_one(db: Session, order_id: int):
    option = db.query(DeliveryOption).filter(DeliveryOption.order_id == order_id).first()
    if not option:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Delivery option not found!")
    return option

def update(db: Session, order_id: int, request):
    option = db.query(DeliveryOption).filter(DeliveryOption.order_id == order_id)
    if not option.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Delivery option not found!")
    option.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return option.first()

def delete(db: Session, order_id: int):
    option = db.query(DeliveryOption).filter(DeliveryOption.order_id == order_id)
    if not option.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Delivery option not found!")
    option.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
