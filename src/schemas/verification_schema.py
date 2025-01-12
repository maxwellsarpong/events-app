from pydantic import BaseModel


class CreateVerification(BaseModel):
    certificate: str
    verfication_code: int

    class Config:
        orm_mode = True


class ShowsVerification(CreateVerification):
    pass


class UpdateVerification(CreateVerification):
    pass
