"""Tests for Reddit integration."""

from unittest.mock import MagicMock, patch


class TestRedditSearchTool:
    """Tests for RedditSearchTool class."""

    def test_reddit_search_returns_posts(self):
        """Test that search returns expected post structure."""
        # Mock PRAW submission
        mock_submission = MagicMock()
        mock_submission.id = "test123"
        mock_submission.title = "Test Post Title"
        mock_submission.selftext = "Test post body content"
        mock_submission.score = 100
        mock_submission.permalink = "/r/marketing/comments/test123"
        mock_submission.url = "https://reddit.com/r/marketing/comments/test123"
        mock_submission.subreddit.display_name = "marketing"
        mock_submission.author = MagicMock()
        mock_submission.author.__str__ = lambda x: "testuser"
        mock_submission.created_utc = 1702656000.0
        mock_submission.num_comments = 10
        mock_submission.upvote_ratio = 0.95
        mock_submission.is_self = True

        with patch("app.integrations.reddit.praw.Reddit") as mock_reddit:
            mock_subreddit = MagicMock()
            mock_subreddit.search.return_value = [mock_submission]
            mock_reddit.return_value.subreddit.return_value = mock_subreddit

            from app.integrations.reddit import RedditSearchTool

            tool = RedditSearchTool(
                client_id="test_id", client_secret="test_secret", user_agent="test_agent"
            )
            tool._reddit = mock_reddit.return_value

            posts = tool.search_subreddits(
                keywords=["test query"], subreddits=["marketing"], limit=10
            )

            assert len(posts) == 1
            assert posts[0]["post_id"] == "test123"
            assert posts[0]["title"] == "Test Post Title"
            assert posts[0]["body"] == "Test post body content"
            assert posts[0]["subreddit"] == "marketing"

    def test_reddit_empty_results(self):
        """Test handling of queries with no matching posts."""
        with patch("app.integrations.reddit.praw.Reddit") as mock_reddit:
            mock_subreddit = MagicMock()
            mock_subreddit.search.return_value = []
            mock_reddit.return_value.subreddit.return_value = mock_subreddit

            from app.integrations.reddit import RedditSearchTool

            tool = RedditSearchTool(
                client_id="test_id", client_secret="test_secret", user_agent="test_agent"
            )
            tool._reddit = mock_reddit.return_value

            posts = tool.search_subreddits(
                keywords=["nonexistent query xyz"], subreddits=["marketing"], limit=10
            )

            assert len(posts) == 0

    def test_extract_post_data_handles_deleted_author(self):
        """Test that deleted authors are handled gracefully."""
        mock_submission = MagicMock()
        mock_submission.id = "test456"
        mock_submission.title = "Test Post"
        mock_submission.selftext = ""
        mock_submission.score = 50
        mock_submission.permalink = "/r/marketing/comments/test456"
        mock_submission.url = "https://example.com"
        mock_submission.subreddit.display_name = "marketing"
        mock_submission.author = None  # Deleted author
        mock_submission.created_utc = 1702656000.0
        mock_submission.num_comments = 5
        mock_submission.upvote_ratio = 0.8
        mock_submission.is_self = False

        from app.integrations.reddit import RedditSearchTool

        tool = RedditSearchTool(
            client_id="test_id", client_secret="test_secret", user_agent="test_agent"
        )

        post_data = tool._extract_post_data(mock_submission)

        assert post_data["author"] == "[deleted]"
        assert post_data["external_url"] == "https://example.com"
