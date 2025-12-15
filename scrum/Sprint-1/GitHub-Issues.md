# 🎫 GitHub Issues for Sprint 1

> **Instructions:** Create each of these as GitHub issues in your repository.
> Use the GitHub CLI or web interface to create issues with the specified labels and assignees.

---

## Issue Creation Commands (GitHub CLI)

You can run these commands after installing [GitHub CLI](https://cli.github.com/):

```bash
# First, create labels if they don't exist
gh label create "sprint:1" --color "0E8A16" --description "Sprint 1 backlog item"
gh label create "priority:P0" --color "B60205" --description "Critical priority"
gh label create "priority:P1" --color "D93F0B" --description "High priority"
gh label create "priority:P2" --color "FBCA04" --description "Medium priority"
gh label create "data-collection" --color "1D76DB" --description "Data collection tools"
gh label create "agent" --color "5319E7" --description "AI agent development"
gh label create "api-integration" --color "0052CC" --description "External API integration"
gh label create "scraping" --color "006B75" --description "Web scraping"
gh label create "nlp" --color "C2E0C6" --description "NLP/NER tasks"
gh label create "infrastructure" --color "BFD4F2" --description "Infrastructure/DevOps"
gh label create "framework" --color "D4C5F9" --description "Framework setup"
gh label create "browser" --color "FEF2C0" --description "Browser automation"

# Create milestone
gh api repos/{owner}/{repo}/milestones -f title="Sprint 1" -f due_on="2025-12-22T23:59:59Z" -f description="Data Collection & AI Agent Framework"
```

---

## Issue 1: DC-001 - Data Collection Agent Setup

```bash
gh issue create \
  --title "[Sprint-1] DC-001: Data Collection Agent Setup" \
  --body "## Description
As a AI developer, I want to create a Data Collection Agent with search capabilities so that our agents can autonomously gather intelligence from the web.

## Story Points: 8
## Assigned To: @abdelrahman-elattar

## Acceptance Criteria
- [ ] Create DataCollectionAgent class extending CrewAI Agent
- [ ] Integrate Tavily/Serper search tool
- [ ] Agent can execute search queries and return structured results
- [ ] Search results stored in MongoDB collection \`collected_data\`
- [ ] Unit tests for agent functionality
- [ ] Documentation with usage examples

## Technical Notes
\`\`\`python
from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool

data_collector = Agent(
    role='Data Collection Specialist',
    goal='Gather relevant market intelligence and user insights',
    tools=[SerperDevTool(), WebsiteSearchTool()],
    memory=True
)
\`\`\`
" \
  --label "sprint:1,priority:P0,agent,data-collection" \
  --milestone "Sprint 1"
```

---

## Issue 2: DC-002 - Reddit API Integration for Product DNA

```bash
gh issue create \
  --title "[Sprint-1] DC-002: Reddit API Integration for Product DNA" \
  --body "## Description
As a marketing analyst, I want to collect discussions from Reddit about our product/industry so that we can understand user voice and pain points.

## Story Points: 8
## Assigned To: @abdelrahman-omar

## Acceptance Criteria
- [ ] Set up PRAW (Python Reddit API Wrapper)
- [ ] Create tool to search subreddits by keywords
- [ ] Extract posts, comments, and metadata
- [ ] Implement rate limiting and caching
- [ ] Store results with sentiment annotation
- [ ] Tool follows CrewAI Tool interface

## Technical Notes
\`\`\`python
import praw
from crewai.tools import BaseTool

class RedditSearchTool(BaseTool):
    name: str = 'Reddit Search'
    description: str = 'Search Reddit for discussions about a topic'
    
    def _run(self, query: str, subreddit: str = 'all', limit: int = 10):
        reddit = praw.Reddit(...)
        results = reddit.subreddit(subreddit).search(query, limit=limit)
        return [{'title': p.title, 'text': p.selftext, 'score': p.score} for p in results]
\`\`\`
" \
  --label "sprint:1,priority:P0,data-collection,api-integration" \
  --milestone "Sprint 1"
```

---

## Issue 3: DC-003 - Competitor Web Scraper Tool

```bash
gh issue create \
  --title "[Sprint-1] DC-003: Competitor Web Scraper Tool" \
  --body "## Description
As a business analyst, I want to scrape competitor websites for content and messaging so that we can build Business DNA from market intelligence.

## Story Points: 10
## Assigned To: @rana-mahmoud

## Acceptance Criteria
- [ ] Create WebScraperTool compatible with CrewAI
- [ ] Extract text content, headings, meta descriptions
- [ ] Handle pagination and navigation
- [ ] Respect robots.txt and rate limits
- [ ] Return structured content with source URL
- [ ] Error handling for blocked/unavailable sites

## Technical Notes
\`\`\`python
from crewai.tools import BaseTool
import requests
from bs4 import BeautifulSoup

class CompetitorScraperTool(BaseTool):
    name: str = 'Competitor Scraper'
    description: str = 'Scrape content from competitor websites'
    
    def _run(self, url: str):
        resp = requests.get(url, headers={'User-Agent': '...'})
        soup = BeautifulSoup(resp.text, 'html.parser')
        return {
            'title': soup.title.string,
            'headings': [h.text for h in soup.find_all(['h1', 'h2'])],
            'content': soup.get_text()[:5000]
        }
\`\`\`
" \
  --label "sprint:1,priority:P0,data-collection,scraping" \
  --milestone "Sprint 1"
```

---

## Issue 4: DC-004 - X/Twitter Search Integration

```bash
gh issue create \
  --title "[Sprint-1] DC-004: X/Twitter Search Integration" \
  --body "## Description
As a social media analyst, I want to collect tweets about our brand and industry so that we capture real-time social sentiment.

## Story Points: 5
## Assigned To: @abdelrahman-omar

## Acceptance Criteria
- [ ] Set up Twitter API v2 access
- [ ] Create TwitterSearchTool for CrewAI
- [ ] Search by hashtags, keywords, mentions
- [ ] Extract tweets with engagement metrics
- [ ] Handle API rate limits gracefully

## Notes
- X/Twitter API has costs - consider using free tier or Nitter as fallback
- May be lower priority if Reddit provides sufficient data
" \
  --label "sprint:1,priority:P1,data-collection,api-integration" \
  --milestone "Sprint 1"
```

---

## Issue 5: US-001 - AI Agent Framework Setup

```bash
gh issue create \
  --title "[Sprint-1] US-001: AI Agent Framework Setup" \
  --body "## Description
As a AI developer, I want to establish the CrewAI agent orchestration framework so that multiple AI agents can collaborate on marketing tasks.

## Story Points: 8
## Assigned To: @abdelrahman-elattar

## Acceptance Criteria
- [ ] CrewAI library configured in backend
- [ ] Agent base class with role, goal, backstory, tools, memory
- [ ] Task orchestration with sequential/parallel execution
- [ ] Inter-agent communication protocol (JSON)
- [ ] Agent memory integrated with MongoDB
- [ ] 5+ unit tests for agent creation/execution
- [ ] POC: 2 agents collaborate on sample task

## Dependencies
- DC-001 (Data Collection tools needed)
" \
  --label "sprint:1,priority:P1,agent,framework" \
  --milestone "Sprint 1"
```

---

## Issue 6: DC-005 - Data Storage Pipeline

```bash
gh issue create \
  --title "[Sprint-1] DC-005: Data Storage Pipeline" \
  --body "## Description
As a data engineer, I want to store all collected data in a structured format so that AI agents can query and use this intelligence.

## Story Points: 3
## Assigned To: @hager-saad

## Acceptance Criteria
- [ ] MongoDB schema for \`collected_data\` collection
- [ ] Fields: source, type, content, sentiment, timestamp, metadata
- [ ] Indexing for efficient queries
- [ ] Data validation and cleaning pipeline
- [ ] TTL policy for data expiration (30 days default)

## Schema Example
\`\`\`json
{
  \"source\": \"reddit\",
  \"type\": \"product_dna\",
  \"content\": \"...\",
  \"sentiment\": 0.75,
  \"entities\": [\"brand_x\", \"feature_y\"],
  \"metadata\": {
    \"subreddit\": \"tech\",
    \"score\": 145
  },
  \"created_at\": \"2025-12-10T10:00:00Z\",
  \"expires_at\": \"2026-01-10T10:00:00Z\"
}
\`\`\`
" \
  --label "sprint:1,priority:P1,infrastructure" \
  --milestone "Sprint 1"
```

---

## Issue 7: DC-006 - Browser Automation Tool

```bash
gh issue create \
  --title "[Sprint-1] DC-006: Browser Automation Tool" \
  --body "## Description
As a data collector, I want to scrape JavaScript-heavy websites so that we can collect data from modern web apps.

## Story Points: 5
## Assigned To: @hager-saad

## Acceptance Criteria
- [ ] Set up Playwright for browser automation
- [ ] Create BrowserScraperTool for CrewAI
- [ ] Handle dynamic content loading
- [ ] Screenshot capability for visual content
- [ ] Session management for authenticated scraping

## Notes
This is P2 priority - implement after core tools are complete
" \
  --label "sprint:1,priority:P2,data-collection,browser" \
  --milestone "Sprint 1"
```

---

## Issue 8: DC-007 - NER for Entity Extraction

```bash
gh issue create \
  --title "[Sprint-1] DC-007: NER for Entity Extraction" \
  --body "## Description
As a NLP engineer, I want to extract entities from collected data so that we can identify brands, products, and key topics.

## Story Points: 3
## Assigned To: @hager-saad

## Acceptance Criteria
- [ ] Integrate spaCy NER pipeline
- [ ] Custom entity types: BRAND, PRODUCT, FEATURE, COMPETITOR
- [ ] Process all collected data through NER
- [ ] Store extracted entities with source reference
- [ ] Entity frequency analysis

## Notes
This is P2 priority - can use default spaCy entities for MVP
" \
  --label "sprint:1,priority:P2,nlp,data-processing" \
  --milestone "Sprint 1"
```

---

## 📊 Summary

| Issue ID | Title | Points | Priority | Assignee |
|----------|-------|--------|----------|----------|
| DC-001 | Data Collection Agent Setup | 8 | P0 | Abdelrahman Elattar |
| DC-002 | Reddit API Integration | 8 | P0 | Abdelrahman Omar |
| DC-003 | Competitor Web Scraper | 10 | P0 | Rana Mahmoud |
| DC-004 | X/Twitter Integration | 5 | P1 | Abdelrahman Omar |
| US-001 | AI Agent Framework | 8 | P1 | Abdelrahman Elattar |
| DC-005 | Data Storage Pipeline | 3 | P1 | Hager Saad |
| DC-006 | Browser Automation | 5 | P2 | Hager Saad |
| DC-007 | NER Entity Extraction | 3 | P2 | Hager Saad |
| **Total** | | **50** | | |

---

## 🏷️ Label Color Reference

| Label | Color | Hex |
|-------|-------|-----|
| sprint:1 | Green | #0E8A16 |
| priority:P0 | Red | #B60205 |
| priority:P1 | Orange | #D93F0B |
| priority:P2 | Yellow | #FBCA04 |
| data-collection | Blue | #1D76DB |
| agent | Purple | #5319E7 |
| api-integration | Dark Blue | #0052CC |
| scraping | Teal | #006B75 |
| nlp | Light Green | #C2E0C6 |
| infrastructure | Light Blue | #BFD4F2 |
