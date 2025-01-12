import re
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.models import Profile
from schemas.profile_schema import CreateProfile, ShowProfile, UpdateProfile


async def create_profile(profile: CreateProfile, db: Session) -> ShowProfile:
    profile_exists = db.query(Profile).filter(Profile.phone == profile.phone).first()
    email_exists = db.query(Profile).filter(Profile.email == profile.email).first()
    phone = is_valid_phone(profile.phone)

    if profile_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account with that number already exists",
        )
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account with that email already exists",
        )
    if not phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect phone number"
        )

    new_profile = Profile(
        fullname=profile.fullname, email=profile.email, phone=profile.phone
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


async def get_profile_by_phone(phone: str, db: Session) -> ShowProfile:
    profile_exists = db.query(Profile).filter(Profile.phone == phone).first()
    if not profile_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile does not exists"
        )
    return profile_exists


async def update_a_profile(
    phone: str, profile: UpdateProfile, db: Session
) -> ShowProfile:
    profile_exist = db.query(Profile).filter(Profile.phone == phone).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )

    profile_exist.email = profile.email
    profile_exist.phone = profile.phone
    profile_exist.fullname = profile.fullname
    db.commit()
    db.refresh(profile_exist)
    return profile_exist


async def delete_a_profile(phone: str, db: Session) -> dict:
    try:
        deleted_rows = db.query(Profile).filter(Profile.phone == phone).delete()
        if deleted_rows == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
            )
        db.commit()
        return {"status": "profile deleted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )


async def get_all_profiles(db: Session) -> list[ShowProfile]:
    return db.query(Profile).all()


def is_valid_phone(phone: str) -> bool:
    pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    if re.match(pattern, phone):
        return True
    return False
