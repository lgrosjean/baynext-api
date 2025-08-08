"""User model using SQLModel."""

from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel

from .base import TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from .project import Project


class UserBase(SQLModel):
    """Base user model with common fields."""

    email: EmailStr


class User(UserBase, UUIDMixin, TimestampMixin, table=True):
    """User model."""

    __tablename__ = "users"

    # Relationships
    projects: list["Project"] | None = Relationship(back_populates="owner")

    class Config:
        """Pydantic configuration."""

        # Enable ORM mode for Pydantic compatibility
        from_attributes = True
