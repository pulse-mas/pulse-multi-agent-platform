# Pulse Platform Frontend

> A modern, premium React frontend for the Pulse AI-Powered Multi-Agent Social Media Platform.

[![React](https://img.shields.io/badge/React-18.x-61DAFB?logo=react)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?logo=typescript)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4?logo=tailwindcss)](https://tailwindcss.com)
[![Vite](https://img.shields.io/badge/Vite-7.x-646CFF?logo=vite)](https://vitejs.dev)

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ (recommended: 22+)
- **npm** 8+
- Backend running on `http://localhost:8000`

### Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at **http://localhost:3000**

---

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── ui/             # Base components (Button, Card, Badge, Input)
│   │   └── layout/         # Layout components (Sidebar, Header)
│   │
│   ├── features/           # Feature-based modules
│   │   ├── dashboard/      # Dashboard with stats and overview
│   │   ├── product-dna/    # Product DNA collection (fully implemented)
│   │   ├── analytics/      # Analytics dashboard
│   │   ├── content/        # Content management
│   │   ├── agents/         # AI agents hub
│   │   ├── interactions/   # Customer interactions
│   │   ├── brands/         # Brand management
│   │   └── settings/       # Platform settings
│   │
│   ├── lib/                # Utilities and API
│   │   ├── api/            # Axios client and endpoints
│   │   ├── utils.ts        # Helper functions
│   │   └── constants.ts    # App constants and routes
│   │
│   ├── stores/             # Zustand state stores
│   │   ├── authStore.ts    # Authentication state
│   │   └── uiStore.ts      # UI state (sidebar, theme)
│   │
│   ├── types/              # TypeScript type definitions
│   ├── App.tsx             # Main app with routing
│   ├── main.tsx            # Entry point
│   └── index.css           # Global styles and theme
│
├── index.html              # HTML template
├── vite.config.ts          # Vite configuration
├── tsconfig.app.json       # TypeScript configuration
└── package.json            # Dependencies and scripts
```

---

## 🎨 Design System

### Theme

The frontend uses a **dark-mode-first** design with a premium aesthetic:

| Token | Value | Usage |
|-------|-------|-------|
| `pulse-primary` | `#6366F1` | Primary brand color (Indigo) |
| `pulse-secondary` | `#8B5CF6` | Secondary brand color (Purple) |
| `pulse-accent` | `#EC4899` | Accent highlights (Pink) |
| `success` | `#10B981` | Positive sentiment, success states |
| `warning` | `#F59E0B` | Warning states |
| `error` | `#EF4444` | Negative sentiment, errors |

### Typography

- **Primary Font**: Inter (Google Fonts)
- **Monospace Font**: JetBrains Mono

### Components

All UI components support variants and are built with accessibility in mind:

```tsx
// Button variants
<Button variant="default" />  // Primary purple
<Button variant="secondary" />
<Button variant="outline" />
<Button variant="ghost" />
<Button variant="destructive" />

// Badge variants (including sentiment)
<Badge variant="positive" />  // Green for positive sentiment
<Badge variant="neutral" />   // Gray for neutral
<Badge variant="negative" />  // Red for negative
```

---

## 🔌 API Integration

The frontend connects to the FastAPI backend via Axios with automatic request/response interceptors.

### Configured Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/v1/status` | GET | System status |
| `/api/v1/product-dna/collect` | POST | Trigger data collection |
| `/api/v1/product-dna/` | GET | List enriched posts |
| `/api/v1/product-dna/stats` | GET | Get collection statistics |

### API Client Usage

```typescript
import { productDnaApi } from '@/lib/api'

// Collect new data
const result = await productDnaApi.collect({
  keywords: ['social media', 'marketing'],
  subreddits: ['marketing', 'socialmedia'],
  limit: 20,
  time_filter: 'week'
})

// Get posts with filters
const posts = await productDnaApi.list({
  sentiment: 'positive',
  limit: 50
})
```

---

## 📜 Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server on port 3000 |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run lint` | Run ESLint |

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Framework** | React 18 |
| **Language** | TypeScript 5.9 |
| **Build Tool** | Vite 7 |
| **Styling** | Tailwind CSS 4 |
| **State (Server)** | TanStack Query 5 |
| **State (Client)** | Zustand 5 |
| **Routing** | React Router 7 |
| **Forms** | React Hook Form 7 |
| **HTTP Client** | Axios |
| **Animations** | Framer Motion |
| **Icons** | Lucide React |
| **Charts** | Recharts 3 |

---

## 📊 Features Status

| Feature | Status | Description |
|---------|--------|-------------|
| Dashboard | ✅ Complete | Stats, sentiment overview, system status |
| Product DNA | ✅ Complete | Collection, listing, filtering |
| Analytics | 🔜 Placeholder | Advanced charts and predictions |
| Content | 🔜 Placeholder | Post scheduling and calendar |
| AI Agents | ⏳ Partial | Agent cards displayed |
| Interactions | 🔜 Placeholder | Customer message inbox |
| Brands | 🔜 Placeholder | Brand profile management |
| Settings | 🔜 Placeholder | User and app settings |

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file for custom configuration:

```env
VITE_API_URL=http://localhost:8000
```

### Backend Proxy

The Vite dev server automatically proxies `/api` requests to the backend:

```typescript
// vite.config.ts
server: {
  port: 3000,
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
    },
  },
}
```

---

## 📝 Development Guidelines

### File Naming

- **Components**: PascalCase (`Button.tsx`, `DashboardPage.tsx`)
- **Utilities**: camelCase (`utils.ts`, `constants.ts`)
- **Types**: PascalCase (`api.ts` exports `EnrichedPost`, `Sentiment`)

### Import Aliases

Use the `@/` alias for clean imports:

```typescript
import { Button } from '@/components/ui'
import { useAuthStore } from '@/stores'
import { productDnaApi } from '@/lib/api'
```

### State Management

- **Server State**: Use TanStack Query for all API data
- **Client State**: Use Zustand for UI state (sidebar, modals)
- **Form State**: Use React Hook Form for forms

---

## 📄 License

This project is part of the Pulse Multi-Agent Platform graduation project.
