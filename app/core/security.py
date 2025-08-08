"""Defines security schemes for FastAPI app."""

from fastapi.security import HTTPBearer

get_bearer_token = HTTPBearer(auto_error=False)
