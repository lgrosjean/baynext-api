"""Database session management for the application."""

import os
from collections.abc import Generator

from sqlmodel import Session, create_engine
from supabase import Client, create_client

from .settings import settings

engine = create_engine(
    settings.DATABASE_URL.get_secret_value(),
    echo=settings.DEBUG,
)


def get_session() -> Generator[Session, None, None]:
    """Dependency to get a database session.

    Yields:
        Session: A SQLModel session for database operations.

    """
    with Session(engine) as session:
        yield session


def get_supabase_client() -> Client:
    """Dependency to get the Supabase client.

    Yields:
        Client: The Supabase client for database operations.

    """
    supabase: Client = create_client(
        settings.SUPABASE_URL.get_secret_value(),
        settings.SUPABASE_KEY.get_secret_value(),
    )

    return supabase


def get_supabase_admin_auth_client() -> Client:
    """Dependency to get the Supabase admin auth client.

    Yields:
        Client: The Supabase admin auth client for database operations.

    """
    supabase: Client = create_client(
        settings.SUPABASE_URL.get_secret_value(),
        settings.SUPABASE_SERVICE_ROLE_KEY.get_secret_value(),
    )

    return supabase
