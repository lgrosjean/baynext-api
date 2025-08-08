"""API router for project-related endpoints.

This module defines the API endpoints for managing resources related to a specific project.
"""

from fastapi import APIRouter

from .base import router as base_router

router = APIRouter(prefix="/{project_id}")
router.include_router(base_router)

for route in router.routes:
    route.path = route.path.rstrip("/")
