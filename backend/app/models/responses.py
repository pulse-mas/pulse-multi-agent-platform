"""Pydantic models for API responses."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str = Field(..., description="Health status")
    timestamp: datetime = Field(..., description="Current server timestamp")

    class Config:
        json_schema_extra = {
            "example": {"status": "healthy", "timestamp": "2025-12-15T15:50:00.000Z"}
        }


class DependencyInfo(BaseModel):
    """Dependency status information."""

    name: str = Field(..., description="Dependency name")
    status: str = Field(..., description="Connection status")
    details: str | None = Field(None, description="Additional details")


class SystemStatusResponse(BaseModel):
    """System status response model."""

    app_name: str = Field(..., description="Application name")
    version: str = Field(..., description="Application version")
    python_version: str = Field(..., description="Python runtime version")
    uptime_seconds: float = Field(..., description="Server uptime in seconds")
    environment: str = Field(..., description="Current environment (development/production)")
    dependencies: dict[str, Any] = Field(
        default_factory=dict, description="Status of external dependencies"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "app_name": "Pulse Platform",
                "version": "0.1.0",
                "python_version": "3.12.0",
                "uptime_seconds": 1234.56,
                "environment": "development",
                "dependencies": {
                    "mongodb": {"status": "not_configured"},
                    "redis": {"status": "not_configured"},
                },
            }
        }


class ErrorResponse(BaseModel):
    """Error response model."""

    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    details: dict[str, Any] | None = Field(None, description="Additional error details")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")

    class Config:
        json_schema_extra = {
            "example": {
                "error": "ValidationError",
                "message": "Invalid request parameters",
                "details": {"field": "email", "issue": "Invalid format"},
                "timestamp": "2025-12-15T15:50:00.000Z",
            }
        }
