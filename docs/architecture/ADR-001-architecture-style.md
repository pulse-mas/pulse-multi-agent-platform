# ADR 001: Monolithic vs Microservices Architecture

## Status
ACCEPTED

## Context
Pulse requires managing multiple agents, external API integrations, real-time data processing, and a user-facing dashboard. We must decide between a monolithic FastAPI application or microservices architecture.

## Decision Drivers
- **Timeline:** 14-week graduation project (limited time)
- **Team Size:** 4 developers (limited resources)
- **Complexity:** Multi-agent system with 4 specialized agents
- **Scalability:** Must handle moderate traffic (not enterprise-scale)
- **Deployment:** Free/low-cost hosting (Render, Railway, Vercel)

## Options Considered

### Option 1: Monolithic FastAPI Application ✅ CHOSEN
**Pros:**
- Faster development (single codebase, shared utilities)
- Simpler deployment (one container, one process)
- Easier debugging (single log stream, no distributed tracing needed)
- Lower infrastructure costs (one server vs multiple)
- Sufficient for project scale (100-1000 users max)

**Cons:**
- Harder to scale individual components independently
- Agents are tightly coupled in same process
- Single point of failure

### Option 2: Microservices (Agent per Service)
**Pros:**
- Independent scaling of agents
- Better fault isolation
- Technology flexibility per service

**Cons:**
- Significantly higher complexity (service mesh, API gateway)
- Longer development time (inter-service communication, deployment pipelines)
- Higher hosting costs ($15-30/month vs $5-10/month)
- Overkill for graduation project scope

## Decision
**We will use a MODULAR MONOLITHIC architecture:**
```
pulse-backend/
├── src/
│   ├── api/          # FastAPI routers
│   ├── agents/       # Agent modules (modular, loosely coupled)
│   │   ├── strategist/
│   │   ├── analyst/
│   │   ├── content_engine/
│   │   └── support/
│   ├── core/         # Shared utilities
│   ├── db/           # Database access layer
│   └── integrations/ # External API clients
```

This gives us:
- ✅ Speed of monolith development
- ✅ Modularity for future refactoring
- ✅ Clear agent separation within codebase
- ✅ Easy migration to microservices if needed post-graduation

## Consequences
- All agents run in same Python process (acceptable for 4 agents)
- Vertical scaling only (scale entire app, not per-agent)
- Must be disciplined about module boundaries to avoid coupling
