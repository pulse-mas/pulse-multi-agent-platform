import { Bot } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle, Badge } from '@/components/ui'

const agents = [
    {
        id: 'marketing-strategist',
        name: 'Marketing Strategist',
        role: 'Strategic planning and brand consistency',
        status: 'active',
    },
    {
        id: 'social-analyst',
        name: 'Social Media Analyst',
        role: 'Content automation and analytics',
        status: 'active',
    },
    {
        id: 'customer-relationship',
        name: 'Customer Relationship Agent',
        role: 'Multi-channel customer support',
        status: 'idle',
    },
    {
        id: 'content-engine',
        name: 'Content Engine',
        role: 'Autonomous content generation',
        status: 'active',
    },
]

export function AgentsPage() {
    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-text-primary">AI Agents</h1>
                <p className="mt-1 text-text-secondary">
                    Monitor and control your AI agent workforce
                </p>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
                {agents.map((agent) => (
                    <Card key={agent.id} className="hover:border-pulse-primary/50 transition-colors">
                        <CardHeader>
                            <div className="flex items-start justify-between">
                                <div className="flex items-center gap-3">
                                    <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-pulse-primary to-pulse-secondary">
                                        <Bot className="h-6 w-6 text-white" />
                                    </div>
                                    <div>
                                        <CardTitle className="text-lg">{agent.name}</CardTitle>
                                        <p className="text-sm text-text-secondary">{agent.role}</p>
                                    </div>
                                </div>
                                <Badge
                                    variant={agent.status === 'active' ? 'success' : 'outline'}
                                >
                                    {agent.status}
                                </Badge>
                            </div>
                        </CardHeader>
                        <CardContent>
                            <div className="flex items-center justify-between text-sm">
                                <span className="text-text-muted">Tasks Completed</span>
                                <span className="text-text-primary font-medium">--</span>
                            </div>
                            <div className="flex items-center justify-between text-sm mt-2">
                                <span className="text-text-muted">Avg Response Time</span>
                                <span className="text-text-primary font-medium">--</span>
                            </div>
                        </CardContent>
                    </Card>
                ))}
            </div>

            <Card>
                <CardContent className="py-8 text-center">
                    <p className="text-text-secondary">
                        Agent orchestration and task management will be available once the backend endpoints are implemented.
                    </p>
                </CardContent>
            </Card>
        </div>
    )
}
