from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from models.models import RoleEnum


class RoleResponse(BaseModel):
    id: int
    name: RoleEnum

    class Config:
        from_attributes = True


class AdministratorBase(BaseModel):
    name: str = Field(max_length=255)
    email: EmailStr

    class Config:
        from_attributes = True


class AdministratorCreate(AdministratorBase):
    password: str = Field(min_length=8)


class AdministratorUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr]
    password: Optional[str] = Field(None, min_length=8)


class AdministratorResponse(AdministratorBase):
    id: int
    is_active: bool
    is_superuser: bool
    roles: list[RoleResponse]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
