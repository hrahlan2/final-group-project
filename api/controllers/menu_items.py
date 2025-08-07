from sqlalchemy.orm import Session
from ..models.menu_items import MenuItem
from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate

def get_all_items(db: Session):
    return db.query(MenuItem).all()

def get_item(db: Session, item_id: int):
    return db.query(MenuItem).filter(MenuItem.id == item_id).first()

def create_item(db: Session, item: MenuItemCreate):
    new_item = MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id: int, item: MenuItemUpdate):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if menu_item:
        for key, value in item.dict(exclude_unset=True).items():
            setattr(menu_item, key, value)
        db.commit()
        db.refresh(menu_item)
    return menu_item

def delete_item(db: Session, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if menu_item:
        db.delete(menu_item)
        db.commit()
    return menu_item
