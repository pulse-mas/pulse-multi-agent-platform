import { Link, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
    LayoutDashboard,
    Database,
    FileText,
    BarChart3,
    Bot,
    MessageSquare,
    Building2,
    Settings,
    ChevronLeft,
    ChevronRight,
} from 'lucide-react'
import { cn } from '@/lib/utils'
import { useUIStore } from '@/stores'
import { ROUTES } from '@/lib/constants'

interface NavItem {
    icon: React.ElementType
    label: string
    href: string
    badge?: number
}

const navItems: NavItem[] = [
    { icon: LayoutDashboard, label: 'Dashboard', href: ROUTES.DASHBOARD },
    { icon: Database, label: 'Product DNA', href: ROUTES.PRODUCT_DNA },
    { icon: FileText, label: 'Content', href: ROUTES.CONTENT },
    { icon: BarChart3, label: 'Analytics', href: ROUTES.ANALYTICS },
    { icon: Bot, label: 'AI Agents', href: ROUTES.AGENTS },
    { icon: MessageSquare, label: 'Interactions', href: ROUTES.INTERACTIONS },
    { icon: Building2, label: 'Brands', href: ROUTES.BRANDS },
]

const bottomNavItems: NavItem[] = [
    { icon: Settings, label: 'Settings', href: ROUTES.SETTINGS },
]

export function Sidebar() {
    const location = useLocation()
    const { sidebarCollapsed, setSidebarCollapsed } = useUIStore()

    return (
        <motion.aside
            initial={false}
            animate={{ width: sidebarCollapsed ? 72 : 256 }}
            transition={{ duration: 0.2, ease: 'easeInOut' }}
            className="fixed left-0 top-0 z-40 h-screen border-r border-border bg-surface flex flex-col"
        >
            {/* Logo */}
            <div className="flex h-16 items-center justify-between px-4 border-b border-border">
                <Link to={ROUTES.DASHBOARD} className="flex items-center gap-3">
                    <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-pulse-primary to-pulse-secondary">
                        <span className="text-lg font-bold text-white">P</span>
                    </div>
                    {!sidebarCollapsed && (
                        <motion.span
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="text-xl font-bold gradient-text"
                        >
                            Pulse
                        </motion.span>
                    )}
                </Link>
            </div>

            {/* Navigation */}
            <nav className="flex-1 overflow-y-auto py-4">
                <ul className="space-y-1 px-3">
                    {navItems.map((item) => {
                        const isActive = location.pathname.startsWith(item.href)
                        return (
                            <li key={item.href}>
                                <Link
                                    to={item.href}
                                    className={cn(
                                        'flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all duration-200',
                                        isActive
                                            ? 'bg-pulse-primary/10 text-pulse-primary'
                                            : 'text-text-secondary hover:bg-surface-elevated hover:text-text-primary'
                                    )}
                                >
                                    <item.icon className={cn('h-5 w-5 shrink-0', isActive && 'text-pulse-primary')} />
                                    {!sidebarCollapsed && (
                                        <motion.span
                                            initial={{ opacity: 0 }}
                                            animate={{ opacity: 1 }}
                                            exit={{ opacity: 0 }}
                                        >
                                            {item.label}
                                        </motion.span>
                                    )}
                                    {!sidebarCollapsed && item.badge !== undefined && (
                                        <span className="ml-auto flex h-5 w-5 items-center justify-center rounded-full bg-pulse-primary text-xs text-white">
                                            {item.badge}
                                        </span>
                                    )}
                                </Link>
                            </li>
                        )
                    })}
                </ul>
            </nav>

            {/* Bottom Navigation */}
            <div className="border-t border-border py-4">
                <ul className="space-y-1 px-3">
                    {bottomNavItems.map((item) => {
                        const isActive = location.pathname.startsWith(item.href)
                        return (
                            <li key={item.href}>
                                <Link
                                    to={item.href}
                                    className={cn(
                                        'flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all duration-200',
                                        isActive
                                            ? 'bg-pulse-primary/10 text-pulse-primary'
                                            : 'text-text-secondary hover:bg-surface-elevated hover:text-text-primary'
                                    )}
                                >
                                    <item.icon className="h-5 w-5 shrink-0" />
                                    {!sidebarCollapsed && <span>{item.label}</span>}
                                </Link>
                            </li>
                        )
                    })}
                </ul>

                {/* Collapse Toggle */}
                <div className="px-3 mt-4">
                    <button
                        onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
                        className="flex w-full items-center justify-center gap-2 rounded-lg px-3 py-2 text-sm text-text-muted hover:bg-surface-elevated hover:text-text-primary transition-colors"
                    >
                        {sidebarCollapsed ? (
                            <ChevronRight className="h-5 w-5" />
                        ) : (
                            <>
                                <ChevronLeft className="h-5 w-5" />
                                <span>Collapse</span>
                            </>
                        )}
                    </button>
                </div>
            </div>
        </motion.aside>
    )
}
