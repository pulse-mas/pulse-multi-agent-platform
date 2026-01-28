// ============================================
// API Type Definitions for Pulse Platform
// ============================================

// ============================================
// Type Constants (using const assertions instead of enums)
// ============================================

export const Sentiments = {
    POSITIVE: 'positive',
    NEUTRAL: 'neutral',
    NEGATIVE: 'negative',
} as const

export type Sentiment = (typeof Sentiments)[keyof typeof Sentiments]

export const PostStatuses = {
    DRAFT: 'draft',
    SCHEDULED: 'scheduled',
    PUBLISHED: 'published',
    FAILED: 'failed',
} as const

export type PostStatus = (typeof PostStatuses)[keyof typeof PostStatuses]

export const AgentRoles = {
    STRATEGIST: 'strategist',
    ANALYST: 'analyst',
    SUPPORT: 'support',
    CONTENT_ENGINE: 'content_engine',
} as const

export type AgentRole = (typeof AgentRoles)[keyof typeof AgentRoles]

export const AgentStatuses = {
    ACTIVE: 'active',
    IDLE: 'idle',
    ERROR: 'error',
} as const

export type AgentStatus = (typeof AgentStatuses)[keyof typeof AgentStatuses]

export const UserRoles = {
    ADMIN: 'admin',
    MANAGER: 'manager',
    ANALYST: 'analyst',
} as const

export type UserRole = (typeof UserRoles)[keyof typeof UserRoles]

// ============================================
// Product DNA Types (Currently Implemented)
// ============================================

export interface PostMetadata {
    score: number
    url: string
    subreddit: string
    author: string
    created_utc: string
    num_comments: number
    upvote_ratio: number
}

export interface EnrichedPost {
    post_id: string
    title: string
    body: string
    sentiment: Sentiment
    summary: string
    metadata: PostMetadata
    keywords: string[]
    enriched_at: string
}

export interface CollectionRequest {
    keywords: string[]
    subreddits?: string[]
    limit?: number
    time_filter?: 'hour' | 'day' | 'week' | 'month' | 'year' | 'all'
}

export interface CollectionResponse {
    success: boolean
    posts_collected: number
    posts_enriched: number
    posts_stored: number
    errors: string[]
    sample: EnrichedPost[]
}

export interface ProductDNAStats {
    total_posts: number
    by_sentiment: Record<string, number>
    by_subreddit: Record<string, number>
    last_collection: string | null
}

// ============================================
// Health & Status Types (Currently Implemented)
// ============================================

export interface HealthResponse {
    status: string
    timestamp: string
}

export interface SystemStatusResponse {
    app_name: string
    version: string
    python_version: string
    uptime_seconds: number
    environment: string
    dependencies: Record<string, unknown>
}

// ============================================
// Authentication Types (Planned)
// ============================================

export interface User {
    id: string
    email: string
    name: string
    role: UserRole
    avatar_url?: string
    created_at: string
}

export interface LoginRequest {
    email: string
    password: string
}

export interface LoginResponse {
    access_token: string
    token_type: string
    user: User
}

export interface RegisterRequest {
    email: string
    password: string
    name: string
}

// ============================================
// Brand Types (Planned)
// ============================================

export interface Brand {
    id: string
    name: string
    industry: string
    website?: string
    logo_url?: string
    created_at: string
}

export interface BrandCreate {
    name: string
    industry?: string
    website?: string
}

// ============================================
// Content Types (Planned)
// ============================================

export interface Post {
    id: string
    brand_id: string
    content: string
    platforms: string[]
    media_urls?: string[]
    hashtags?: string[]
    scheduled_at?: string
    published_at?: string
    status: PostStatus
    created_at: string
}

export interface PostCreate {
    brand_id: string
    content: string
    platforms: string[]
    media_urls?: string[]
    hashtags?: string[]
    scheduled_at?: string
}

// ============================================
// Analytics Types (Planned)
// ============================================

export interface AnalyticsOverview {
    total_posts: number
    total_engagement: number
    avg_sentiment: number
    posts_scheduled: number
    period: string
}

export interface TrendData {
    date: string
    likes: number
    comments: number
    shares: number
    reach: number
}

// ============================================
// Agent Types (Planned)
// ============================================

export interface Agent {
    id: string
    name: string
    role: AgentRole
    status: AgentStatus
    current_task?: string
    tasks_completed: number
    avg_response_time: number
    last_active?: string
}

export interface AgentTask {
    id: string
    agent_id: string
    description: string
    status: 'pending' | 'running' | 'completed' | 'failed'
    result?: unknown
    created_at: string
    completed_at?: string
}

// ============================================
// Interaction Types (Planned)
// ============================================

export interface Interaction {
    id: string
    brand_id: string
    platform: string
    sender_name: string
    sender_avatar?: string
    message: string
    urgency: 1 | 2 | 3 | 4 | 5
    sentiment: Sentiment
    status: 'unread' | 'read' | 'responded' | 'escalated'
    created_at: string
}

export interface AISuggestion {
    text: string
    confidence: number
    intent: string
}

// ============================================
// API Response Wrappers
// ============================================

export interface ApiError {
    error: string
    message: string
    details?: Record<string, unknown>
    timestamp: string
}

export interface PaginatedResponse<T> {
    data: T[]
    total: number
    page: number
    page_size: number
    total_pages: number
}

// ============================================
// Query Parameter Types
// ============================================

export interface ProductDNAListParams {
    sentiment?: Sentiment
    subreddit?: string
    limit?: number
    skip?: number
}

export interface PostListParams {
    brand_id?: string
    status?: PostStatus
    platform?: string
    limit?: number
    skip?: number
}
