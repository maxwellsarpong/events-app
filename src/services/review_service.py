from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.models import Review
from schemas.review_schema import CreateReview, ShowReview, UpdateReview


async def create_review(review: CreateReview, db: Session) -> ShowReview:
    review_exists = db.query(Review).filter(Review.id == review.id.first())

    if review_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Review already exists",
        )

    new_review = Review(
        reviewer_name=review.reviewer_name,
        skill_id=review.skill_id,
        rating=review.rating,
        weakness=review.weakness,
        strength=review.strength,
        suggestions=review.suggestions,
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


async def get_review_by_id(id: int, db: Session) -> ShowReview:
    review_exists = db.query(Review).filter(Review.id == id).first()
    if not review_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Review does not exists"
        )
    return review_exists


async def update_a_review(id: int, review: UpdateReview, db: Session) -> ShowReview:
    review_exist = db.query(Review).filter(Review.id == id).first()
    if not review_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Review not found"
        )

    review_exist.reviewer_name = review.reviewer_name
    review_exist.skill_id = review.skill_id
    review_exist.rating = review.rating
    review_exist.weakness = review.weakness
    review_exist.strength = review.strength
    review_exist.suggestions = review.suggestions
    db.commit()
    db.refresh(review_exist)
    return review_exist


async def delete_a_review(id: int, db: Session) -> dict:
    try:
        deleted_rows = db.query(Review).filter(Review.id == id).delete()
        if deleted_rows == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Review not found"
            )
        db.commit()
        return {"status": "review deleted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Review not found"
        )


async def get_all_review(db: Session) -> list[ShowReview]:
    return db.query(Review).all()
