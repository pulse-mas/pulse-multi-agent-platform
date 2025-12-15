"""System information service."""

import sys
import time
from typing import Dict, Any
from app.config import settings


# Track application start time
_start_time = time.time()


class SystemService:
    """Service for retrieving system information."""

    @staticmethod
    def get_python_version() -> str:
        """Get the current Python version."""
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

    @staticmethod
    def get_uptime() -> float:
        """Get application uptime in seconds."""
        return time.time() - _start_time

    @staticmethod
    def get_dependency_status() -> Dict[str, Any]:
        """Get status of external dependencies."""
        dependencies = {}

        # MongoDB status (placeholder for Sprint 1)
        dependencies["mongodb"] = {
            "status": "not_configured",
            "message": "MongoDB integration planned for Sprint 1"
        }

        # Redis status (placeholder for Sprint 1)
        dependencies["redis"] = {
            "status": "not_configured",
            "message": "Redis integration planned for Sprint 1"
        }

        # OpenAI API status
        if settings.OPENAI_API_KEY:
            dependencies["openai"] = {
                "status": "configured",
                "api_base": settings.OPENAI_API_BASE
            }
        else:
            dependencies["openai"] = {
                "status": "not_configured",
                "message": "OPENAI_API_KEY not set"
            }

        return dependencies

    @classmethod
    def get_system_info(cls) -> Dict[str, Any]:
        """Get comprehensive system information."""
        return {
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "python_version": cls.get_python_version(),
            "uptime_seconds": round(cls.get_uptime(), 2),
            "environment": settings.APP_ENV,
            "dependencies": cls.get_dependency_status()
        }


# Singleton instance
system_service = SystemService()
