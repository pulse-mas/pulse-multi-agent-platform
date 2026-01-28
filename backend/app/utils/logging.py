"""Logging configuration using Loguru."""

import sys
from pathlib import Path

from loguru import logger

from app.config import settings


def setup_logging() -> None:
    """Configure Loguru logging for the application."""

    # Remove default handler
    logger.remove()

    # Console logging format
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )

    # Add console handler
    logger.add(
        sys.stdout,
        format=log_format,
        level=settings.LOG_LEVEL,
        colorize=True,
        backtrace=True,
        diagnose=True,
    )

    # Add file handler for production
    if settings.APP_ENV == "production":
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        # JSON logging for production
        logger.add(
            log_dir / "pulse_{time:YYYY-MM-DD}.log",
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name}:{function}:{line} | {message}",
            level="INFO",
            rotation="00:00",  # Rotate at midnight
            retention="30 days",  # Keep logs for 30 days
            compression="zip",  # Compress old logs
            serialize=True,  # JSON format
        )

    logger.info(f"Logging configured with level: {settings.LOG_LEVEL}")


# Expose logger for use throughout the application
__all__ = ["logger", "setup_logging"]
