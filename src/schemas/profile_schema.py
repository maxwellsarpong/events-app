from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateProfile(BaseModel):
    fullname: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True


class ShowProfile(CreateProfile):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateProfile(CreateProfile):
    pass
