from sqlalchemy.orm import Session
from api.models.resources import Resource
from api.schemas.resources import ResourceCreate

def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session):
    return db.query(Resource).all()
