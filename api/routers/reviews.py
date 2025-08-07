from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas.reviews import Review, ReviewCreate
from api.controllers import reviews
from api.dependencies.database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return reviews.create_review(db, review)

@router.get("/", response_model=list[Review])
def read_reviews(db: Session = Depends(get_db)):
    return reviews.get_reviews(db)
