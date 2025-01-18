from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from models.models import Administrator
from schemas.admin_schema import (
    AdministratorCreate,
    AdministratorResponse,
    AdministratorUpdate,
)


async def create_admin(
    admin: AdministratorCreate, db: Session
) -> AdministratorResponse:
    admin_exists = (
        db.query(Administrator).filter(Administrator.email == admin.email).first()
    )
    if admin_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Administrator with that email already exists",
        )
    new_admin = Administrator(name=admin.name, email=admin.email)
    new_admin.set_password(admin.password)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


async def get_single_admin(id: int, db: Session) -> AdministratorResponse:
    admin_exists = db.query(Administrator).filter(Administrator.id == id).first()
    if not admin_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admininstrator does not exists",
        )
    return admin_exists


async def update_admin(
    id: int, admin: AdministratorUpdate, db: Session
) -> AdministratorResponse:
    admin_exists = db.query(Administrator).filter(Administrator.id == id).first()
    if not admin_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admininstrator does not exists",
        )

    if admin_exists.name:
        admin_exists.name = admin.name
    if admin.email:
        admin_exists.email = admin.email
    if admin.password:
        # Hash the password if provided
        admin_exists.hashed_password = bcrypt.hash(admin.password)

    db.commit()
    db.refresh(admin_exists)
    return admin_exists


async def delete_admin(id: int, db: Session) -> AdministratorResponse:
    admin_exists = db.query(Administrator).filter(Administrator.id == id).first()
    if not admin_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admininstrator does not exists",
        )
    db.delete(admin_exists)
    db.commit()
    return {"status": status.HTTP_200_OK, "detail": "Admin deleted successfully"}


async def get_all_admins(db: Session) -> list[(AdministratorResponse)]:
    return db.query(Administrator).all()
