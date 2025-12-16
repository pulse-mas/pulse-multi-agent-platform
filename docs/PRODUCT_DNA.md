# Product DNA - AI-Enhanced Reddit Data Collection

> Automatically collect and enrich social media posts with AI-powered sentiment analysis and summarization.

## Overview

Product DNA is a data pipeline that:
1. 🔍 **Collects** posts from Reddit based on keywords
2. 🤖 **Analyzes** each post with GPT-4o for sentiment (positive/neutral/negative)
3. 📝 **Summarizes** content into one-sentence insights
4. 💾 **Stores** enriched data in MongoDB for future use

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/product-dna/collect` | Trigger data collection |
| GET | `/api/v1/product-dna/` | Retrieve stored records |
| GET | `/api/v1/product-dna/stats` | Get statistics |

## Quick Start

### 1. Configure Environment

```bash
cd backend
cp .env.template .env
```

Edit `.env` with your credentials:
```env
# Reddit API (https://www.reddit.com/prefs/apps)
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret

# GitHub Token for GPT-4o (https://github.com/settings/tokens)
GITHUB_TOKEN=your_github_token
```

### 2. Start Services

```bash
# Start MongoDB
docker-compose up -d

# Start API server
.\venv\Scripts\activate  # Windows
uvicorn app.main:app --reload
```

### 3. Test the API

Open http://localhost:8000/docs and try:

```json
POST /api/v1/product-dna/collect
{
  "keywords": ["social media marketing"],
  "subreddits": ["marketing", "socialmedia"],
  "limit": 10
}
```

**Response:**
```json
{
  "posts_collected": 10,
  "posts_enriched": 10,
  "posts_stored": 10,
  "sample": [
    {
      "title": "Tips for Instagram growth",
      "sentiment": "positive",
      "summary": "User shares organic growth strategies for small businesses."
    }
  ]
}
```

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Reddit API  │────▶│  LLM (GPT-4) │────▶│   MongoDB    │
│    (PRAW)    │     │  Sentiment   │     │ product_dna  │
│              │     │  + Summary   │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

## File Structure

```
backend/app/
├── integrations/
│   ├── reddit.py      # RedditSearchTool
│   └── llm.py         # LLMService (GPT-4o)
├── services/
│   └── product_dna.py # Orchestration
├── models/
│   └── reddit.py      # Pydantic schemas
├── routers/
│   └── product_dna.py # API endpoints
└── db/
    └── mongodb.py     # Database connection
```

## Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `REDDIT_CLIENT_ID` | Reddit app client ID | ✅ |
| `REDDIT_CLIENT_SECRET` | Reddit app secret | ✅ |
| `GITHUB_TOKEN` | GitHub token for LLM | ✅ |
| `MONGODB_URI` | MongoDB connection | Default: localhost |
| `LLM_MODEL` | Model name | Default: gpt-4o |

## Getting API Credentials

### Reddit API
1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" → Select "script"
3. Copy `client_id` (under app name) and `secret`

### GitHub Token (Free GPT-4o)
1. Go to https://github.com/settings/tokens
2. Generate new token (no special scopes needed)
3. Use token as `GITHUB_TOKEN`

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

## License

MIT License - See [LICENSE](../LICENSE)
