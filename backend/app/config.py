"""Application configuration using Pydantic Settings."""

from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Application metadata
    APP_NAME: str = Field(default="Pulse Platform", description="Application name")
    APP_VERSION: str = Field(default="0.1.0", description="Application version")
    APP_ENV: str = Field(default="development", description="Application environment")
    DEBUG: bool = Field(default=True, description="Debug mode")

    # Server configuration
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")

    # Database configuration (for Sprint 1)
    MONGODB_URI: str = Field(
        default="mongodb://localhost:27017/pulse",
        description="MongoDB connection URI"
    )

    # Cache configuration (for Sprint 1)
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Redis connection URL"
    )

    # AI/LLM APIs
    OPENAI_API_KEY: str = Field(
        default="",
        description="OpenAI API key for LLM integration"
    )
    OPENAI_API_BASE: str = Field(
        default="https://api.openai.com/v1",
        description="OpenAI API base URL"
    )

    # CORS configuration (accepts either list or comma-separated string)
    CORS_ORIGINS: str = Field(
        default="http://localhost:3000,http://localhost:5173",
        description="Allowed CORS origins (comma-separated)"
    )
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins as a list."""
        if isinstance(self.CORS_ORIGINS, list):
            return self.CORS_ORIGINS
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]

    # Logging
    LOG_LEVEL: str = Field(default="DEBUG", description="Logging level")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
