import { useQuery } from '@tanstack/react-query'
import { motion } from 'framer-motion'
import {
    Database,
    TrendingUp,
    MessageSquare,
    Bot,
    ArrowUpRight,
    ArrowDownRight,
} from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle, Badge } from '@/components/ui'
import { productDnaApi, healthApi } from '@/lib/api'
import { cn, formatNumber } from '@/lib/utils'

interface StatCardProps {
    title: string
    value: string | number
    change?: number
    icon: React.ElementType
    gradient: string
}

function StatCard({ title, value, change, icon: Icon, gradient }: StatCardProps) {
    const isPositive = change && change > 0

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3 }}
        >
            <Card className="overflow-hidden">
                <CardContent className="p-6">
                    <div className="flex items-start justify-between">
                        <div>
                            <p className="text-sm text-text-secondary">{title}</p>
                            <p className="mt-2 text-3xl font-bold text-text-primary">
                                {typeof value === 'number' ? formatNumber(value) : value}
                            </p>
                            {change !== undefined && (
                                <div className="mt-2 flex items-center gap-1">
                                    {isPositive ? (
                                        <ArrowUpRight className="h-4 w-4 text-success" />
                                    ) : (
                                        <ArrowDownRight className="h-4 w-4 text-error" />
                                    )}
                                    <span
                                        className={cn(
                                            'text-sm font-medium',
                                            isPositive ? 'text-success' : 'text-error'
                                        )}
                                    >
                                        {Math.abs(change)}%
                                    </span>
                                    <span className="text-sm text-text-muted">vs last week</span>
                                </div>
                            )}
                        </div>
                        <div
                            className={cn(
                                'flex h-12 w-12 items-center justify-center rounded-xl',
                                gradient
                            )}
                        >
                            <Icon className="h-6 w-6 text-white" />
                        </div>
                    </div>
                </CardContent>
            </Card>
        </motion.div>
    )
}

export function DashboardPage() {
    // Fetch system status
    const { data: status } = useQuery({
        queryKey: ['system-status'],
        queryFn: healthApi.status,
    })

    // Fetch Product DNA stats
    const { data: stats, isLoading: statsLoading } = useQuery({
        queryKey: ['product-dna-stats'],
        queryFn: productDnaApi.getStats,
    })

    return (
        <div className="space-y-8">
            {/* Page Header */}
            <div>
                <h1 className="text-3xl font-bold text-text-primary">Dashboard</h1>
                <p className="mt-1 text-text-secondary">
                    Welcome back! Here's your platform overview.
                </p>
            </div>

            {/* Stats Grid */}
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
                <StatCard
                    title="Total Posts Collected"
                    value={statsLoading ? '...' : stats?.total_posts ?? 0}
                    change={12}
                    icon={Database}
                    gradient="bg-gradient-to-br from-pulse-primary to-pulse-secondary"
                />
                <StatCard
                    title="Positive Sentiment"
                    value={
                        statsLoading
                            ? '...'
                            : `${stats?.by_sentiment?.positive ?? 0} posts`
                    }
                    change={8}
                    icon={TrendingUp}
                    gradient="bg-gradient-to-br from-success to-emerald-400"
                />
                <StatCard
                    title="Interactions"
                    value="Coming Soon"
                    icon={MessageSquare}
                    gradient="bg-gradient-to-br from-info to-blue-400"
                />
                <StatCard
                    title="Active Agents"
                    value="4"
                    icon={Bot}
                    gradient="bg-gradient-to-br from-pulse-secondary to-pink-400"
                />
            </div>

            {/* Content Grid */}
            <div className="grid gap-6 lg:grid-cols-3">
                {/* Sentiment Overview */}
                <Card className="lg:col-span-2">
                    <CardHeader>
                        <CardTitle>Sentiment Overview</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {statsLoading ? (
                            <div className="h-48 flex items-center justify-center text-text-muted">
                                Loading sentiment data...
                            </div>
                        ) : stats?.by_sentiment ? (
                            <div className="space-y-4">
                                {Object.entries(stats.by_sentiment).map(([sentiment, count]) => (
                                    <div key={sentiment} className="flex items-center gap-4">
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
                                        <div className="flex-1">
                                            <div className="h-3 w-full rounded-full bg-surface-elevated overflow-hidden">
                                                <div
                                                    className={cn(
                                                        'h-full rounded-full transition-all duration-500',
                                                        sentiment === 'positive'
                                                            ? 'bg-success'
                                                            : sentiment === 'negative'
                                                                ? 'bg-error'
                                                                : 'bg-text-muted'
                                                    )}
                                                    style={{
                                                        width: `${(count / (stats.total_posts || 1)) * 100}%`,
                                                    }}
                                                />
                                            </div>
                                        </div>
                                        <span className="text-sm font-medium text-text-primary w-16 text-right">
                                            {count} posts
                                        </span>
                                    </div>
                                ))}
                            </div>
                        ) : (
                            <div className="h-48 flex items-center justify-center text-text-muted">
                                No sentiment data available. Collect some Product DNA first!
                            </div>
                        )}
                    </CardContent>
                </Card>

                {/* System Status */}
                <Card>
                    <CardHeader>
                        <CardTitle>System Status</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="flex items-center justify-between">
                            <span className="text-text-secondary">Backend</span>
                            <Badge variant="success">Online</Badge>
                        </div>
                        <div className="flex items-center justify-between">
                            <span className="text-text-secondary">Version</span>
                            <span className="text-text-primary font-mono text-sm">
                                {status?.version ?? '...'}
                            </span>
                        </div>
                        <div className="flex items-center justify-between">
                            <span className="text-text-secondary">Environment</span>
                            <span className="text-text-primary font-mono text-sm">
                                {status?.environment ?? '...'}
                            </span>
                        </div>
                        <div className="flex items-center justify-between">
                            <span className="text-text-secondary">Uptime</span>
                            <span className="text-text-primary font-mono text-sm">
                                {status?.uptime_seconds
                                    ? `${Math.floor(status.uptime_seconds / 60)}m`
                                    : '...'}
                            </span>
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* Subreddit Distribution */}
            {stats?.by_subreddit && Object.keys(stats.by_subreddit).length > 0 && (
                <Card>
                    <CardHeader>
                        <CardTitle>Posts by Subreddit</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="flex flex-wrap gap-3">
                            {Object.entries(stats.by_subreddit).map(([subreddit, count]) => (
                                <div
                                    key={subreddit}
                                    className="flex items-center gap-2 rounded-lg bg-surface-elevated px-4 py-2"
                                >
                                    <span className="text-pulse-primary font-medium">
                                        r/{subreddit}
                                    </span>
                                    <Badge variant="outline">{count}</Badge>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
            )}
        </div>
    )
}
