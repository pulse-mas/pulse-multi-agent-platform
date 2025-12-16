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

    # Database configuration
    MONGODB_URI: str = Field(
        default="mongodb://localhost:27017",
        description="MongoDB connection URI"
    )
    MONGODB_DB_NAME: str = Field(
        default="pulse",
        description="MongoDB database name"
    )

    # Cache configuration (for Sprint 1)
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Redis connection URL"
    )

    # Reddit API
    REDDIT_CLIENT_ID: str = Field(
        default="",
        description="Reddit API client ID"
    )
    REDDIT_CLIENT_SECRET: str = Field(
        default="",
        description="Reddit API client secret"
    )
    REDDIT_USER_AGENT: str = Field(
        default="PulsePlatform/1.0",
        description="Reddit API user agent"
    )

    # LLM Configuration (GitHub Models or OpenAI)
    GITHUB_TOKEN: str = Field(
        default="",
        description="GitHub token for GitHub Models API"
    )
    OPENAI_API_KEY: str = Field(
        default="",
        description="OpenAI API key (fallback if GITHUB_TOKEN not set)"
    )
    LLM_MODEL: str = Field(
        default="gpt-4o",
        description="LLM model name"
    )
    LLM_BASE_URL: str = Field(
        default="https://models.inference.ai.azure.com",
        description="LLM API base URL (GitHub Models endpoint)"
    )

    # CORS configuration
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

