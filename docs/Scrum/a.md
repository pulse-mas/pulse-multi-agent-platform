graph TD
    %% Level 1 - Project Root
    Project["🚀 Pulse Multi-Agent Platform"]

    %% Level 2 - Major Phases
    Project --> Sprint0
    Project --> Sprint1
    Project --> Sprint2
    Project --> Sprint3
    Project --> CrossCutting
    Project --> AIML
    Project --> CICD
    Project --> Docs

    subgraph Sprint0["📋 Sprint 0: Planning<br/>Nov 28 - Dec 5"]
        S0_Stories["User Stories<br/>Writing & Refinement"]
        S0_Arch["Architecture<br/>Design"]
        S0_POC["Proof of<br/>Concepts"]
        S0_Env["Environment<br/>Setup"]
        S0_Board["GitHub Projects<br/>Configuration"]

        %% Level 4 - Sprint 0 Work Packages
        S0_Stories --> S0_US_Write["Write 15+ Stories"]
        S0_Stories --> S0_US_Est["Story Estimation"]
        S0_Stories --> S0_US_Priority["MoSCoW Prioritization"]

        S0_Arch --> S0_Arch_Agent["Agent Architecture"]
        S0_Arch --> S0_Arch_DB["Database Schema"]
        S0_Arch --> S0_Arch_API["API Specifications"]

        S0_POC --> S0_POC_Crew["CrewAI POC<br/>👤 Elattar"]
        S0_POC --> S0_POC_RAG["RAG POC<br/>👤 Omar"]
        S0_POC --> S0_POC_Sent["Sentiment POC<br/>👤 Rana"]
        S0_POC --> S0_POC_Deploy["Docker POC<br/>👤 Hager"]

        S0_Env --> S0_Env_Repo["GitHub Repo"]
        S0_Env --> S0_Env_Docker["Docker Compose"]
        S0_Env --> S0_Env_Deps["Dependencies"]

        S0_Board --> S0_Board_Cols["Board Columns"]
        S0_Board --> S0_Board_Labels["Labels & Milestones"]
        S0_Board --> S0_Board_Views["Project Views"]
    end

    subgraph Sprint1["🔨 Sprint 1: Core AI Framework<br/>Dec 6 - Dec 19"]
        S1_US001["US-001<br/>Agent Framework"]
        S1_US002["US-002<br/>Brand RAG"]
        S1_US003["US-003<br/>Campaign Planner"]
        S1_US010["US-010<br/>Brand DNA"]
        S1_US014["US-014<br/>CI/CD Pipeline"]

        %% Level 4 - Sprint 1 Work Packages
        S1_US001 --> S1_001_Crew["CrewAI Setup"]
        S1_US001 --> S1_001_Memory["Agent Memory"]
        S1_US001 --> S1_001_Orch["Task Orchestration"]
        S1_US001 --> S1_001_Tests["Agent Tests"]

        S1_US002 --> S1_002_Upload["Doc Upload API"]
        S1_US002 --> S1_002_Embed["Embedding Pipeline"]
        S1_US002 --> S1_002_Vector["Vector DB Setup"]
        S1_US002 --> S1_002_Query["RAG Query Function"]

        S1_US003 --> S1_003_Form["Campaign Form UI"]
        S1_US003 --> S1_003_API["Campaign API"]
        S1_US003 --> S1_003_Agent["Strategy Agent"]

        S1_US010 --> S1_010_Visual["Visual DNA Extract"]
        S1_US010 --> S1_010_Ling["Linguistic Analysis"]
        S1_US010 --> S1_010_UI["DNA Dashboard"]

        S1_US014 --> S1_014_GHA["GitHub Actions"]
        S1_US014 --> S1_014_Tests["AI Model Tests"]
        S1_US014 --> S1_014_Deploy["Staging Deploy"]
    end

    subgraph Sprint2["📊 Sprint 2: Analytics & Scheduling<br/>Dec 20 - Jan 2"]
        S2_US004["US-004<br/>Content Scheduler"]
        S2_US005["US-005<br/>Sentiment Dashboard"]
        S2_US007["US-007<br/>Message Inbox"]
        S2_US011["US-011<br/>Hallucination Detector"]
        S2_US015["US-015<br/>Rate Limiter"]

        %% Level 4 - Sprint 2 Work Packages
        S2_US004 --> S2_004_Calendar["Calendar UI"]
        S2_US004 --> S2_004_Optimal["Optimal Time AI"]
        S2_US004 --> S2_004_Publish["Auto-Publish Jobs"]

        S2_US005 --> S2_005_Model["Sentiment Model"]
        S2_US005 --> S2_005_Charts["Dashboard Charts"]
        S2_US005 --> S2_005_Alerts["Sentiment Alerts"]

        S2_US007 --> S2_007_Inbox["Unified Inbox UI"]
        S2_US007 --> S2_007_Priority["AI Prioritization"]
        S2_US007 --> S2_007_Polling["API Polling"]

        S2_US011 --> S2_011_Claims["Claim Extraction"]
        S2_US011 --> S2_011_Verify["KB Verification"]
        S2_US011 --> S2_011_Brand["Brand Consistency"]

        S2_US015 --> S2_015_Bucket["Token Bucket"]
        S2_US015 --> S2_015_Queue["Priority Queue"]
        S2_US015 --> S2_015_Cache["Redis Caching"]
    end

    subgraph Sprint3["✨ Sprint 3: Autonomous Content<br/>Jan 3 - Jan 16"]
        S3_US006["US-006<br/>Anomaly Detection"]
        S3_US008["US-008<br/>AI Response Suggest"]
        S3_US009["US-009<br/>Trend Content Gen"]
        S3_US012["US-012<br/>Human-in-Loop"]
        S3_US013["US-013<br/>Model Monitoring"]

        %% Level 4 - Sprint 3 Work Packages
        S3_US006 --> S3_006_Zscore["Z-Score Algorithm"]
        S3_US006 --> S3_006_Notify["Alert System"]
        S3_US006 --> S3_006_Log["Anomaly Dashboard"]

        S3_US008 --> S3_008_Gen["Response Generator"]
        S3_US008 --> S3_008_Voice["Brand Voice Match"]
        S3_US008 --> S3_008_Feed["Feedback Loop"]

        S3_US009 --> S3_009_Trends["Trend Discovery"]
        S3_US009 --> S3_009_Posts["Post Generation"]
        S3_US009 --> S3_009_Valid["Content Validation"]

        S3_US012 --> S3_012_Route["Routing Logic"]
        S3_US012 --> S3_012_Queue["Review Queue UI"]
        S3_US012 --> S3_012_Learn["Learning Loop"]

        S3_US013 --> S3_013_Metrics["Prometheus Metrics"]
        S3_US013 --> S3_013_Dash["Grafana Dashboard"]
        S3_US013 --> S3_013_AB["A/B Testing"]
    end

    subgraph CrossCutting["🏗️ Cross-Cutting Infrastructure"]
        CC_Backend["Backend Services"]
        CC_Frontend["Frontend Components"]
        CC_Data["Data Layer"]
        CC_External["External APIs"]

        CC_Backend --> CC_BE_FastAPI["FastAPI Server"]
        CC_Backend --> CC_BE_Auth["JWT Auth"]
        CC_Backend --> CC_BE_Jobs["Job Scheduler"]

        CC_Frontend --> CC_FE_React["React Dashboard"]
        CC_Frontend --> CC_FE_Charts["Chart Components"]
        CC_Frontend --> CC_FE_Forms["Form Components"]

        CC_Data --> CC_Data_Mongo["MongoDB"]
        CC_Data --> CC_Data_Vector["Pinecone/Qdrant"]
        CC_Data --> CC_Data_Redis["Redis Cache"]

        CC_External --> CC_Ext_Meta["Meta API"]
        CC_External --> CC_Ext_LinkedIn["LinkedIn API"]
        CC_External --> CC_Ext_X["X API"]
        CC_External --> CC_Ext_OpenAI["OpenAI API"]
    end

    subgraph AIML["🧠 AI/ML Foundations"]
        AI_Agents["AI Agents"]
        AI_Models["ML Models"]
        AI_LLM["LLM Integration"]

        AI_Agents --> AI_Agent_Strat["Marketing Strategist"]
        AI_Agents --> AI_Agent_Social["Social Analyst"]
        AI_Agents --> AI_Agent_CRM["Customer Relations"]
        AI_Agents --> AI_Agent_Content["Content Engine"]

        AI_Models --> AI_Model_Sent["Sentiment Model"]
        AI_Models --> AI_Model_NER["NER Model"]
        AI_Models --> AI_Model_Brand["Brand Scorer"]

        AI_LLM --> AI_LLM_Prompt["Prompt Engineering"]
        AI_LLM --> AI_LLM_RAG["RAG Retrieval"]
        AI_LLM --> AI_LLM_Cache["Response Caching"]
    end

    subgraph CICD["⚙️ CI/CD & Quality"]
        QA_Pipeline["Pipeline Stages"]
        QA_Testing["Testing Suites"]
        QA_Deploy["Deployment"]

        QA_Pipeline --> QA_Lint["Linting"]
        QA_Pipeline --> QA_Unit["Unit Tests"]
        QA_Pipeline --> QA_AITest["AI Model Tests"]
        QA_Pipeline --> QA_Security["Security Scan"]

        QA_Testing --> QA_Test_Sent["Sentiment Accuracy"]
        QA_Testing --> QA_Test_Hall["Hallucination Tests"]
        QA_Testing --> QA_Test_Brand["Brand Consistency"]

        QA_Deploy --> QA_Deploy_Stage["Staging"]
        QA_Deploy --> QA_Deploy_Roll["Rollback"]
        QA_Deploy --> QA_Deploy_Notify["Slack Alerts"]
    end

    subgraph Docs["📚 Documentation"]
        Doc_Arch["Architecture Docs"]
        Doc_API["API Specs"]
        Doc_Guide["Dev Guides"]
        Doc_Risk["Risk Management"]

        Doc_Arch --> Doc_Arch_Sys["System Diagram"]
        Doc_Arch --> Doc_Arch_Data["Data Flow"]
        Doc_Arch --> Doc_Arch_Agent["Agent Protocols"]

        Doc_API --> Doc_API_Swagger["OpenAPI Spec"]
        Doc_API --> Doc_API_Auth["Auth Flow"]
        Doc_API --> Doc_API_Rate["Rate Limits"]

        Doc_Guide --> Doc_Guide_Setup["Setup Guide"]
        Doc_Guide --> Doc_Guide_Learn["AI Learning Plan"]
        Doc_Guide --> Doc_Guide_Contrib["Contribution Guide"]

        Doc_Risk --> Doc_Risk_Log["Risk Log"]
        Doc_Risk --> Doc_Risk_Mit["Mitigations"]
        Doc_Risk --> Doc_Risk_Monitor["Monitoring"]
    end

    subgraph Team["👥 Team Responsibilities"]
        Team_Elattar["Abdelrahman Elattar<br/>PO + AI/ML Lead"]
        Team_Omar["Abdelrahman Omar<br/>PO + Backend AI Lead"]
        Team_Rana["Rana Mahmoud<br/>SM + Analytics Lead"]
        Team_Hager["Hager Saad<br/>SM + DevOps Lead"]
    end

    %% Cross-Dependencies
    S0_POC_Crew -->|validates| S1_US001
    S0_POC_RAG -->|validates| S1_US002
    S0_POC_Sent -->|validates| S2_US005
    S0_POC_Deploy -->|validates| S1_US014

    S1_US001 -->|enables| S1_US003
    S1_US001 -->|enables| S3_US008
    S1_US001 -->|enables| S3_US009

    S1_US002 -->|feeds| S2_US011
    S1_US002 -->|feeds| S3_US008
    S1_US010 -->|feeds| S2_US011

    S2_US005 -->|triggers| S3_US006
    S2_US011 -->|protects| S3_US012

    S3_US009 -->|requires| S3_US012

    %% Team to Components
    Team_Elattar -.->|owns| AI_Agents
    Team_Omar -.->|owns| CC_Backend
    Team_Rana -.->|owns| AI_Models
    Team_Hager -.->|owns| CICD

    %% Styling
    classDef sprint0 fill:#818cf8,stroke:#6366f1,color:#fff
    classDef sprint1 fill:#34d399,stroke:#10b981,color:#fff
    classDef sprint2 fill:#fbbf24,stroke:#f59e0b,color:#000
    classDef sprint3 fill:#f87171,stroke:#ef4444,color:#fff
    classDef infra fill:#64748b,stroke:#475569,color:#fff
    classDef team fill:#a78bfa,stroke:#8b5cf6,color:#fff

    class S0_Stories,S0_Arch,S0_POC,S0_Env,S0_Board sprint0
    class S1_US001,S1_US002,S1_US003,S1_US010,S1_US014 sprint1
    class S2_US004,S2_US005,S2_US007,S2_US011,S2_US015 sprint2
    class S3_US006,S3_US008,S3_US009,S3_US012,S3_US013 sprint3
    class CC_Backend,CC_Frontend,CC_Data,CC_External infra
    class Team_Elattar,Team_Omar,Team_Rana,Team_Hager team
