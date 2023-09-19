from pydantic import BaseModel, EmailStr


class CreateProfile(BaseModel):
    fullname: str
    email: EmailStr
    phone: str


class ShowProfile(CreateProfile):
    fullname: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True
