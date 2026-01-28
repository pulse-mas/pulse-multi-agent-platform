import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { motion } from 'framer-motion'
import { useForm } from 'react-hook-form'
import {
    Database,
    Plus,
    Filter,
    RefreshCw,
    ExternalLink,
} from 'lucide-react'
import {
    Button,
    Card,
    CardContent,
    CardHeader,
    CardTitle,
    CardDescription,
    Badge,
    Input,
    Skeleton,
} from '@/components/ui'
import { productDnaApi } from '@/lib/api'
import { formatRelativeTime } from '@/lib/utils'
import type { EnrichedPost, Sentiment, CollectionRequest } from '@/types'

function SentimentBadge({ sentiment }: { sentiment: Sentiment }) {
    return (
        <Badge
            variant={
                sentiment === 'positive'
                    ? 'positive'
                    : sentiment === 'negative'
                        ? 'negative'
                        : 'neutral'
            }
        >
            {sentiment}
        </Badge>
    )
}

function PostCard({ post }: { post: EnrichedPost }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.2 }}
        >
            <Card className="hover:border-pulse-primary/50 transition-colors">
                <CardContent className="p-5">
                    <div className="flex items-start justify-between gap-4">
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2 mb-2">
                                <SentimentBadge sentiment={post.sentiment} />
                                <span className="text-sm text-text-muted">
                                    r/{post.metadata.subreddit}
                                </span>
                                <span className="text-sm text-text-muted">•</span>
                                <span className="text-sm text-text-muted">
                                    {formatRelativeTime(post.metadata.created_utc)}
                                </span>
                            </div>
                            <h3 className="font-semibold text-text-primary mb-2 line-clamp-2">
                                {post.title}
                            </h3>
                            <p className="text-sm text-text-secondary mb-3">
                                {post.summary}
                            </p>
                            <div className="flex items-center gap-4 text-sm text-text-muted">
                                <span>⬆️ {post.metadata.score}</span>
                                <span>💬 {post.metadata.num_comments}</span>
                                <span>👤 {post.metadata.author}</span>
                            </div>
                        </div>
                        <a
                            href={post.metadata.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="shrink-0"
                        >
                            <Button variant="ghost" size="icon-sm">
                                <ExternalLink className="h-4 w-4" />
                            </Button>
                        </a>
                    </div>
                </CardContent>
            </Card>
        </motion.div>
    )
}

function CollectionForm({ onClose }: { onClose: () => void }) {
    const queryClient = useQueryClient()

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<{
        keywords: string
        subreddits: string
        limit: number
        time_filter: 'hour' | 'day' | 'week' | 'month' | 'year' | 'all'
    }>({
        defaultValues: {
            keywords: '',
            subreddits: '',
            limit: 10,
            time_filter: 'week',
        },
    })

    const collectMutation = useMutation({
        mutationFn: (data: CollectionRequest) => productDnaApi.collect(data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['product-dna'] })
            onClose()
        },
    })

    const onSubmit = handleSubmit((data) => {
        if (!data.keywords.trim()) {
            return
        }
        const request: CollectionRequest = {
            keywords: data.keywords.split(',').map((k) => k.trim()).filter(Boolean),
            subreddits: data.subreddits
                ? data.subreddits.split(',').map((s) => s.trim()).filter(Boolean)
                : undefined,
            limit: data.limit,
            time_filter: data.time_filter,
        }
        collectMutation.mutate(request)
    })

    return (
        <Card>
            <CardHeader>
                <CardTitle>Collect Product DNA</CardTitle>
                <CardDescription>
                    Search Reddit for posts matching your keywords and enrich them with AI analysis.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <form onSubmit={onSubmit} className="space-y-4">
                    <div>
                        <label className="text-sm font-medium text-text-primary">
                            Keywords *
                        </label>
                        <Input
                            {...register('keywords')}
                            placeholder="social media marketing, engagement tips"
                            error={errors.keywords?.message}
                        />
                        <p className="mt-1 text-xs text-text-muted">
                            Separate multiple keywords with commas
                        </p>
                    </div>

                    <div>
                        <label className="text-sm font-medium text-text-primary">
                            Subreddits (optional)
                        </label>
                        <Input
                            {...register('subreddits')}
                            placeholder="marketing, socialmedia, smallbusiness"
                        />
                        <p className="mt-1 text-xs text-text-muted">
                            Leave empty for defaults: marketing, socialmedia, smallbusiness
                        </p>
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <label className="text-sm font-medium text-text-primary">
                                Limit
                            </label>
                            <Input
                                {...register('limit')}
                                type="number"
                                min={1}
                                max={100}
                            />
                        </div>
                        <div>
                            <label className="text-sm font-medium text-text-primary">
                                Time Filter
                            </label>
                            <select
                                {...register('time_filter')}
                                className="flex h-10 w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary focus:outline-none focus:ring-2 focus:ring-pulse-primary"
                            >
                                <option value="hour">Last Hour</option>
                                <option value="day">Last 24 Hours</option>
                                <option value="week">Last Week</option>
                                <option value="month">Last Month</option>
                                <option value="year">Last Year</option>
                                <option value="all">All Time</option>
                            </select>
                        </div>
                    </div>

                    {collectMutation.error && (
                        <p className="text-sm text-error">
                            {(collectMutation.error as Error).message}
                        </p>
                    )}

                    {collectMutation.data && (
                        <div className="rounded-lg bg-success/10 p-4 text-sm">
                            <p className="font-medium text-success">Collection Complete!</p>
                            <p className="text-text-secondary">
                                Collected: {collectMutation.data.posts_collected} |
                                Enriched: {collectMutation.data.posts_enriched} |
                                Stored: {collectMutation.data.posts_stored}
                            </p>
                        </div>
                    )}

                    <div className="flex justify-end gap-3">
                        <Button type="button" variant="outline" onClick={onClose}>
                            Cancel
                        </Button>
                        <Button
                            type="submit"
                            isLoading={collectMutation.isPending}
                        >
                            <Database className="h-4 w-4" />
                            Collect
                        </Button>
                    </div>
                </form>
            </CardContent>
        </Card>
    )
}

export function ProductDNAPage() {
    const [showForm, setShowForm] = useState(false)
    const [sentimentFilter, setSentimentFilter] = useState<Sentiment | ''>('')

    const { data: posts, isLoading, refetch, isRefetching } = useQuery({
        queryKey: ['product-dna', 'list', sentimentFilter],
        queryFn: () =>
            productDnaApi.list({
                sentiment: sentimentFilter || undefined,
                limit: 50,
            }),
    })

    const { data: stats } = useQuery({
        queryKey: ['product-dna', 'stats'],
        queryFn: productDnaApi.getStats,
    })

    return (
        <div className="space-y-6">
            {/* Page Header */}
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-3xl font-bold text-text-primary">Product DNA</h1>
                    <p className="mt-1 text-text-secondary">
                        AI-analyzed social media posts for market insights
                    </p>
                </div>
                <div className="flex items-center gap-3">
                    <Button
                        variant="outline"
                        onClick={() => refetch()}
                        isLoading={isRefetching}
                    >
                        <RefreshCw className="h-4 w-4" />
                        Refresh
                    </Button>
                    <Button onClick={() => setShowForm(true)}>
                        <Plus className="h-4 w-4" />
                        Collect New
                    </Button>
                </div>
            </div>

            {/* Collection Form */}
            {showForm && (
                <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                >
                    <CollectionForm onClose={() => setShowForm(false)} />
                </motion.div>
            )}

            {/* Stats Summary */}
            {stats && (
                <div className="grid gap-4 md:grid-cols-4">
                    <Card>
                        <CardContent className="p-4">
                            <p className="text-sm text-text-secondary">Total Posts</p>
                            <p className="text-2xl font-bold text-text-primary">
                                {stats.total_posts}
                            </p>
                        </CardContent>
                    </Card>
                    <Card>
                        <CardContent className="p-4">
                            <p className="text-sm text-text-secondary">Positive</p>
                            <p className="text-2xl font-bold text-success">
                                {stats.by_sentiment?.positive ?? 0}
                            </p>
                        </CardContent>
                    </Card>
                    <Card>
                        <CardContent className="p-4">
                            <p className="text-sm text-text-secondary">Neutral</p>
                            <p className="text-2xl font-bold text-text-muted">
                                {stats.by_sentiment?.neutral ?? 0}
                            </p>
                        </CardContent>
                    </Card>
                    <Card>
                        <CardContent className="p-4">
                            <p className="text-sm text-text-secondary">Negative</p>
                            <p className="text-2xl font-bold text-error">
                                {stats.by_sentiment?.negative ?? 0}
                            </p>
                        </CardContent>
                    </Card>
                </div>
            )}

            {/* Filters */}
            <div className="flex items-center gap-3">
                <Filter className="h-5 w-5 text-text-muted" />
                <span className="text-sm text-text-secondary">Filter:</span>
                <div className="flex gap-2">
                    {['', 'positive', 'neutral', 'negative'].map((s) => (
                        <Button
                            key={s || 'all'}
                            variant={sentimentFilter === s ? 'default' : 'outline'}
                            size="sm"
                            onClick={() => setSentimentFilter(s as Sentiment | '')}
                        >
                            {s || 'All'}
                        </Button>
                    ))}
                </div>
            </div>

            {/* Posts List */}
            {isLoading ? (
                <div className="space-y-4">
                    {[...Array(5)].map((_, i) => (
                        <Skeleton key={i} className="h-32 w-full" />
                    ))}
                </div>
            ) : posts && posts.length > 0 ? (
                <div className="space-y-4">
                    {posts.map((post) => (
                        <PostCard key={post.post_id} post={post} />
                    ))}
                </div>
            ) : (
                <Card>
                    <CardContent className="flex flex-col items-center justify-center py-12">
                        <Database className="h-12 w-12 text-text-muted mb-4" />
                        <h3 className="text-lg font-medium text-text-primary mb-2">
                            No Product DNA Yet
                        </h3>
                        <p className="text-text-secondary mb-4">
                            Start by collecting posts from Reddit to build your knowledge base.
                        </p>
                        <Button onClick={() => setShowForm(true)}>
                            <Plus className="h-4 w-4" />
                            Collect First Batch
                        </Button>
                    </CardContent>
                </Card>
            )}
        </div>
    )
}
