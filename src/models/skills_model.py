from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime
from settings.database import Base


class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
