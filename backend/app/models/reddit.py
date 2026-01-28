"""Reddit and Product DNA data models."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Sentiment(str, Enum):
    """Sentiment classification labels."""

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class RedditPost(BaseModel):
    """Raw Reddit post data."""

    post_id: str = Field(..., description="Reddit post ID")
    title: str = Field(..., description="Post title")
    body: str = Field(default="", description="Post body/selftext")
    score: int = Field(default=0, description="Upvote score")
    url: str = Field(..., description="Reddit permalink")
    external_url: str | None = Field(None, description="External link if not self post")
    subreddit: str = Field(..., description="Subreddit name")
    author: str = Field(default="[deleted]", description="Post author")
    created_utc: datetime = Field(..., description="Post creation time")
    num_comments: int = Field(default=0, description="Number of comments")
    upvote_ratio: float = Field(default=0.0, description="Upvote ratio")
    is_self: bool = Field(default=True, description="Is self/text post")

    class Config:
        json_schema_extra = {
            "example": {
                "post_id": "abc123",
                "title": "How to improve social media engagement",
                "body": "Looking for tips on...",
                "score": 145,
                "url": "https://reddit.com/r/marketing/...",
                "subreddit": "marketing",
                "author": "user123",
                "created_utc": "2025-12-10T14:30:00Z",
                "num_comments": 23,
                "upvote_ratio": 0.95,
                "is_self": True,
            }
        }


class PostMetadata(BaseModel):
    """Metadata for an enriched post."""

    score: int = Field(default=0)
    url: str = Field(...)
    subreddit: str = Field(...)
    author: str = Field(default="[deleted]")
    created_utc: datetime = Field(...)
    num_comments: int = Field(default=0)
    upvote_ratio: float = Field(default=0.0)


class EnrichedPost(BaseModel):
    """Product DNA record with LLM enrichment."""

    post_id: str = Field(..., description="Original post ID")
    title: str = Field(..., description="Post title")
    body: str = Field(default="", description="Post body")
    sentiment: Sentiment = Field(..., description="LLM-generated sentiment")
    summary: str = Field(..., description="LLM-generated summary")
    metadata: PostMetadata = Field(..., description="Post metadata")
    keywords: list[str] = Field(default_factory=list, description="Search keywords used")
    enriched_at: datetime = Field(
        default_factory=datetime.utcnow, description="Enrichment timestamp"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "post_id": "abc123",
                "title": "How to improve social media engagement",
                "body": "Looking for tips on...",
                "sentiment": "positive",
                "summary": "User seeks advice on increasing social media engagement for small business.",
                "metadata": {
                    "score": 145,
                    "url": "https://reddit.com/r/marketing/...",
                    "subreddit": "marketing",
                    "author": "user123",
                    "created_utc": "2025-12-10T14:30:00Z",
                    "num_comments": 23,
                    "upvote_ratio": 0.95,
                },
                "keywords": ["social media", "engagement"],
                "enriched_at": "2025-12-15T10:00:00Z",
            }
        }


class CollectionRequest(BaseModel):
    """Request to collect Product DNA from Reddit."""

    keywords: list[str] = Field(..., description="Keywords to search for", min_length=1)
    subreddits: list[str] = Field(
        default=["marketing", "socialmedia", "smallbusiness"], description="Subreddits to search"
    )
    limit: int = Field(default=10, ge=1, le=100, description="Max posts to collect")
    time_filter: str = Field(
        default="week", description="Time filter (hour/day/week/month/year/all)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "keywords": ["social media marketing", "engagement tips"],
                "subreddits": ["marketing", "socialmedia"],
                "limit": 10,
                "time_filter": "week",
            }
        }


class CollectionResponse(BaseModel):
    """Response from Product DNA collection."""

    success: bool = Field(...)
    posts_collected: int = Field(...)
    posts_enriched: int = Field(...)
    posts_stored: int = Field(...)
    errors: list[str] = Field(default_factory=list)
    sample: list[EnrichedPost] = Field(
        default_factory=list, description="Sample of collected posts"
    )


class ProductDNAStats(BaseModel):
    """Statistics about Product DNA collection."""

    total_posts: int = Field(...)
    by_sentiment: dict[str, int] = Field(...)
    by_subreddit: dict[str, int] = Field(...)
    last_collection: datetime | None = Field(None)
