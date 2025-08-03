from sqlalchemy.orm import Session
from models.reviews import Review
from schemas.reviews import ReviewCreate

def create_review(db: Session, review: ReviewCreate):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session):
    return db.query(Review).all()
