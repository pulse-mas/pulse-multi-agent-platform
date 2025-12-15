"""System status endpoint."""

from fastapi import APIRouter
from app.models.responses import SystemStatusResponse
from app.services.system import system_service
from app.utils.logging import logger

router = APIRouter(prefix="/api/v1", tags=["Status"])


@router.get(
    "/status",
    response_model=SystemStatusResponse,
    summary="System Status",
    description="Get detailed system information including version, uptime, and dependency status"
)
async def get_status() -> SystemStatusResponse:
    """
    Get comprehensive system status information.
    
    Returns:
        SystemStatusResponse: Detailed system information
    """
    logger.debug("Status endpoint called")
    
    system_info = system_service.get_system_info()
    
    return SystemStatusResponse(**system_info)
