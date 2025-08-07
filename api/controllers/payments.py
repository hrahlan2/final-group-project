from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models.payments import Payments

def create(db: Session, request):
    new_payment = Payments(
        order=request.order,
        card_details=request.card_details,
        payment_type=request.payment_type,
        transaction_status=request.transaction_status
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def read_one(db: Session, payment_id: int):
    payment = db.query(Payments).filter(Payments.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    return payment

def update(db: Session, payment_id: int, request):
    payment = db.query(Payments).filter(Payments.id == payment_id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    payment.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return payment.first()

def delete(db: Session, payment_id: int):
    payment = db.query(Payments).filter(Payments.id == payment_id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    payment.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
