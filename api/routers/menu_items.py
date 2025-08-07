from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import database
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema

router = APIRouter(prefix="/menu-items", tags=["Menu Items"])

@router.get("/", response_model=list[schema.MenuItem])
def get_all_items(db: Session = Depends(database.get_db)):
    return controller.get_all_items(db)

@router.get("/{item_id}", response_model=schema.MenuItem)
def get_item(item_id: int, db: Session = Depends(database.get_db)):
    item = controller.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=schema.MenuItem)
def create_item(item: schema.MenuItemCreate, db: Session = Depends(database.get_db)):
    return controller.create_item(db, item)

@router.put("/{item_id}", response_model=schema.MenuItem)
def update_item(item_id: int, item: schema.MenuItemUpdate, db: Session = Depends(database.get_db)):
    return controller.update_item(db, item_id, item)

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    return controller.delete_item(db, item_id)
