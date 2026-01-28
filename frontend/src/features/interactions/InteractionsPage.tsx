import { MessageSquare } from 'lucide-react'
import { Card, CardContent } from '@/components/ui'

export function InteractionsPage() {
    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-text-primary">Interactions</h1>
                <p className="mt-1 text-text-secondary">
                    Unified inbox for customer messages
                </p>
            </div>

            <Card>
                <CardContent className="flex flex-col items-center justify-center py-16">
                    <MessageSquare className="h-16 w-16 text-text-muted mb-4" />
                    <h3 className="text-xl font-medium text-text-primary mb-2">
                        Coming Soon
                    </h3>
                    <p className="text-text-secondary text-center max-w-md">
                        AI-prioritized message inbox with smart response suggestions
                        will be available once the backend endpoints are implemented.
                    </p>
                </CardContent>
            </Card>
        </div>
    )
}
