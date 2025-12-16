"""Product DNA service - orchestrates Reddit collection and LLM enrichment."""

import asyncio
from datetime import datetime
from typing import Optional
from loguru import logger

from app.integrations.reddit import reddit_tool, RedditSearchTool
from app.integrations.llm import llm_service, LLMService
from app.db.mongodb import mongodb
from app.models.reddit import (
    EnrichedPost,
    PostMetadata,
    Sentiment,
    CollectionRequest,
    CollectionResponse,
    ProductDNAStats,
)


class ProductDNAService:
    """Orchestrates Reddit data collection, LLM enrichment, and storage."""

    COLLECTION_NAME = "product_dna"

    def __init__(
        self,
        reddit: Optional[RedditSearchTool] = None,
        llm: Optional[LLMService] = None,
    ):
        """
        Initialize Product DNA service.
        
        Args:
            reddit: Reddit search tool instance
            llm: LLM service instance
        """
        self.reddit = reddit or reddit_tool
        self.llm = llm or llm_service

    @property
    def collection(self):
        """Get the product_dna MongoDB collection."""
        return mongodb.get_collection(self.COLLECTION_NAME)

    async def collect_and_enrich(
        self,
        request: CollectionRequest,
    ) -> CollectionResponse:
        """
        Collect posts from Reddit and enrich with LLM analysis.
        
        Args:
            request: Collection request parameters
            
        Returns:
            CollectionResponse with results
        """
        errors = []
        posts_collected = 0
        posts_enriched = 0
        posts_stored = 0
        enriched_posts = []

        try:
            # Step 1: Collect from Reddit
            logger.info(f"Collecting posts for keywords: {request.keywords}")
            
            raw_posts = self.reddit.search_subreddits(
                keywords=request.keywords,
                subreddits=request.subreddits,
                limit=request.limit,
                time_filter=request.time_filter,
            )
            posts_collected = len(raw_posts)
            logger.info(f"Collected {posts_collected} posts from Reddit")

            # Step 2: Enrich with LLM (in batches to avoid rate limits)
            for post in raw_posts:
                try:
                    enriched = await self._enrich_post(post, request.keywords)
                    enriched_posts.append(enriched)
                    posts_enriched += 1
                except Exception as e:
                    logger.warning(f"Failed to enrich post {post.get('post_id')}: {e}")
                    errors.append(f"Enrichment failed for {post.get('post_id')}: {str(e)}")

            logger.info(f"Enriched {posts_enriched}/{posts_collected} posts")

            # Step 3: Store in MongoDB
            if enriched_posts:
                posts_stored = await self._store_posts(enriched_posts)
                logger.info(f"Stored {posts_stored} posts in MongoDB")

        except Exception as e:
            logger.error(f"Collection pipeline error: {e}")
            errors.append(f"Pipeline error: {str(e)}")

        return CollectionResponse(
            success=len(errors) == 0,
            posts_collected=posts_collected,
            posts_enriched=posts_enriched,
            posts_stored=posts_stored,
            errors=errors,
            sample=enriched_posts[:3],  # Return first 3 as sample
        )

    async def _enrich_post(self, post: dict, keywords: list[str]) -> EnrichedPost:
        """Enrich a single post with LLM analysis."""
        title = post.get("title", "")
        body = post.get("body", "")

        # Run sentiment and summary analysis
        sentiment_result, summary = await asyncio.gather(
            self.llm.analyze_sentiment(title, body),
            self.llm.generate_summary(title, body),
        )

        # Build enriched post
        metadata = PostMetadata(
            score=post.get("score", 0),
            url=post.get("url", ""),
            subreddit=post.get("subreddit", ""),
            author=post.get("author", "[deleted]"),
            created_utc=post.get("created_utc", datetime.utcnow()),
            num_comments=post.get("num_comments", 0),
            upvote_ratio=post.get("upvote_ratio", 0.0),
        )

        return EnrichedPost(
            post_id=post.get("post_id", ""),
            title=title,
            body=body,
            sentiment=Sentiment(sentiment_result.sentiment.value),
            summary=summary,
            metadata=metadata,
            keywords=keywords,
            enriched_at=datetime.utcnow(),
        )

    async def _store_posts(self, posts: list[EnrichedPost]) -> int:
        """Store enriched posts in MongoDB with upsert."""
        stored_count = 0
        
        for post in posts:
            try:
                # Use upsert to avoid duplicates
                result = await self.collection.update_one(
                    {"post_id": post.post_id},
                    {"$set": post.model_dump()},
                    upsert=True,
                )
                if result.upserted_id or result.modified_count:
                    stored_count += 1
            except Exception as e:
                logger.error(f"Failed to store post {post.post_id}: {e}")

        return stored_count

    async def get_product_dna(
        self,
        sentiment: Optional[Sentiment] = None,
        subreddit: Optional[str] = None,
        limit: int = 50,
        skip: int = 0,
    ) -> list[EnrichedPost]:
        """
        Retrieve stored Product DNA records.
        
        Args:
            sentiment: Filter by sentiment
            subreddit: Filter by subreddit
            limit: Maximum records to return
            skip: Number of records to skip (for pagination)
            
        Returns:
            List of enriched posts
        """
        query = {}
        
        if sentiment:
            query["sentiment"] = sentiment.value
        if subreddit:
            query["metadata.subreddit"] = subreddit

        cursor = self.collection.find(query).skip(skip).limit(limit).sort("enriched_at", -1)
        
        posts = []
        async for doc in cursor:
            doc.pop("_id", None)  # Remove MongoDB _id
            posts.append(EnrichedPost(**doc))

        return posts

    async def get_stats(self) -> ProductDNAStats:
        """Get statistics about the Product DNA collection."""
        total = await self.collection.count_documents({})

        # Aggregate by sentiment
        sentiment_pipeline = [
            {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
        ]
        sentiment_cursor = self.collection.aggregate(sentiment_pipeline)
        by_sentiment = {}
        async for doc in sentiment_cursor:
            by_sentiment[doc["_id"]] = doc["count"]

        # Aggregate by subreddit
        subreddit_pipeline = [
            {"$group": {"_id": "$metadata.subreddit", "count": {"$sum": 1}}}
        ]
        subreddit_cursor = self.collection.aggregate(subreddit_pipeline)
        by_subreddit = {}
        async for doc in subreddit_cursor:
            by_subreddit[doc["_id"]] = doc["count"]

        # Get last collection time
        last_doc = await self.collection.find_one(
            {},
            sort=[("enriched_at", -1)]
        )
        last_collection = last_doc.get("enriched_at") if last_doc else None

        return ProductDNAStats(
            total_posts=total,
            by_sentiment=by_sentiment,
            by_subreddit=by_subreddit,
            last_collection=last_collection,
        )

    async def ensure_indexes(self) -> None:
        """Create MongoDB indexes for efficient queries."""
        await self.collection.create_index("post_id", unique=True)
        await self.collection.create_index("sentiment")
        await self.collection.create_index("metadata.subreddit")
        await self.collection.create_index("enriched_at")
        logger.info("MongoDB indexes created for product_dna collection")


# Singleton instance
product_dna_service = ProductDNAService()
