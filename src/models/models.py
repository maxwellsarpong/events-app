from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
    Enum,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import bcrypt
import enum

Base = declarative_base()


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    years_of_experience = Column(Integer, nullable=True)
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


class RoleEnum(enum.Enum):
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"


# Association table for many-to-many relationship between administrators and roles
admin_roles = Table(
    "admin_roles",
    Base.metadata,
    Column("admin_id", Integer, ForeignKey("administrators.id")),
    Column("role_id", Integer, ForeignKey("roles.id")),
)


class RoleDB(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum), unique=True, nullable=False)


class Administrator(Base):
    __tablename__ = "administrators"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    roles = relationship("RoleDB", secondary=admin_roles, back_populates="admins")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def verify_password(self, password: str) -> bool:
        """Verify the password using bcrypt."""
        return bcrypt.verify(password, self.hashed_password)

    def set_password(self, password: str):
        """Hash and set the password."""
        self.hashed_password = bcrypt.hash(password)


RoleDB.admins = relationship(
    "Administrator", secondary=admin_roles, back_populates="roles"
)
