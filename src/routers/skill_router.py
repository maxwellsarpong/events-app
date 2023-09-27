from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import database
from schemas.skills_schema import ShowSkill, CreateSkill, UpdateSkill
from services.skill_services import (
    create_skill,
    update_skill,
    get_skills,
    get_a_skill,
    delete_a_skill,
)
from typing import Iterable

skill_router = APIRouter()
get_db = database.get_db


@skill_router.post(
    "/api/skill",
    response_model=ShowSkill,
    tags=["Create a skill"],
    description="Create a skill",
)
async def create_a_skill(
    skill: CreateSkill, db: Session = Depends(get_db)
) -> ShowSkill:
    return await create_skill(skill=skill, db=db)


@skill_router.put(
    "/api/skill/{id}", tags=["Update a skill"], description="Update a skill"
)
async def update_a_skill(
    id: int, skill: UpdateSkill, db: Session = Depends(get_db)
) -> ShowSkill:
    return await update_skill(id=id, skill=skill, db=db)


@skill_router.get("/api/skill", tags=["Get all skills"], description="Get all skills")
async def get_all_skills(db: Session = Depends(get_db)) -> Iterable[ShowSkill]:
    return await get_skills(db=db)


@skill_router.get("/api/skill/{id}", tags=["Get a skill"], description="Get a skill")
async def get_skill_by_id(id: int, db: Session = Depends(get_db)) -> ShowSkill:
    return await get_a_skill(id=id, db=db)


@skill_router.delete(
    "/api/skill/{id}", tags=["Delete a skill"], description="Delete a skill"
)
async def delete_skill_by_id(id: int, db: Session = Depends(get_db)) -> dict:
    return await delete_a_skill(id=id, db=db)
