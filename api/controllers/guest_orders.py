from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Order, OrderItem, MenuItem
from schemas.order import OrderCreate, OrderOut

def create(db: Session, request: OrderCreate) -> OrderOut:
    total = 0
    for item in request.items:
        menu = db.query(MenuItem).filter(MenuItem.id == item.menu_item_id).first()
        if not menu:
            raise HTTPException(status_code=404, detail=f"Menu item {item.menu_item_id} not found")
        total += menu.price * item.quantity

    new_order = Order(
        customer_id=None,
        guest_name=request.guest_name,
        guest_phone=request.guest_phone,
        guest_address=request.guest_address,
        status=request.status,
        total_price=total,
        tracking_number=f"TRACK-{str(total)}"  # Replace uuid4 if desired
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in request.items:
        db.add(OrderItem(order_id=new_order.id, menu_item_id=item.menu_item_id, quantity=item.quantity))

    db.commit()
    return new_order

def read_all(db: Session):
    return db.query(Order).filter(Order.customer_id == None).all()

def read_one(db: Session, item_id: int):
    order = db.query(Order).filter(Order.id == item_id, Order.customer_id == None).first()
    if not order:
        raise HTTPException(status_code=404, detail="Guest order not found")
    return order

def delete(db: Session, item_id: int):
    order = db.query(Order).filter(Order.id == item_id, Order.customer_id == None).first()
    if not order:
        raise HTTPException(status_code=404, detail="Guest order not found")
    db.delete(order)
    db.commit()
    return {"detail": "Guest order deleted successfully"}
