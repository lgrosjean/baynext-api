"""API v1 module."""

from fastapi import APIRouter

from . import projects, user

router = APIRouter(prefix="/v1")

router.include_router(projects.router)
router.include_router(user.router)
