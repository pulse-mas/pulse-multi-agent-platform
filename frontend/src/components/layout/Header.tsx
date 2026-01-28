import { Bell, Search, User } from 'lucide-react'
import { Button } from '@/components/ui'
import { cn } from '@/lib/utils'
import { useUIStore } from '@/stores'

interface HeaderProps {
    title?: string
    subtitle?: string
}

export function Header({ title, subtitle }: HeaderProps) {
    const { sidebarCollapsed } = useUIStore()

    return (
        <header
            className={cn(
                'fixed top-0 right-0 z-30 h-16 border-b border-border bg-surface/80 backdrop-blur-md transition-all duration-200',
                sidebarCollapsed ? 'left-[72px]' : 'left-64'
            )}
        >
            <div className="flex h-full items-center justify-between px-6">
                {/* Left - Page Title */}
                <div>
                    {title && (
                        <h1 className="text-xl font-semibold text-text-primary">{title}</h1>
                    )}
                    {subtitle && (
                        <p className="text-sm text-text-secondary">{subtitle}</p>
                    )}
                </div>

                {/* Right - Actions */}
                <div className="flex items-center gap-4">
                    {/* Search */}
                    <div className="relative hidden md:block">
                        <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-text-muted" />
                        <input
                            type="text"
                            placeholder="Search..."
                            className="h-9 w-64 rounded-lg border border-border bg-background pl-9 pr-4 text-sm text-text-primary placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-pulse-primary transition-all"
                        />
                    </div>

                    {/* Notifications */}
                    <Button variant="ghost" size="icon" className="relative">
                        <Bell className="h-5 w-5" />
                        <span className="absolute -right-1 -top-1 flex h-4 w-4 items-center justify-center rounded-full bg-error text-[10px] font-bold text-white">
                            3
                        </span>
                    </Button>

                    {/* User Menu */}
                    <Button variant="ghost" size="icon" className="rounded-full">
                        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-pulse-primary/20">
                            <User className="h-4 w-4 text-pulse-primary" />
                        </div>
                    </Button>
                </div>
            </div>
        </header>
    )
}
