"""Application settings module.

This module defines the application settings.
It uses Pydantic's BaseSettings to load environment variables
and provides a structured way to access configuration values.
"""

import tomllib
from enum import Enum
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Read version from pyproject.toml
with Path.open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)
    version = pyproject["project"]["version"]

DESCRIPTION = """
This is the API documentation for the Baynext project management system.
It provides endpoints for managing projects, datasets, pipelines, and more.

Authentication is handled via JWT tokens, and the system supports
role-based access control to ensure secure and efficient project management.
"""


class Env(str, Enum):
    """Enumeration for application environments.

    Defines the environment in which the application is running.
    """

    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # App settings
    APP_NAME: str = "Baynext API"
    ENV: Env = Env.DEV
    VERSION: str = version
    DEBUG: bool = True
    DESCRIPTION: str = DESCRIPTION

    DATABASE_URL: SecretStr

    # Supabase settings
    SUPABASE_URL: SecretStr
    SUPABASE_KEY: SecretStr
    SUPABASE_SERVICE_ROLE_KEY: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        use_enum_values=True,
    )

    def is_prod(self) -> bool:
        """Check if the application is running in production environment."""
        return self.ENV == Env.PROD


settings = Settings()
