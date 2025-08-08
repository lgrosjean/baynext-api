"""API v1 module for user management."""

from fastapi import APIRouter

from .me import router as me_router

router = APIRouter(prefix="/user")

# Include the sub-routers
router.include_router(me_router)

for route in router.routes:
    route.path = route.path.rstrip("/")
