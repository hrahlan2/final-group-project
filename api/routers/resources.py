from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas.resources import Resource, ResourceCreate
from api.controllers import resources
from api.dependencies.database import get_db

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/", response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db, resource)

@router.get("/", response_model=list[Resource])
def read_resources(db: Session = Depends(get_db)):
    return resources.get_resources(db)
