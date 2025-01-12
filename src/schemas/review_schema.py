from pydantic import BaseModel, Field
from datetime import datetime


class CreateReview(BaseModel):
    reviewer_name: str
    service_name: str
    rating: int
    weakness: str
    strength: str
    suggestions: str

    class Config:
        orm_mode = True


class ShowReview(CreateReview):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateReview(CreateReview):
    pass
