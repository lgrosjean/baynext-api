"""User service for managing user-related operations."""

from typing import TYPE_CHECKING

from app.core.db import get_supabase_admin_auth_client
from app.models.user import User

if TYPE_CHECKING:
    from gotrue.types import UserResponse


class UserService:
    """Service for managing user-related operations on Supabase."""

    def __init__(self) -> None:
        """Initialize the user service."""
        self.supabase = get_supabase_admin_auth_client()

    def get_user_by_id(self, user_id: str) -> User | None:
        """Get a user by their ID."""
        response: UserResponse = self.supabase.auth.admin.get_user_by_id(user_id)
        return User(**response.user)
