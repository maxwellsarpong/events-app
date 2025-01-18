from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import database
from schemas.admin_schema import (
    AdministratorCreate,
    AdministratorResponse,
    AdministratorUpdate,
)
from services.admin_service import (
    create_admin,
    get_single_admin,
    update_admin,
    delete_admin,
    get_all_admins,
)

admin_router = APIRouter()
get_db = database.get_db


@admin_router.post(
    "/api/admin",
    tags=["admin"],
    description="Register an Admin",
    response_model=AdministratorResponse,
)
async def create_admin_router(
    admin: AdministratorCreate, db: Session = Depends(get_db)
) -> AdministratorResponse:
    return await create_admin(admin=admin, db=db)


@admin_router.get(
    "/api/admin/{id}",
    tags=["admin"],
    description="Get a single Admin",
    response_model=AdministratorResponse,
)
async def get_an_admin(id: int, db: Session = Depends(get_db)) -> AdministratorResponse:
    return await get_single_admin(id=id, db=db)


@admin_router.put(
    "/api/admin/{id}",
    tags=["admin"],
    description="Update a single Admin",
    response_model=AdministratorResponse,
)
async def update_an_admin(
    id: int, admin: AdministratorUpdate, db: Session = Depends(get_db)
) -> AdministratorResponse:
    return await update_admin(id=id, admin=admin, db=db)


@admin_router.delete(
    "/api/admin/{id}", tags=["admin"], description="delete a single Admin"
)
async def delete_an_admin(id: int, db: Session = Depends(get_db)) -> dict:
    return await delete_admin(id=id, db=db)


@admin_router.get(
    "/api/admin",
    tags=["All Admins"],
    description="Retrieve all Admins",
    response_model=list[AdministratorResponse],
)
async def get_admins(db: Session = Depends(get_db)) -> list[AdministratorResponse]:
    return await get_all_admins(db=db)
