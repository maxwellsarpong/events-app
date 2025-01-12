from pydantic import BaseModel, Field
from datetime import datetime


class CreateReview(BaseModel):
    id: int = Field(None, alias="id")
    reviewer_name: str
    service_name: str
    rating: int
    weakness: str
    strength: str
    suggestions: str

    class Config:
        from_attributes = True


class ShowReview(CreateReview):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateReview(CreateReview):
    pass
