from pydantic import BaseModel


class CreateVerification(BaseModel):
    certificate: str
    verfication_code: int

    class Config:
        from_attributes = True


class ShowsVerification(CreateVerification):
    pass


class UpdateVerification(CreateVerification):
    pass
