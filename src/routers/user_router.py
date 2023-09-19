from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import database
from schemas.profile_schema import ShowProfile, CreateProfile
from services.profile_service import create_profile

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
