"""Enumeration definitions for the database models."""

from enum import Enum


class ProjectStatus(str, Enum):
    """Enumeration for project status."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    COMPLETED = "completed"
