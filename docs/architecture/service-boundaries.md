# Service Boundaries & Module Responsibilities

## Core Modules

### 1. API Layer (`src/api/`)
**Responsibility:** HTTP endpoints, request validation, response formatting

**Sub-modules:**
- `auth.py` - Authentication endpoints
- `brands.py` - Brand CRUD operations
- `posts.py` - Content management
- `analytics.py` - Performance data endpoints
- `interactions.py` - Customer support
- `agents.py` - Agent status & control

### 2. Agent Layer (`src/agents/`)
**Responsibility:** AI agent logic, decision-making, task execution

**Sub-modules:**
- `strategist/` - Marketing Strategist Agent
  - Goal setting
  - KPI monitoring
  - Agent coordination
  
- `analyst/` - Performance Analyst Agent
  - Data analysis
  - Pattern detection
  - Optimization recommendations
  
- `content_engine/` - Content Engine Agent
  - Brand DNA extraction
  - Content generation
  - Scheduling
  
- `support/` - Customer Support Agent
  - Intent classification
  - Response generation
  - Escalation logic

### 3. Integration Layer (`src/integrations/`)
**Responsibility:** External API communication

**Sub-modules:**
- `social_media/`
  - `meta.py`
  - `linkedin.py`
  - `twitter.py`
- `analytics/`
  - `ga4.py`
- `data_sources/`
  - `gdelt.py`
  - `news_api.py`
  - `reddit.py`

### 4. Data Layer (`src/db/`)
**Responsibility:** Database operations, data models

**Sub-modules:**
- `models.py` - Pydantic models
- `repositories.py` - Data access patterns
- `migrations.py` - Schema changes

### 5. Core Layer (`src/core/`)
**Responsibility:** Shared utilities

**Sub-modules:**
- `config.py` - Environment configuration
- `logging.py` - Structured logging
- `cache.py` - Redis caching
- `security.py` - Auth utilities
