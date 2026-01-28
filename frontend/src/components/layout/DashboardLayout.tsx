import { Outlet } from 'react-router-dom'
import { Sidebar } from './Sidebar'
import { Header } from './Header'
import { cn } from '@/lib/utils'
import { useUIStore } from '@/stores'

export function DashboardLayout() {
    const { sidebarCollapsed } = useUIStore()

    return (
        <div className="min-h-screen bg-background">
            {/* Sidebar */}
            <Sidebar />

            {/* Main Content */}
            <div
                className={cn(
                    'transition-all duration-200',
                    sidebarCollapsed ? 'ml-[72px]' : 'ml-64'
                )}
            >
                {/* Header */}
                <Header />

                {/* Page Content */}
                <main className="min-h-screen pt-16">
                    <div className="p-6">
                        <Outlet />
                    </div>
                </main>
            </div>
        </div>
    )
}
