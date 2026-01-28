import { BarChart3 } from 'lucide-react'
import { Card, CardContent } from '@/components/ui'

export function AnalyticsPage() {
    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-text-primary">Analytics</h1>
                <p className="mt-1 text-text-secondary">
                    Performance insights and AI predictions
                </p>
            </div>

            <Card>
                <CardContent className="flex flex-col items-center justify-center py-16">
                    <BarChart3 className="h-16 w-16 text-text-muted mb-4" />
                    <h3 className="text-xl font-medium text-text-primary mb-2">
                        Coming Soon
                    </h3>
                    <p className="text-text-secondary text-center max-w-md">
                        Advanced analytics with sentiment trends, engagement predictions,
                        and AI-powered insights will be available once the backend endpoints are implemented.
                    </p>
                </CardContent>
            </Card>
        </div>
    )
}
