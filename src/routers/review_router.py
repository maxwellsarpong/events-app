from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import database
from schemas.review_schema import ShowReview, CreateReview, UpdateReview
from services.review_service import (
    create_review,
    get_review_by_id,
    update_a_review,
    delete_a_review,
    get_all_review,
)
from typing import List

review_router = APIRouter()
get_db = database.get_db


@review_router.post(
    "/api/review",
    tags=["review"],
    description="Register a Review",
    response_model=ShowReview,
)
async def create_review_router(
    review: CreateReview, db: Session = Depends(get_db)
) -> ShowReview:
    return await create_review(review=review, db=db)


@review_router.get(
    "/api/review/{id}",
    tags=["review"],
    description="Get a single Review",
    response_model=ShowReview,
)
async def get_a_review(id: int, db: Session = Depends(get_db)) -> ShowReview:
    return await get_review_by_id(id=id, db=db)


@review_router.put(
    "/api/review/{id}",
    tags=["review"],
    description="Update a single Review",
    response_model=ShowReview,
)
async def update_review(
    id: id, review: UpdateReview, db: Session = Depends(get_db)
) -> ShowReview:
    return await update_a_review(id=id, review=review, db=db)


@review_router.delete(
    "/api/review/{id}", tags=["review"], description="delete a single review"
)
async def delete_review(id: int, db: Session = Depends(get_db)) -> dict:
    return await delete_a_review(id=id, db=db)


@review_router.get(
    "/api/review", tags=["get all reviews"], description="Retrieve all review"
)
async def get_reviews(db: Session = Depends(get_db)) -> list[ShowReview]:
    return await get_all_review(db=db)
