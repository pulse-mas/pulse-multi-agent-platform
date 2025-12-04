graph TD
    subgraph Users["👤 Users"]
        MktDir[Marketing Director]
        SocialMgr[Social Media Manager]
        Support[Customer Support]
    end

    subgraph Dashboard["🖥️ React Dashboard"]
        CampaignUI[Campaign Planner]
        SchedulerUI[Content Scheduler]
        InboxUI[Message Inbox]
        AnalyticsUI[Analytics Dashboard]
        ReviewUI[Approval Queue]
    end

    subgraph Agents["🤖 AI Agents - CrewAI"]
        Strategist[Marketing Strategist Agent]
        Analyst[Social Media Analyst Agent]
        CRM[Customer Relationship Agent]
        ContentEngine[Content Engine Agent]
    end

    subgraph Backend["⚙️ FastAPI Backend"]
        API[REST API Gateway]
        RAG[RAG Pipeline]
        Scheduler[Job Scheduler]
        Validator[Hallucination Detector]
        RateLimiter[Rate Limiter]
    end

    subgraph AI_Services["🧠 AI Services"]
        LLM[OpenAI / Anthropic LLM]
        Sentiment[Sentiment Model]
        BrandDNA[Brand DNA Analyzer]
        Anomaly[Anomaly Detector]
    end

    subgraph Data["🗄️ Data Layer"]
        MongoDB[(MongoDB)]
        VectorDB[(Vector DB - Pinecone)]
        Redis[(Redis Cache)]
    end

    subgraph External["🌐 External APIs"]
        Meta[Meta API]
        LinkedIn[LinkedIn API]
        XApi[X API]
        TrendAPI[Trend APIs]
    end

    %% User interactions
    MktDir --> CampaignUI
    SocialMgr --> SchedulerUI
    Support --> InboxUI

    %% Dashboard to Backend
    CampaignUI --> API
    SchedulerUI --> API
    InboxUI --> API
    AnalyticsUI --> API
    ReviewUI --> API

    %% Backend to Agents
    API --> Strategist
    API --> Analyst
    API --> CRM
    API --> ContentEngine

    %% Agent collaboration
    Strategist -->|delegates| ContentEngine
    Analyst -->|insights| Strategist
    CRM -->|feedback| ContentEngine

    %% Backend services
    API --> RAG
    API --> Validator
    Scheduler --> RateLimiter

    %% AI Services connections
    Strategist --> LLM
    ContentEngine --> LLM
    CRM --> LLM
    Analyst --> Sentiment
    ContentEngine --> BrandDNA
    Analyst --> Anomaly

    %% Data layer
    RAG --> VectorDB
    API --> MongoDB
    RateLimiter --> Redis
    Validator --> VectorDB

    %% External APIs
    RateLimiter --> Meta
    RateLimiter --> LinkedIn
    RateLimiter --> XApi
    Analyst --> TrendAPI

    %% Styling
    classDef agentClass fill:#6366f1,stroke:#4f46e5,color:#fff
    classDef serviceClass fill:#10b981,stroke:#059669,color:#fff
    classDef dataClass fill:#f59e0b,stroke:#d97706,color:#fff
    classDef externalClass fill:#64748b,stroke:#475569,color:#fff

    class Strategist,Analyst,CRM,ContentEngine agentClass
    class LLM,Sentiment,BrandDNA,Anomaly serviceClass
    class MongoDB,VectorDB,Redis dataClass
    class Meta,LinkedIn,XApi,TrendAPI externalClass
