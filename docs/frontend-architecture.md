# Pulse Platform Frontend Architecture

> Technical architecture documentation for the Pulse Platform React frontend.

## Overview

The Pulse Platform frontend is a modern, single-page application (SPA) built with React 18 and TypeScript. It provides a premium, dark-mode-first user interface for managing AI-powered social media operations.

---

## Architecture Principles

### 1. Feature-Based Organization

The codebase follows a **feature-based architecture** where each major feature is self-contained:

```
src/features/
├── dashboard/           # Dashboard feature
│   ├── DashboardPage.tsx
│   ├── components/      # Feature-specific components
│   ├── hooks/           # Feature-specific hooks
│   └── index.ts         # Public exports
```

**Benefits:**
- Clear separation of concerns
- Easy to locate related code
- Simplified testing and maintenance
- Better code splitting opportunities

### 2. Layered Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        UI Layer                              │
│  (components/ui, components/layout, features/*/components)   │
├─────────────────────────────────────────────────────────────┤
│                     Feature Layer                            │
│           (features/*Page.tsx, feature logic)                │
├─────────────────────────────────────────────────────────────┤
│                     State Layer                              │
│         (TanStack Query, Zustand stores)                     │
├─────────────────────────────────────────────────────────────┤
│                     API Layer                                │
│              (lib/api/client.ts, endpoints.ts)               │
├─────────────────────────────────────────────────────────────┤
│                     Type Layer                               │
│                    (types/api.ts)                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Core Technologies

### React 18+

- **Concurrent Features**: Suspense for code splitting
- **Strict Mode**: Enabled for development
- **Functional Components**: All components use hooks

### TypeScript 5.9

- **Strict Mode**: Enabled (`strict: true`)
- **Path Aliases**: `@/*` maps to `src/*`
- **Type-Only Imports**: Used for cleaner compilation

### Vite 7

- **Fast HMR**: Hot module replacement
- **Code Splitting**: Automatic chunking
- **API Proxy**: Development proxy to backend

---

## State Management Strategy

### Server State: TanStack Query

All data from the API is managed by TanStack Query for:
- Automatic caching
- Background refetching
- Optimistic updates
- Loading/error states

```typescript
// Query for fetching data
const { data, isLoading } = useQuery({
  queryKey: ['product-dna', 'stats'],
  queryFn: () => productDnaApi.getStats(),
})

// Mutation for modifying data
const mutation = useMutation({
  mutationFn: productDnaApi.collect,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['product-dna'] })
  },
})
```

### Client State: Zustand

UI-specific state that doesn't come from the server:

```typescript
// UI Store
const useUIStore = create<UIState>((set) => ({
  sidebarCollapsed: false,
  theme: 'dark',
  setSidebarCollapsed: (collapsed) => set({ sidebarCollapsed: collapsed }),
}))

// Auth Store  
const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: null,
  login: (user, token) => set({ user, token, isAuthenticated: true }),
  logout: () => set({ user: null, token: null, isAuthenticated: false }),
}))
```

### Why This Split?

| State Type | Technology | Examples |
|------------|------------|----------|
| Server State | TanStack Query | API data, posts, stats |
| Client State | Zustand | Sidebar, theme, modals |
| Form State | React Hook Form | Input values, validation |
| URL State | React Router | Current page, query params |

---

## Component Architecture

### Component Hierarchy

```
App
├── QueryClientProvider (TanStack Query)
└── BrowserRouter
    ├── DashboardLayout
    │   ├── Sidebar
    │   ├── Header
    │   └── Outlet (Page Content)
    │       ├── DashboardPage
    │       ├── ProductDNAPage
    │       └── ...other pages
    └── 404 Page
```

### UI Component Design

Components use **Compound Variants** via `class-variance-authority`:

```typescript
const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-all',
  {
    variants: {
      variant: {
        default: 'bg-pulse-primary text-white',
        outline: 'border border-border bg-transparent',
        ghost: 'hover:bg-surface-elevated',
      },
      size: {
        sm: 'h-8 px-3 text-xs',
        default: 'h-10 px-4',
        lg: 'h-12 px-6 text-base',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)
```

---

## API Integration

### Client Architecture

```typescript
// Singleton Axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
})

// Request Interceptor: Add auth token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Response Interceptor: Handle errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
    }
    return Promise.reject(error)
  }
)
```

### Endpoint Organization

```typescript
// Grouped by feature
export const productDnaApi = {
  collect: (data) => post('/api/v1/product-dna/collect', data),
  list: (params) => get('/api/v1/product-dna/', { params }),
  getStats: () => get('/api/v1/product-dna/stats'),
}
```

---

## Routing Strategy

### Lazy Loading

All feature pages are lazy-loaded for optimal bundle splitting:

```typescript
const DashboardPage = lazy(() =>
  import('@/features/dashboard').then(m => ({ default: m.DashboardPage }))
)
```

### Route Structure

| Path | Component | Description |
|------|-----------|-------------|
| `/` | Redirect | → `/dashboard` |
| `/dashboard` | DashboardPage | Main overview |
| `/product-dna` | ProductDNAPage | DNA collection |
| `/content` | ContentPage | Content management |
| `/analytics` | AnalyticsPage | Analytics dashboard |
| `/agents` | AgentsPage | AI agents hub |
| `/interactions` | InteractionsPage | Customer inbox |
| `/brands` | BrandsPage | Brand profiles |
| `/settings` | SettingsPage | Platform settings |
| `*` | 404 Page | Not found |

---

## Styling Architecture

### Design Tokens

Custom CSS variables defined in `index.css`:

```css
@theme {
  --color-pulse-primary: #6366F1;
  --color-background: #0F0F0F;
  --color-surface: #1A1A1A;
  --color-text-primary: #FAFAFA;
  --color-sentiment-positive: #10B981;
}
```

### Utility Classes

Using Tailwind CSS with custom utilities:

```css
/* Glassmorphism */
.glass {
  background: rgba(26, 26, 26, 0.8);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Gradient text */
.gradient-text {
  background: linear-gradient(135deg, var(--color-pulse-primary), var(--color-pulse-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Performance Considerations

### Bundle Optimization

- **Code Splitting**: Each feature is a separate chunk
- **Tree Shaking**: Unused exports are eliminated
- **Dynamic Imports**: Large libraries loaded on demand

### Runtime Performance

- **React.memo**: Used for expensive components
- **useMemo/useCallback**: Optimized where beneficial
- **Virtual Lists**: For large data sets (future)

### Current Bundle Size

```
Total: ~135 KB gzipped
├── React/ReactDOM: ~45 KB
├── TanStack Query: ~12 KB
├── Framer Motion: ~35 KB
├── Application Code: ~43 KB
```

---

## Security Considerations

### Authentication

- JWT tokens stored in localStorage
- Auto-logout on 401 responses
- Token refresh mechanism (planned)

### XSS Prevention

- React's built-in escaping
- No `dangerouslySetInnerHTML` usage
- Content Security Policy (planned)

### API Security

- CORS configured on backend
- Request timeouts (30s)
- Error message sanitization

---

## Testing Strategy (Planned)

| Layer | Tool | Focus |
|-------|------|-------|
| Unit | Vitest | Utilities, hooks |
| Component | React Testing Library | UI components |
| Integration | Vitest + MSW | Feature flows |
| E2E | Playwright | Critical paths |

---

## Future Enhancements

1. **PWA Support**: Service worker for offline capability
2. **Real-time Updates**: WebSocket for agent status
3. **Internationalization**: i18n support
4. **Advanced Charts**: D3.js visualizations
5. **E2E Testing**: Playwright test suite
