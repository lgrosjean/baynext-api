"""Defines dependencies for FastAPI routes."""

from typing import Annotated
from uuid import uuid4

from fastapi import Depends, Path
from fastapi.security import HTTPAuthorizationCredentials
from sqlmodel import Session

from app.core.db import Client, get_session, get_supabase_client
from app.core.exceptions import InvalidApiKeyError, MissingApiKeyError
from app.core.logging import get_logger
from app.core.security import get_bearer_token
from app.models import User
from app.services.supabase.user import UserService

ProjectId = Annotated[
    str,
    Path(example=f"{uuid4()!s}"),
]


logger = get_logger(__name__)

SessionDep = Annotated[Session, Depends(get_session)]


# TODO: move to middleware
def get_current_user(
    supabase: Annotated[Client, Depends(get_supabase_client)],
    key: Annotated[HTTPAuthorizationCredentials, Depends(get_bearer_token)],
) -> User:
    """Get the currently authenticated user from the API key."""
    if not key:
        raise MissingApiKeyError

    response = (
        supabase.table("apiKey")
        .select("*")
        .eq("key", key.credentials)
        .single()
        .execute()
    )

    if not response.data:
        logger.warning("Unauthorized access attempt with key: %s", key.credentials)
        raise InvalidApiKeyError

    user_id = response.data.get("user_id")

    user = UserService().get_user_by_id(user_id)

    if not user:
        logger.warning("Unauthorized access attempt with key: %s", key.credentials)
        raise InvalidApiKeyError

    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
"""Dependency to get the currently authenticated user."""
