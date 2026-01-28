"""Reddit API integration using PRAW."""

import time
from datetime import datetime

import praw
from loguru import logger
from praw.exceptions import RedditAPIException

from app.config import settings


class RedditSearchTool:
    """AI-enhanced Reddit data collection tool using PRAW."""

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        user_agent: str | None = None,
    ):
        """
        Initialize Reddit client with credentials.

        Args:
            client_id: Reddit API client ID (defaults to env)
            client_secret: Reddit API client secret (defaults to env)
            user_agent: Reddit API user agent (defaults to env)
        """
        self.client_id = client_id or settings.REDDIT_CLIENT_ID
        self.client_secret = client_secret or settings.REDDIT_CLIENT_SECRET
        self.user_agent = user_agent or settings.REDDIT_USER_AGENT

        self._reddit: praw.Reddit | None = None
        self._last_request_time = 0
        self._min_request_interval = 1.0  # Rate limit: 1 request per second

    @property
    def reddit(self) -> praw.Reddit:
        """Lazy initialization of Reddit client."""
        if self._reddit is None:
            if not self.client_id or not self.client_secret:
                raise ValueError(
                    "Reddit credentials not configured. "
                    "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in .env"
                )

            self._reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
            )
            logger.info("Reddit client initialized successfully")

        return self._reddit

    def _rate_limit(self) -> None:
        """Enforce rate limiting between requests."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self._min_request_interval:
            time.sleep(self._min_request_interval - elapsed)
        self._last_request_time = time.time()

    def search_subreddits(
        self,
        keywords: list[str],
        subreddits: list[str] | None = None,
        limit: int = 10,
        time_filter: str = "week",
    ) -> list[dict]:
        """
        Search Reddit for posts matching keywords.

        Args:
            keywords: List of keywords to search for
            subreddits: List of subreddit names (defaults to popular ones)
            limit: Maximum number of posts to return
            time_filter: Time filter (hour, day, week, month, year, all)

        Returns:
            List of post dictionaries with raw Reddit data
        """
        if subreddits is None:
            subreddits = ["marketing", "socialmedia", "smallbusiness", "Entrepreneur"]

        query = " OR ".join(keywords)
        subreddit_str = "+".join(subreddits)

        posts = []

        try:
            self._rate_limit()

            logger.info(f"Searching Reddit: '{query}' in r/{subreddit_str}")

            subreddit = self.reddit.subreddit(subreddit_str)

            for submission in subreddit.search(
                query,
                limit=limit,
                time_filter=time_filter,
                sort="relevance",
            ):
                post_data = self._extract_post_data(submission)
                posts.append(post_data)

                if len(posts) >= limit:
                    break

            logger.info(f"Found {len(posts)} posts matching query")

        except RedditAPIException as e:
            logger.error(f"Reddit API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error searching Reddit: {e}")
            raise

        return posts

    def _extract_post_data(self, submission) -> dict:
        """Extract relevant data from a Reddit submission."""
        return {
            "post_id": submission.id,
            "title": submission.title,
            "body": submission.selftext or "",
            "score": submission.score,
            "url": f"https://reddit.com{submission.permalink}",
            "external_url": submission.url if not submission.is_self else None,
            "subreddit": submission.subreddit.display_name,
            "author": str(submission.author) if submission.author else "[deleted]",
            "created_utc": datetime.utcfromtimestamp(submission.created_utc),
            "num_comments": submission.num_comments,
            "upvote_ratio": submission.upvote_ratio,
            "is_self": submission.is_self,
        }

    def get_post_details(self, post_id: str) -> dict:
        """
        Get detailed information about a specific post.

        Args:
            post_id: Reddit post ID

        Returns:
            Post dictionary with detailed data
        """
        self._rate_limit()

        try:
            submission = self.reddit.submission(id=post_id)
            return self._extract_post_data(submission)
        except Exception as e:
            logger.error(f"Error fetching post {post_id}: {e}")
            raise

    def get_top_comments(self, post_id: str, limit: int = 5) -> list[dict]:
        """
        Get top comments for a post.

        Args:
            post_id: Reddit post ID
            limit: Maximum number of comments

        Returns:
            List of comment dictionaries
        """
        self._rate_limit()

        try:
            submission = self.reddit.submission(id=post_id)
            submission.comments.replace_more(limit=0)

            comments = []
            for comment in submission.comments[:limit]:
                comments.append(
                    {
                        "comment_id": comment.id,
                        "body": comment.body,
                        "score": comment.score,
                        "author": str(comment.author) if comment.author else "[deleted]",
                        "created_utc": datetime.utcfromtimestamp(comment.created_utc),
                    }
                )

            return comments

        except Exception as e:
            logger.error(f"Error fetching comments for {post_id}: {e}")
            raise


# Singleton instance for reuse
reddit_tool = RedditSearchTool()
