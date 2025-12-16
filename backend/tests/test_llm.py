"""Tests for LLM integration."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch


class TestLLMService:
    """Tests for LLMService class."""

    @pytest.mark.asyncio
    async def test_sentiment_analysis_positive(self):
        """Test positive sentiment detection."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "positive"

        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService, Sentiment

            service = LLMService(api_key="test_key")
            service._client = mock_client

            result = await service.analyze_sentiment(
                title="Great product, highly recommend!",
                body="This is amazing, absolutely love it."
            )

            assert result.sentiment == Sentiment.POSITIVE

    @pytest.mark.asyncio
    async def test_sentiment_analysis_negative(self):
        """Test negative sentiment detection."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "negative"

        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService, Sentiment

            service = LLMService(api_key="test_key")
            service._client = mock_client

            result = await service.analyze_sentiment(
                title="Terrible experience, avoid!",
                body="Worst product ever, complete waste of money."
            )

            assert result.sentiment == Sentiment.NEGATIVE

    @pytest.mark.asyncio
    async def test_sentiment_analysis_neutral(self):
        """Test neutral sentiment detection."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "neutral"

        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService, Sentiment

            service = LLMService(api_key="test_key")
            service._client = mock_client

            result = await service.analyze_sentiment(
                title="Product update released",
                body="New version is now available for download."
            )

            assert result.sentiment == Sentiment.NEUTRAL

    @pytest.mark.asyncio
    async def test_summary_generation(self):
        """Test summary generation is within word limit."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "User asks for social media marketing tips for small business growth."

        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService

            service = LLMService(api_key="test_key")
            service._client = mock_client

            summary = await service.generate_summary(
                title="How to grow my small business on social media?",
                body="I have a small bakery and want to increase my online presence..."
            )

            # Check summary is within word limit (roughly)
            word_count = len(summary.split())
            assert word_count <= 30  # Allow some buffer over 25

    @pytest.mark.asyncio
    async def test_enrich_post_parallel_execution(self):
        """Test that enrich_post runs sentiment and summary in parallel."""
        mock_sentiment_response = MagicMock()
        mock_sentiment_response.choices = [MagicMock()]
        mock_sentiment_response.choices[0].message.content = "positive"

        mock_summary_response = MagicMock()
        mock_summary_response.choices = [MagicMock()]
        mock_summary_response.choices[0].message.content = "Test summary."

        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            # Return different responses for different calls
            mock_client.chat.completions.create = AsyncMock(
                side_effect=[mock_sentiment_response, mock_summary_response]
            )
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService

            service = LLMService(api_key="test_key")
            service._client = mock_client

            post = {
                "post_id": "test123",
                "title": "Test Title",
                "body": "Test body content"
            }

            enriched = await service.enrich_post(post)

            assert enriched["sentiment"] == "positive"
            assert enriched["summary"] == "Test summary."
            assert enriched["post_id"] == "test123"

    @pytest.mark.asyncio
    async def test_sentiment_error_returns_neutral(self):
        """Test that errors in sentiment analysis default to neutral."""
        with patch("app.integrations.llm.AsyncOpenAI") as mock_openai:
            mock_client = AsyncMock()
            mock_client.chat.completions.create = AsyncMock(
                side_effect=Exception("API Error")
            )
            mock_openai.return_value = mock_client

            from app.integrations.llm import LLMService, Sentiment

            service = LLMService(api_key="test_key")
            service._client = mock_client

            result = await service.analyze_sentiment(
                title="Test",
                body="Test"
            )

            # Should default to neutral on error
            assert result.sentiment == Sentiment.NEUTRAL
