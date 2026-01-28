import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { User } from '@/types'

interface AuthState {
    // State
    user: User | null
    token: string | null
    isAuthenticated: boolean
    isLoading: boolean

    // Actions
    setUser: (user: User | null) => void
    setToken: (token: string | null) => void
    login: (user: User, token: string) => void
    logout: () => void
    setLoading: (loading: boolean) => void
}

export const useAuthStore = create<AuthState>()(
    persist(
        (set) => ({
            // Initial state
            user: null,
            token: null,
            isAuthenticated: false,
            isLoading: false,

            // Actions
            setUser: (user) =>
                set({ user, isAuthenticated: !!user }),

            setToken: (token) => {
                if (token) {
                    localStorage.setItem('auth_token', token)
                } else {
                    localStorage.removeItem('auth_token')
                }
                set({ token })
            },

            login: (user, token) => {
                localStorage.setItem('auth_token', token)
                set({ user, token, isAuthenticated: true, isLoading: false })
            },

            logout: () => {
                localStorage.removeItem('auth_token')
                set({ user: null, token: null, isAuthenticated: false })
            },

            setLoading: (isLoading) =>
                set({ isLoading }),
        }),
        {
            name: 'pulse-auth-store',
            partialize: (state) => ({
                user: state.user,
                token: state.token,
                isAuthenticated: state.isAuthenticated,
            }),
        }
    )
)
