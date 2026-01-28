import { create } from 'zustand'
import { persist } from 'zustand/middleware'

type Theme = 'light' | 'dark' | 'system'

interface UIState {
    // Sidebar
    sidebarOpen: boolean
    sidebarCollapsed: boolean

    // Theme
    theme: Theme

    // Modal
    activeModal: string | null
    modalData: unknown

    // Actions
    toggleSidebar: () => void
    setSidebarCollapsed: (collapsed: boolean) => void
    setTheme: (theme: Theme) => void
    openModal: (modalId: string, data?: unknown) => void
    closeModal: () => void
}

export const useUIStore = create<UIState>()(
    persist(
        (set) => ({
            // Initial state
            sidebarOpen: true,
            sidebarCollapsed: false,
            theme: 'dark',
            activeModal: null,
            modalData: null,

            // Actions
            toggleSidebar: () =>
                set((state) => ({ sidebarOpen: !state.sidebarOpen })),

            setSidebarCollapsed: (collapsed) =>
                set({ sidebarCollapsed: collapsed }),

            setTheme: (theme) => {
                // Apply theme to document
                const root = document.documentElement
                if (theme === 'system') {
                    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches
                        ? 'dark'
                        : 'light'
                    root.classList.toggle('dark', systemTheme === 'dark')
                } else {
                    root.classList.toggle('dark', theme === 'dark')
                }
                set({ theme })
            },

            openModal: (modalId, data) =>
                set({ activeModal: modalId, modalData: data }),

            closeModal: () =>
                set({ activeModal: null, modalData: null }),
        }),
        {
            name: 'pulse-ui-store',
            partialize: (state) => ({
                theme: state.theme,
                sidebarCollapsed: state.sidebarCollapsed,
            }),
        }
    )
)
