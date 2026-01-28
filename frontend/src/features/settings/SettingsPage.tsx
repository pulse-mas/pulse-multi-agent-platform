import { Settings } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui'

export function SettingsPage() {
    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-text-primary">Settings</h1>
                <p className="mt-1 text-text-secondary">
                    Configure your platform preferences
                </p>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
                <Card>
                    <CardHeader>
                        <CardTitle>Profile</CardTitle>
                    </CardHeader>
                    <CardContent className="text-text-secondary">
                        User profile settings will be available after authentication is implemented.
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Notifications</CardTitle>
                    </CardHeader>
                    <CardContent className="text-text-secondary">
                        Notification preferences will be available after the notification system is implemented.
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Integrations</CardTitle>
                    </CardHeader>
                    <CardContent className="text-text-secondary">
                        Social media platform connections will be available after OAuth integration is implemented.
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>API Keys</CardTitle>
                    </CardHeader>
                    <CardContent className="text-text-secondary">
                        API key management will be available after the authentication system is implemented.
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}
