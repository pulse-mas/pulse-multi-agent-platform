import { lazy, Suspense } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { DashboardLayout } from '@/components/layout'
import { ROUTES } from '@/lib/constants'

// Lazy load pages for code splitting
const DashboardPage = lazy(() =>
  import('@/features/dashboard').then((m) => ({ default: m.DashboardPage }))
)
const ProductDNAPage = lazy(() =>
  import('@/features/product-dna').then((m) => ({ default: m.ProductDNAPage }))
)
const ContentPage = lazy(() =>
  import('@/features/content').then((m) => ({ default: m.ContentPage }))
)
const AnalyticsPage = lazy(() =>
  import('@/features/analytics').then((m) => ({ default: m.AnalyticsPage }))
)
const AgentsPage = lazy(() =>
  import('@/features/agents').then((m) => ({ default: m.AgentsPage }))
)
const InteractionsPage = lazy(() =>
  import('@/features/interactions').then((m) => ({ default: m.InteractionsPage }))
)
const BrandsPage = lazy(() =>
  import('@/features/brands').then((m) => ({ default: m.BrandsPage }))
)
const SettingsPage = lazy(() =>
  import('@/features/settings').then((m) => ({ default: m.SettingsPage }))
)

// Create Query Client with defaults
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30000, // 30 seconds
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
})

// Loading fallback
function PageLoader() {
  return (
    <div className="flex h-[50vh] items-center justify-center">
      <div className="flex flex-col items-center gap-4">
        <div className="h-10 w-10 animate-spin rounded-full border-4 border-pulse-primary border-t-transparent" />
        <p className="text-text-secondary">Loading...</p>
      </div>
    </div>
  )
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          {/* Redirect root to dashboard */}
          <Route path="/" element={<Navigate to={ROUTES.DASHBOARD} replace />} />

          {/* Dashboard Layout */}
          <Route element={<DashboardLayout />}>
            <Route
              path={ROUTES.DASHBOARD}
              element={
                <Suspense fallback={<PageLoader />}>
                  <DashboardPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.PRODUCT_DNA}
              element={
                <Suspense fallback={<PageLoader />}>
                  <ProductDNAPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.CONTENT}
              element={
                <Suspense fallback={<PageLoader />}>
                  <ContentPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.ANALYTICS}
              element={
                <Suspense fallback={<PageLoader />}>
                  <AnalyticsPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.AGENTS}
              element={
                <Suspense fallback={<PageLoader />}>
                  <AgentsPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.INTERACTIONS}
              element={
                <Suspense fallback={<PageLoader />}>
                  <InteractionsPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.BRANDS}
              element={
                <Suspense fallback={<PageLoader />}>
                  <BrandsPage />
                </Suspense>
              }
            />
            <Route
              path={ROUTES.SETTINGS}
              element={
                <Suspense fallback={<PageLoader />}>
                  <SettingsPage />
                </Suspense>
              }
            />
          </Route>

          {/* 404 Fallback */}
          <Route
            path="*"
            element={
              <div className="flex h-screen items-center justify-center bg-background">
                <div className="text-center">
                  <h1 className="text-6xl font-bold text-text-primary">404</h1>
                  <p className="mt-4 text-text-secondary">Page not found</p>
                  <a
                    href={ROUTES.DASHBOARD}
                    className="mt-6 inline-block text-pulse-primary hover:underline"
                  >
                    Go to Dashboard
                  </a>
                </div>
              </div>
            }
          />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
