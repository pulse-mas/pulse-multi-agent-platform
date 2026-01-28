import { FileText } from 'lucide-react'
import { Card, CardContent } from '@/components/ui'

export function ContentPage() {
    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-text-primary">Content</h1>
                <p className="mt-1 text-text-secondary">
                    Manage and schedule your social media posts
                </p>
            </div>

            <Card>
                <CardContent className="flex flex-col items-center justify-center py-16">
                    <FileText className="h-16 w-16 text-text-muted mb-4" />
                    <h3 className="text-xl font-medium text-text-primary mb-2">
                        Coming Soon
                    </h3>
                    <p className="text-text-secondary text-center max-w-md">
                        AI-powered content creation, scheduling calendar, and multi-platform
                        publishing will be available once the backend endpoints are implemented.
                    </p>
                </CardContent>
            </Card>
        </div>
    )
}
