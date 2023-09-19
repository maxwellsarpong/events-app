import re
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.profile_models import Profile
from schemas.profile_schema import CreateProfile, ShowProfile


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


def is_valid_phone(phone: str) -> bool:
    pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    if re.match(pattern, phone):
        return True
    return False
