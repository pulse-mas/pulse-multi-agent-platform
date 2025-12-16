"""LLM integration using GitHub Models (Azure OpenAI endpoint)."""

import asyncio
from typing import Optional
from enum import Enum
from openai import AsyncOpenAI
from pydantic import BaseModel
from loguru import logger

from app.config import settings


class Sentiment(str, Enum):
    """Sentiment classification labels."""
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class SentimentResult(BaseModel):
    """Result of sentiment analysis."""
    sentiment: Sentiment
    confidence: Optional[float] = None


# Prompt templates
SENTIMENT_PROMPT = """Analyze the sentiment of the following social media post.
Respond with exactly one word: positive, neutral, or negative.

Title: {title}
Content: {body}

Sentiment:"""

SUMMARY_PROMPT = """Summarize the following social media post in one concise sentence (maximum 25 words).
Focus on the main topic, user intent, and any key insights.

Title: {title}
Content: {body}

Summary:"""


class LLMService:
    """LLM integration service using GitHub Models GPT-4o."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        """
        Initialize LLM service.
        
        Args:
            api_key: GitHub token or OpenAI API key
            model: Model name (defaults to gpt-4o)
            base_url: API base URL (defaults to GitHub Models endpoint)
        """
        self.api_key = api_key or settings.GITHUB_TOKEN or settings.OPENAI_API_KEY
        self.model = model or settings.LLM_MODEL
        self.base_url = base_url or settings.LLM_BASE_URL
        
        self._client: Optional[AsyncOpenAI] = None

    @property
    def client(self) -> AsyncOpenAI:
        """Lazy initialization of OpenAI client."""
        if self._client is None:
            if not self.api_key:
                raise ValueError(
                    "LLM API key not configured. "
                    "Set GITHUB_TOKEN or OPENAI_API_KEY in .env"
                )
            
            self._client = AsyncOpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
            )
            logger.info(f"LLM client initialized with model: {self.model}")
        
        return self._client

    async def analyze_sentiment(self, title: str, body: str = "") -> SentimentResult:
        """
        Analyze sentiment of a post using LLM.
        
        Args:
            title: Post title
            body: Post body/content
            
        Returns:
            SentimentResult with classification
        """
        prompt = SENTIMENT_PROMPT.format(
            title=title,
            body=body[:1000] if body else "(no content)"
        )
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a sentiment analysis expert. Respond with only one word."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10,
                temperature=0.1,
            )
            
            result = response.choices[0].message.content.strip().lower()
            
            # Parse the sentiment
            if "positive" in result:
                sentiment = Sentiment.POSITIVE
            elif "negative" in result:
                sentiment = Sentiment.NEGATIVE
            else:
                sentiment = Sentiment.NEUTRAL
                
            logger.debug(f"Sentiment for '{title[:50]}...': {sentiment.value}")
            return SentimentResult(sentiment=sentiment)
            
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {e}")
            # Default to neutral on error
            return SentimentResult(sentiment=Sentiment.NEUTRAL)

    async def generate_summary(self, title: str, body: str = "", max_words: int = 25) -> str:
        """
        Generate a concise summary of a post.
        
        Args:
            title: Post title
            body: Post body/content
            max_words: Maximum words in summary
            
        Returns:
            One-sentence summary
        """
        prompt = SUMMARY_PROMPT.format(
            title=title,
            body=body[:2000] if body else "(no content)"
        )
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"You are a summarization expert. Keep summaries under {max_words} words."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.3,
            )
            
            summary = response.choices[0].message.content.strip()
            
            # Ensure summary ends with period
            if summary and not summary.endswith(('.', '!', '?')):
                summary += '.'
                
            logger.debug(f"Summary for '{title[:50]}...': {summary[:50]}...")
            return summary
            
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            # Return title as fallback
            return f"{title[:100]}..."

    async def enrich_post(self, post: dict) -> dict:
        """
        Enrich a post with sentiment and summary.
        
        Args:
            post: Raw post data dictionary
            
        Returns:
            Enriched post with sentiment and summary fields
        """
        title = post.get("title", "")
        body = post.get("body", "")
        
        # Run sentiment and summary in parallel
        sentiment_result, summary = await asyncio.gather(
            self.analyze_sentiment(title, body),
            self.generate_summary(title, body),
        )
        
        return {
            **post,
            "sentiment": sentiment_result.sentiment.value,
            "summary": summary,
        }


# Singleton instance for reuse
llm_service = LLMService()
