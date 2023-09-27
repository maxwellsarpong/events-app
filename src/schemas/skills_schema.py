from pydantic import BaseModel
from datetime import datetime


class CreateSkill(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ShowSkill(CreateSkill):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateSkill(CreateSkill):
    pass
