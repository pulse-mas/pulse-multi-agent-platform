# Pulse API Specifications v1

## Base URL
```
Development: http://localhost:8000/api/v1
Production: https://api.pulse-platform.com/api/v1
```

## Authentication
All protected endpoints require JWT token in header:
```
Authorization: Bearer <token>
```

## Core Endpoints

### Authentication
```
POST   /auth/register      - Create new user account
POST   /auth/login         - Authenticate and get JWT
POST   /auth/refresh       - Refresh JWT token
POST   /auth/logout        - Invalidate token
```

### Brand Management
```
POST   /brands             - Create brand profile
GET    /brands             - List all brands (paginated)
GET    /brands/{id}        - Get brand details
PUT    /brands/{id}        - Update brand profile
DELETE /brands/{id}        - Delete brand
POST   /brands/{id}/dna/extract  - Trigger DNA extraction
GET    /brands/{id}/dna    - Retrieve Brand DNA profile
```

### Content Management
```
POST   /posts              - Create/schedule post
GET    /posts              - List posts (with filters)
GET    /posts/{id}         - Get post details
PUT    /posts/{id}         - Update post
DELETE /posts/{id}         - Delete post
POST   /posts/{id}/publish - Manually publish post
GET    /posts/calendar     - Get content calendar view
```

### Analytics
```
GET    /analytics/overview          - Dashboard overview stats
GET    /analytics/trends            - Engagement trends (time-series)
GET    /analytics/platforms         - Cross-platform comparison
GET    /analytics/posts/top         - Top performing posts
POST   /analytics/refresh           - Trigger data refresh
GET    /analytics/forecasts         - Predictive analytics
```

### Customer Interactions
```
GET    /interactions               - List customer interactions
GET    /interactions/{id}          - Get interaction thread
POST   /interactions/{id}/respond  - Agent response
PUT    /interactions/{id}/escalate - Escalate to human
GET    /interactions/queue         - Unresolved interactions
```

### Agent Control
```
GET    /agents                     - List all agents + status
GET    /agents/{agent_id}/status   - Get agent health
POST   /agents/{agent_id}/task     - Assign task to agent
GET    /agents/{agent_id}/memory   - Get agent decision log
POST   /agents/orchestrate         - Trigger multi-agent workflow
```

### Integrations
```
POST   /integrations/social/{platform}/connect  - OAuth connect
GET    /integrations/social/{platform}/status   - Connection health
POST   /integrations/social/{platform}/test     - Test API access
DELETE /integrations/social/{platform}          - Disconnect
```
