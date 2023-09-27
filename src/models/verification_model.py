from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from settings.database import Base


class Verification(Base):
    __tablename__ = "verification"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    certificate = Column(String, nullable=False, unique=True)
    verification_code = Column(Integer, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    skill_id = Column(Integer, ForeignKey("skill.id"), nullable=False)
    skill = relationship("Skill", foreign_keys="skill_id")
