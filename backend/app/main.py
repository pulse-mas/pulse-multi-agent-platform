"""FastAPI application entry point."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.db.mongodb import mongodb
from app.exceptions.handlers import setup_exception_handlers
from app.middleware.cors import setup_cors
from app.routers import health, product_dna, status
from app.utils.logging import logger, setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for startup and shutdown events.

    Args:
        app: FastAPI application instance
    """
    # Startup
    logger.info("=" * 80)
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    logger.info(f"Environment: {settings.APP_ENV}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"Server: {settings.HOST}:{settings.PORT}")
    logger.info("=" * 80)

    # Connect to MongoDB
    try:
        await mongodb.connect()
        logger.info("MongoDB connected successfully")
    except Exception as e:
        logger.warning(f"MongoDB connection failed: {e}. Some features may be unavailable.")

    yield

    # Shutdown
    logger.info("=" * 80)
    logger.info(f"Shutting down {settings.APP_NAME}")

    # Disconnect from MongoDB
    await mongodb.disconnect()

    logger.info("=" * 80)


def create_app() -> FastAPI:
    """
    Application factory for creating FastAPI instances.

    Returns:
        FastAPI: Configured FastAPI application
    """
    # Setup logging first
    setup_logging()

    # Create FastAPI app
    app = FastAPI(
        title=settings.APP_NAME,
        description=(
            "Pulse Platform - AI-Powered Multi-Agent Social Media Platform\n\n"
            "A sophisticated social media platform leveraging AI agents for content "
            "generation, moderation, and user engagement."
        ),
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # Setup middleware
    setup_cors(app)

    # Setup exception handlers
    setup_exception_handlers(app)

    # Register routers
    app.include_router(health.router)
    app.include_router(status.router)
    app.include_router(product_dna.router)

    logger.info("FastAPI application created successfully")

    return app


# Create the application instance
app = create_app()


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with basic API information."""
    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/health",
        "status": "/api/v1/status",
        "product_dna": "/api/v1/product-dna",
    }
