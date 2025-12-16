"""Product DNA API endpoints."""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from loguru import logger

from app.models.reddit import (
    Sentiment,
    EnrichedPost,
    CollectionRequest,
    CollectionResponse,
    ProductDNAStats,
)
from app.services.product_dna import product_dna_service


router = APIRouter(prefix="/api/v1/product-dna", tags=["Product DNA"])


@router.post(
    "/collect",
    response_model=CollectionResponse,
    summary="Collect Product DNA",
    description="Trigger Reddit collection and LLM enrichment pipeline",
)
async def collect_product_dna(request: CollectionRequest) -> CollectionResponse:
    """
    Collect posts from Reddit, enrich with LLM analysis, and store in MongoDB.
    
    - **keywords**: List of keywords to search for
    - **subreddits**: Target subreddits (defaults to marketing, socialmedia, smallbusiness)
    - **limit**: Maximum posts to collect (1-100)
    - **time_filter**: Time range (hour, day, week, month, year, all)
    """
    logger.info(f"Starting Product DNA collection: {request.keywords}")
    
    try:
        result = await product_dna_service.collect_and_enrich(request)
        return result
    except Exception as e:
        logger.error(f"Collection failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/",
    response_model=list[EnrichedPost],
    summary="Get Product DNA",
    description="Retrieve stored Product DNA records with optional filters",
)
async def get_product_dna(
    sentiment: Optional[Sentiment] = Query(None, description="Filter by sentiment"),
    subreddit: Optional[str] = Query(None, description="Filter by subreddit"),
    limit: int = Query(50, ge=1, le=500, description="Max records to return"),
    skip: int = Query(0, ge=0, description="Records to skip (pagination)"),
) -> list[EnrichedPost]:
    """
    Retrieve Product DNA records from the database.
    
    Supports filtering by sentiment and subreddit, with pagination.
    """
    try:
        posts = await product_dna_service.get_product_dna(
            sentiment=sentiment,
            subreddit=subreddit,
            limit=limit,
            skip=skip,
        )
        return posts
    except Exception as e:
        logger.error(f"Failed to retrieve Product DNA: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/stats",
    response_model=ProductDNAStats,
    summary="Product DNA Statistics",
    description="Get aggregated statistics about the Product DNA collection",
)
async def get_stats() -> ProductDNAStats:
    """
    Get statistics about the Product DNA collection.
    
    Returns:
    - Total posts collected
    - Breakdown by sentiment
    - Breakdown by subreddit
    - Last collection timestamp
    """
    try:
        stats = await product_dna_service.get_stats()
        return stats
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/ensure-indexes",
    summary="Create Database Indexes",
    description="Create MongoDB indexes for efficient queries",
)
async def ensure_indexes():
    """Create MongoDB indexes for the product_dna collection."""
    try:
        await product_dna_service.ensure_indexes()
        return {"message": "Indexes created successfully"}
    except Exception as e:
        logger.error(f"Failed to create indexes: {e}")
        raise HTTPException(status_code=500, detail=str(e))
