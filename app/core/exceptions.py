"""Exceptions for authentication and authorization errors."""

from fastapi import status
from fastapi.exceptions import HTTPException


class ForbiddenError(HTTPException):
    """Exception raised for authentication errors."""

    def __init__(self, details: str) -> None:
        """Initialize the exception with a specific status code and detail."""
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=details,
            headers={"WWW-Authenticate": "Bearer"},
        )


class UnauthorizedError(HTTPException):
    """Exception raised for unauthorized access."""

    def __init__(self, details: str) -> None:
        """Initialize the exception with a specific status code and detail."""
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=details,
            headers={"WWW-Authenticate": "Bearer"},
        )


class MissingApiKeyError(HTTPException):
    """Exception raised for missing API key."""

    def __init__(self) -> None:
        """Initialize the exception with a specific status code and detail."""
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is missing",
            headers={"WWW-Authenticate": "Bearer"},
        )


class InvalidApiKeyError(HTTPException):
    """Exception raised for invalid API key."""

    def __init__(self) -> None:
        """Initialize the exception with a specific status code and detail."""
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
