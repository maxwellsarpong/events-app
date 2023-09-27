from pydantic import BaseModel, Field


class CreateVerification(BaseModel):
    certificate: str
    verfication_code: int
    skill_id = Field(default=None, foreign_key="Skill.id")

    class Config:
        orm_mode = True


class ShowsVerification(CreateVerification):
    pass


class UpdateVerification(CreateVerification):
    pass
