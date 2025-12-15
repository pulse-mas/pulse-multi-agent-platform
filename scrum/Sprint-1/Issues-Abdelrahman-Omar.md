# 1.0 AI‑Enhanced Reddit Data Collection
**Assignee:** Abdelrahman Omar
**Epic:** AI Data Collection / Sprint 1
**Sprint:** Sprint 1 (Dec 9‑22, 2025)
**Estimate:** 20 hours

## Description
Create an AI‑augmented Reddit data‑collection pipeline that not only fetches posts but also leverages LLM‑based sentiment analysis and summarization to produce high‑quality **Product DNA**.

### Tasks
1. **Reddit API Integration**
   - Configure PRAW with credentials from `.env`.
   - Build `RedditSearchTool` class.
2. **AI‑Powered Extraction & Enrichment**
   - Retrieve top‑N posts for given keywords.
   - Use an LLM (e.g., OpenAI `gpt‑4o‑mini`) to generate sentiment scores and concise summaries for each post.
   - Store raw post data plus LLM‑generated metadata.
3. **Storage**
   - Persist enriched records in MongoDB `product_dna` collection with fields: `title`, `body`, `sentiment`, `summary`, `metadata`.
4. **Testing & Documentation**
   - Unit tests with mocked Reddit responses and LLM calls.
   - Documentation with usage examples and prompt templates.

### Acceptance Criteria
- [ ] At least 10 relevant Reddit posts are returned per query.
- [ ] Each post includes an LLM‑generated sentiment label (positive/neutral/negative) and a one‑sentence summary.
- [ ] Data is stored in `product_dna` collection.
- [ ] All tests pass with >80 % coverage.

### Definition of Done
- Code merged after peer review.
- Docs updated in `docs/`.
- Live demo of AI‑enhanced Reddit extraction presented in Sprint Review.
