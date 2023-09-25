from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import database
from schemas.profile_schema import ShowProfile, CreateProfile, UpdateProfile
from services.profile_service import (
    create_profile,
    get_profile_by_phone,
    update_a_profile,
    delete_a_profile,
    get_all_profiles,
)
from typing import List

profile_router = APIRouter()
get_db = database.get_db


@profile_router.post(
    "/api/profile",
    tags=["profile"],
    description="Register a Profile",
    response_model=ShowProfile,
)
async def create_profile_router(
    profile: CreateProfile, db: Session = Depends(get_db)
) -> ShowProfile:
    return await create_profile(profile=profile, db=db)


@profile_router.get(
    "/api/profile/{phone}",
    tags=["profile"],
    description="Get a single Profile",
    response_model=ShowProfile,
)
async def get_a_profile(phone: str, db: Session = Depends(get_db)) -> ShowProfile:
    return await get_profile_by_phone(phone=phone, db=db)


@profile_router.put(
    "/api/profile/{phone}",
    tags=["profile"],
    description="Update a single Profile",
    response_model=ShowProfile,
)
async def update_profile(
    phone: str, profile: UpdateProfile, db: Session = Depends(get_db)
) -> ShowProfile:
    return await update_a_profile(phone=phone, profile=profile, db=db)


@profile_router.delete(
    "/api/profile/{phone}", tags=["profile"], description="delete a single profile"
)
async def delete_profile(phone: str, db: Session = Depends(get_db)) -> dict:
    return await delete_a_profile(phone=phone, db=db)


@profile_router.get(
    "/api/profile", tags=["get all profiles"], description="Retrieve all profile"
)
async def get_profiles(db: Session = Depends(get_db)) -> list[ShowProfile]:
    return await get_all_profiles(db=db)
