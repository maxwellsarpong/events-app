from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewer_name = Column(String, nullable=False)
    service_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    strength = Column(String, nullable=True, info={"A brief summary of what went well"})
    weakness = Column(
        String, nullable=True, info={"A brief summary of what could be impoved"}
    )
    suggestions = Column(
        String, nullable=True, info={"A brie suggestion on how to improve"}
    )
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Verification(Base):
    __tablename__ = "verification"

    id = Column(Integer, primary_key=True, autoincrement=True)
    certificate = Column(String, nullable=False, unique=True)
    verification_code = Column(Integer, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
