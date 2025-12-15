"""Health check endpoint."""

from datetime import datetime
from fastapi import APIRouter
from app.models.responses import HealthResponse
from app.utils.logging import logger

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Simple health check endpoint to verify the API is running",
    tags=["Health"]
)
async def health_check() -> HealthResponse:
    """
    Perform a basic health check.
    
    Returns:
        HealthResponse: Health status and timestamp
    """
    logger.debug("Health check endpoint called")
    
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow()
    )
