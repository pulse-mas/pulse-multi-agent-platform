# 1.0 Browser Automation & NER Extraction
**Assignee:** Hager Saad
**Epic:** Data Collection / Sprint 1
**Sprint:** Sprint 1 (Dec 9‑22, 2025)
**Estimate:** 18 hours

## Description
Implement browser‑automation tools for JS‑heavy competitor sites and NER extraction for brand‑specific entities. This supports both **Product DNA** and **Business DNA** pipelines.

### Tasks
1. **Browser Automation Engine**
   - Use Playwright to launch headless Chromium.
   - Navigate to URLs, wait for dynamic content, capture HTML.
2. **NER Model Integration**
   - Load a spaCy NER model (or HuggingFace transformer) to extract brand‑related entities (products, features, sentiment).
   - Store entities with source URL and context.
3. **Data Storage**
   - Persist extracted entities in MongoDB `entity_extractions` collection.
4. **Testing & Docs**
   - Unit tests with mocked browser sessions.
   - Documentation with sample scripts.

### Acceptance Criteria
- [ ] Playwright script can fetch and render a competitor page.
- [ ] NER extracts at least 5 entity types per page.
- [ ] Results stored in `entity_extractions`.
- [ ] Tests pass (>80% coverage).

### Definition of Done
- Code reviewed and merged.
- Docs updated.
- Demonstrated extraction in sprint demo.
