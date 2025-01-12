from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.models import Skill
from schemas.skills_schema import CreateSkill, ShowSkill, UpdateSkill
from typing import Iterable


async def create_skill(skill: CreateSkill, db: Session) -> ShowSkill:
    skill_exist = db.query(Skill).filter(Skill.name == skill.name).first()
    if skill_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Skill already exists"
        )
    new_skill = Skill(name=skill.name)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


async def update_skill(id: int, skill: UpdateSkill, db: Session) -> ShowSkill:
    skill_exist = db.query(Skill).filter(Skill.id == id).first()
    if not skill_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )

    skill_exist.name = skill.name
    db.commit()
    db.refresh(skill_exist)
    return skill_exist


async def get_a_skill(id: int, db: Session) -> ShowSkill:
    skill_exist = db.query(Skill).filter(Skill.id == id).first()
    if not skill_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    return skill_exist


async def get_skills(db: Session) -> Iterable[ShowSkill]:
    return db.query(Skill).all()


async def delete_a_skill(id: int, db: Session) -> dict:
    skill_exist = db.query(Skill).filter(Skill.id == id).first()
    if not skill_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    db.delete(skill_exist)
    db.commit()
    return {"status": "skill deleted successfully"}
