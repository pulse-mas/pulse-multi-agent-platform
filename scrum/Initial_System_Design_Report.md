# Initial System Design & Work Division Report

---

**Project Title:** Pulse: AI-Powered Multi-Agent Social Media Platform

**Team #:** 44

**Team Members:**
- Abdelrahman Elattar (Product Owner + Multi-Agent Systems Lead)
- Abdelrahman Omar (Product Owner + RAG & NLP Lead)
- Rana Mahmoud (Scrum Master + ML Analytics Lead)
- Hager Saad (Scrum Master + Content Generation & NER Lead)

**Supervisor:** Dr. Mohamed Maher

**Course:** CSAI 498 / CSAI 499 | Fall 2025 / Spring 2026

**Institution:** Zewail City of Science and Technology

**Date:** December 13, 2025

---

## Table of Contents

1. [Project Summary](#1-project-summary)
2. [Progress Since Proposal](#2-progress-since-proposal)
3. [System Architecture](#3-system-architecture)
4. [Component Breakdown](#4-component-breakdown)
5. [Data Flow](#5-data-flow)
6. [Work Breakdown Structure](#6-work-breakdown-structure)
7. [Risk Analysis](#7-risk-analysis)
8. [References](#references)

---

## 1. Project Summary

### 1.1 Objective

Pulse is an autonomous AI-powered platform that revolutionizes social media management through intelligent multi-agent orchestration. The system delivers automated content creation, real-time customer engagement, and actionable performance insights, enabling businesses to transform labor-intensive social media execution into high-level strategic orchestration.

### 1.2 Scope

**Target Users:** Marketing teams, small-to-medium businesses, social media managers, and digital marketing agencies.

**Core Capabilities:**
- AI-powered content generation and intelligent scheduling
- Real-time sentiment analysis and audience engagement tracking
- Multi-platform integration (Facebook, Instagram, LinkedIn, X/Twitter)
- Autonomous customer response with brand voice consistency
- Human-in-the-loop approval workflows for quality control
- Predictive analytics and anomaly detection

**Project Timeline:** November 2025 – May 2026 (2 semesters)

**Stakeholder Alignment:** The platform addresses critical pain points identified through stakeholder analysis: managing simultaneous multi-platform presence, maintaining brand consistency, and scaling customer engagement without proportional staffing increases.

---

## 2. Progress Since Proposal

### 2.1 Completed Tasks (Week 4 to Present)

| Task | Evidence | Status |
|------|----------|--------|
| Sprint 0 Planning Documentation | `main.md` - 57KB comprehensive planning document | ✅ Complete |
| User Story Creation | 15+ detailed user stories with acceptance criteria | ✅ Complete |
| Work Breakdown Structure | `wbs-detailed.md` - 127 work packages, 136 story points | ✅ Complete |
| System Architecture Design | Architecture diagrams and technical specifications | ✅ Complete |
| GitHub Repository Setup | https://github.com/el3ttar3/Social-Media-and-Marketing-Multi-Agents-Platform | ✅ Complete |
| GitHub Projects Board | Configured with swim lanes, labels, story point scale | ✅ Complete |
| Technology Stack Research | Evaluated CrewAI, LangChain, vector databases | ✅ Complete |

### 2.2 Proof of Concept Development

Each team member completed individual POCs to validate technical feasibility:

1. **CrewAI Multi-Agent POC** (Abdelrahman Elattar): Demonstrated 2 agents collaborating on marketing task delegation with inter-agent communication protocols.

2. **RAG Pipeline POC** (Abdelrahman Omar): Implemented document upload, text chunking, embedding generation with OpenAI Ada-002, and semantic retrieval using vector database.

3. **Sentiment Analysis POC** (Rana Mahmoud): Integrated DistilBERT model for real-time sentiment classification with React dashboard visualization.

4. **NER & Content Generation POC** (Hager Saad): Deployed spaCy NER model for brand entity extraction and GPT-4 integration for brand-aligned content generation.

### 2.3 Repository Structure

```
pulse-platform/
├── backend/           # FastAPI application
│   ├── agents/        # CrewAI agent definitions
│   ├── services/      # NLP, analytics, content services
│   └── integrations/  # Social media API clients
├── frontend/          # React dashboard
├── docs/              # Architecture documentation
├── tests/             # Unit and integration tests
└── .github/workflows/ # CI/CD pipelines
```

**Version Control:** 50+ commits, active development across 4 contributors.

---

## 3. System Architecture

### 3.1 High-Level Architecture Diagram

![Fig. 1: System Architecture Overview](C:/Users/Abdu%20Omar/.gemini/antigravity/brain/d08391a3-00e2-4473-8a64-8204324115f1/system_overview.png)

*Fig. 1: Pulse Platform System Architecture showing AI agents, processing layers, and external integrations.*

### 3.2 Architecture Layers

**Presentation Layer:**
- React 18+ frontend with Recharts visualization
- Real-time WebSocket updates for live analytics
- Responsive dashboard with shadcn/ui components

**Agent Orchestration Layer:**
- CrewAI framework for multi-agent coordination
- Hierarchical agent collaboration with task delegation
- Agent memory system using MongoDB for context persistence

**AI/ML Processing Layer:**
- NLP Engine: spaCy, Hugging Face Transformers
- Content Generation: GPT-4/Claude integration via LangChain
- Analytics Engine: Sentiment classification, anomaly detection

**Data Layer:**
- MongoDB for flexible document storage
- Pinecone/Qdrant for vector embeddings
- Redis for caching and rate limiting

**Integration Layer:**
- Meta Graph API (Facebook, Instagram)
- LinkedIn Marketing API
- X API v2
- Google Analytics 4 Data API

### 3.3 Technology Justification

| Technology | Justification |
|------------|---------------|
| CrewAI | Purpose-built for multi-agent orchestration with native memory and tool support |
| FastAPI | Async Python framework with OpenAPI spec generation, ideal for AI workloads |
| MongoDB | Flexible schema accommodates varied social media data structures |
| Pinecone | Managed vector database reduces operational complexity for RAG |
| React | Component-based architecture with rich visualization ecosystem |

---

## 4. Component Breakdown

### 4.1 AI Marketing Strategist Agent

**Function:** Strategic planning, campaign goal decomposition, brand consistency oversight

**Inputs:** Campaign objectives, target KPIs, budget constraints, brand knowledge context

**Outputs:** Execution plans with content themes, platform distribution, posting frequency recommendations

**Core Functionality:**
- Receives high-level marketing goals from users
- Queries brand knowledge base for context alignment
- Generates actionable campaign strategies
- Delegates tasks to specialized agents

**Technologies:** CrewAI, GPT-4, LangChain chains, custom prompt templates

---

### 4.2 Social Media & Performance Analyst Agent

**Function:** Content scheduling optimization, real-time analytics aggregation, engagement prediction

**Inputs:** Historical engagement data, platform performance metrics, scheduled content queue

**Outputs:** Optimal posting times, sentiment reports, trend analysis, anomaly alerts

**Core Functionality:**
- Analyzes time-series engagement patterns
- Implements ML-based optimal time prediction
- Aggregates cross-platform analytics
- Detects engagement anomalies using Z-score algorithms

**Technologies:** Transformers (DistilBERT), scikit-learn, Recharts, Celery job scheduler

---

### 4.3 Customer Relationship Agent

**Function:** Message prioritization, AI-powered response generation with brand voice matching

**Inputs:** Customer messages from all platforms, conversation history, brand tone profile

**Outputs:** Urgency scores, suggested responses, escalation flags

**Core Functionality:**
- Aggregates messages from Instagram DMs, Facebook Messenger, LinkedIn
- Classifies urgency using keyword + sentiment analysis
- Generates contextual responses maintaining brand voice
- Routes low-confidence responses to human review

**Technologies:** spaCy NER, GPT-4, custom urgency classification model

---

### 4.4 Content & Market Authority Engine

**Function:** Trend-based content generation, SEO optimization, brand voice validation

**Inputs:** Trending topics, brand DNA profile, industry keywords

**Outputs:** Platform-optimized posts, hashtag recommendations, content validation scores

**Core Functionality:**
- Discovers trends via NewsAPI, Reddit, GDELT
- Generates multi-platform content variants
- Validates against hallucination detection pipeline
- Ensures brand consistency scoring >75%

**Technologies:** GPT-4, TF-IDF trend analysis, spaCy NER, custom brand scorer

---

### 4.5 RAG Knowledge Base System

**Function:** Brand document ingestion, semantic search, context retrieval for agents

**Inputs:** PDF, DOCX, TXT brand documents, user queries

**Outputs:** Relevant document chunks with similarity scores, contextual answers

**Core Functionality:**
- Document parsing and text extraction
- Semantic chunking (500 tokens, 50-token overlap)
- Embedding generation with OpenAI text-embedding-3-small
- Vector similarity search with reranking

**Technologies:** LangChain, PyPDF2, Pinecone, OpenAI Embeddings API

---

### 4.6 Hallucination Detection System

**Function:** Automated validation of AI-generated content against verified knowledge base

**Inputs:** AI-generated text, brand knowledge base, product catalog

**Outputs:** Validity scores, flagged claims, specific rejection reasons

**Core Functionality:**
- Extracts factual claims using NER
- Verifies claims against knowledge base
- Scores brand consistency (threshold: 75%)
- Flags unverified claims for human review

**Technologies:** spaCy NER, custom claim extraction, KB verification engine

---

## 5. Data Flow

### 5.1 Data Flow Diagram

![Fig. 2: Data Pipeline Architecture](C:/Users/Abdu%20Omar/.gemini/antigravity/brain/d08391a3-00e2-4473-8a64-8204324115f1/data_pipeline.png)

*Fig. 2: Data flow through Pulse platform showing transformation stages and module interactions.*

### 5.2 Data Transformation Pipeline

**Stage 1: Document Ingestion**
```
Brand Documents → Text Extraction → Semantic Chunking → 
Ada-002 Embeddings → Pinecone Vector Storage
```
- PDF/DOCX files parsed using PyPDF2/python-docx
- Text chunked at 500 tokens with 50-token overlap
- Embeddings generated via OpenAI API
- Stored in Pinecone with metadata (brand_id, source, timestamp)

**Stage 2: Content Generation Flow**
```
User Campaign Goal → Marketing Agent → RAG Context Retrieval → 
Content Engine (GPT-4) → Hallucination Validation → 
Confidence Routing → Publish/Review Queue
```
- Campaign goals trigger agent orchestration
- RAG provides brand context to LLM prompts
- Generated content validated against KB
- High confidence (>90%) auto-publishes; medium (70-90%) routes to human review

**Stage 3: Analytics Pipeline**
```
Platform APIs → Data Ingestion (60s intervals) → 
Sentiment Classification → Time-Series Aggregation → 
Anomaly Detection → Dashboard Visualization
```
- Social media APIs polled for comments, messages, metrics
- DistilBERT classifies sentiment in real-time
- Z-score algorithm detects engagement anomalies
- Recharts renders live dashboard updates

### 5.3 Data Storage Schema

| Collection | Purpose | Key Fields |
|------------|---------|------------|
| `brands` | Brand profiles and DNA | brand_id, colors, tone, vocabulary |
| `posts` | Scheduled/published content | post_id, platform, status, scheduled_time |
| `analytics` | Performance metrics | impressions, engagement, sentiment_score |
| `interactions` | Customer messages | sender, platform, urgency, sentiment |
| `agent_memory` | Agent context history | agent_id, task_id, memory_type |
| `campaigns` | Marketing campaigns | goal_type, target_kpis, status |

---

## 6. Work Breakdown Structure

### 6.1 Project Phase Overview

| Phase | Timeline | Story Points | Description |
|-------|----------|--------------|-------------|
| Sprint 0 | Nov 28 - Dec 5 | - | Planning & Foundation |
| Sprint 1 | Dec 6 - Dec 19 | 42 | Core AI Framework + RAG |
| Sprint 2 | Dec 20 - Jan 2 | 47 | Analytics & Scheduling |
| Sprint 3 | Jan 3 - Jan 16 | 47 | Autonomous Content Engine |

### 6.2 Detailed Work Breakdown

| WBS | Task | Responsible | Start | End | Status |
|-----|------|-------------|-------|-----|--------|
| 1.1 | Sprint 0: Planning & Foundation | All Team | Nov 28 | Dec 5 | ✅ Complete |
| 1.1.1 | Requirements Engineering | Abdelrahman E. + O. | Nov 28 | Dec 1 | ✅ Complete |
| 1.1.2 | System Architecture Design | All Team | Nov 29 | Dec 3 | ✅ Complete |
| 1.1.3 | Proof of Concept Development | All Team | Nov 30 | Dec 5 | ✅ Complete |
| 1.1.4 | GitHub Projects Setup | Rana + Hager | Nov 28 | Dec 2 | ✅ Complete |
| 1.2 | Sprint 1: Core AI Framework | All Team | Dec 6 | Dec 19 | 🟡 In Progress |
| 1.2.1 | US-001: Multi-Agent Framework (8 pts) | Abdelrahman E. | Dec 6 | Dec 12 | 🟡 In Progress |
| 1.2.2 | US-002: Brand Knowledge RAG (13 pts) | Abdelrahman O. | Dec 6 | Dec 15 | 🟡 In Progress |
| 1.2.3 | US-003: Campaign Planner (5 pts) | Abdelrahman E. + Rana | Dec 10 | Dec 16 | ⬜ Planned |
| 1.2.4 | US-010: Brand DNA Extraction (8 pts) | Abdelrahman O. + Rana | Dec 8 | Dec 14 | ⬜ Planned |
| 1.2.5 | US-014: CI/CD Pipeline (8 pts) | Hager S. | Dec 6 | Dec 12 | 🟡 In Progress |
| 1.3 | Sprint 2: Analytics & Scheduling | All Team | Dec 20 | Jan 2 | ⬜ Backlog |
| 1.3.1 | US-004: Content Scheduler (13 pts) | Abdelrahman O. + Rana | Dec 20 | Dec 28 | ⬜ Backlog |
| 1.3.2 | US-005: Sentiment Dashboard (8 pts) | Rana (Lead) | Dec 20 | Dec 26 | ⬜ Backlog |
| 1.3.3 | US-007: Unified Message Inbox (8 pts) | Abdelrahman O. + Hager | Dec 22 | Dec 28 | ⬜ Backlog |
| 1.3.4 | US-011: Hallucination Detection (13 pts) | Hager (Lead) | Dec 20 | Dec 30 | ⬜ Backlog |
| 1.3.5 | US-015: API Rate Limiter (5 pts) | All Team | Dec 26 | Jan 2 | ⬜ Backlog |
| 1.4 | Sprint 3: Autonomous Content | All Team | Jan 3 | Jan 16 | ⬜ Backlog |
| 1.4.1 | US-006: Anomaly Detection (8 pts) | Rana (Lead) | Jan 3 | Jan 8 | ⬜ Backlog |
| 1.4.2 | US-008: AI Response Generator (13 pts) | Abdelrahman E. + Hager | Jan 3 | Jan 10 | ⬜ Backlog |
| 1.4.3 | US-009: Trend-Based Content (13 pts) | Hager (Lead) | Jan 5 | Jan 12 | ⬜ Backlog |
| 1.4.4 | US-012: Human-in-the-Loop (8 pts) | Abdelrahman O. + Rana | Jan 8 | Jan 14 | ⬜ Backlog |
| 1.4.5 | US-013: Model Monitoring (5 pts) | All Team | Jan 10 | Jan 16 | ⬜ Backlog |

### 6.3 Summary Statistics

| Metric | Value |
|--------|-------|
| Total Work Packages | 127 |
| Total User Stories | 15 |
| Total Story Points | 136 |
| Estimated Hours | 480h |
| Team Capacity | 560h (4 × 20h/week × 7 weeks) |
| Buffer | 80h (17%) |

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk ID | Category | Risk Description | Likelihood | Impact | Mitigation Strategy | Owner |
|---------|----------|------------------|------------|--------|---------------------|-------|
| R1 | Technical | Team unfamiliar with CrewAI framework | High | Medium | Allocate learning time, complete tutorials, create shared knowledge documentation, pair programming | Abdelrahman E. |
| R2 | Resource | OpenAI API costs exceed budget | Medium | High | Use GPT-3.5-turbo for prototyping, implement aggressive response caching, monitor daily costs | Hager S. |
| R3 | Technical | Social media API rate limits | Medium | Low | Use test accounts for development, implement rate limiter early (US-015), cache API responses | Abdelrahman O. |
| R4 | Technical | Vector database learning curve | Medium | Medium | Use Pinecone (managed service) over self-hosted alternatives, follow official tutorials, pair programming sessions | Abdelrahman O. |
| R5 | Timeline | Story point estimation inaccuracy | High | Medium | Include 20% buffer in sprint planning, refine estimates after Sprint 1 completion, track actual vs. estimated hours | Rana M. |
| R6 | Technical | Model hallucination in production | Low | High | Implement validation pipeline (US-011) as P0 priority, enforce human review for low-confidence outputs, maintain test dataset | Hager S. |
| R7 | Security | API key security breach | Low | Critical | Store keys in .env files (never commit), rotate keys monthly, enable GitHub secret scanning, use environment variables in CI/CD | Hager S. |

### 7.2 Mitigation Monitoring

**Daily Monitoring:**
- API cost dashboard review
- Rate limit usage tracking

**Weekly Monitoring:**
- Risk log review and status updates
- Sprint velocity tracking vs. estimates

**Sprint Retrospective:**
- Identify new risks
- Close resolved risks
- Update mitigation effectiveness

---

## References

[1] CrewAI Documentation. (2024). Available: https://docs.crewai.com

[2] LangChain Documentation. (2024). Available: https://docs.langchain.com

[3] OpenAI API Documentation. (2024). Available: https://platform.openai.com/docs

[4] Meta Graph API Documentation. (2024). Available: https://developers.facebook.com/docs/graph-api

[5] Pinecone Vector Database Documentation. (2024). Available: https://docs.pinecone.io

---

**GitHub Repository:** https://github.com/el3ttar3/Social-Media-and-Marketing-Multi-Agents-Platform

---

*Document Version: 1.0 | Last Updated: December 13, 2025*
