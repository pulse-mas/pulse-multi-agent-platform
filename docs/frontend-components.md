# Frontend Component Library

> Documentation for the Pulse Platform UI component library.

## Overview

The Pulse Platform uses a custom component library built with React, TypeScript, and Tailwind CSS. All components follow a consistent design language with full accessibility support.

---

## Base Components

### Button

A versatile button component with multiple variants and sizes.

```tsx
import { Button } from '@/components/ui'

// Variants
<Button variant="default">Primary Action</Button>
<Button variant="secondary">Secondary Action</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="destructive">Delete</Button>
<Button variant="success">Confirm</Button>
<Button variant="link">Link Style</Button>

// Sizes
<Button size="sm">Small</Button>
<Button size="default">Default</Button>
<Button size="lg">Large</Button>
<Button size="xl">Extra Large</Button>
<Button size="icon">🔍</Button>

// Loading State
<Button isLoading>Processing...</Button>
```

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'default' \| 'secondary' \| 'destructive' \| 'outline' \| 'ghost' \| 'link' \| 'success'` | `'default'` | Visual style |
| `size` | `'sm' \| 'default' \| 'lg' \| 'xl' \| 'icon'` | `'default'` | Size variant |
| `isLoading` | `boolean` | `false` | Shows spinner and disables |

---

### Card

Container component for content sections.

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui'

<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Supporting text for the card.</CardDescription>
  </CardHeader>
  <CardContent>
    Main content goes here.
  </CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

**Subcomponents:**
- `CardHeader` - Top section for title/description
- `CardTitle` - Main heading
- `CardDescription` - Subtitle/description text
- `CardContent` - Main content area
- `CardFooter` - Bottom section for actions

---

### Badge

Small status indicators and labels.

```tsx
import { Badge } from '@/components/ui'

// Standard Variants
<Badge variant="default">Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="outline">Outline</Badge>
<Badge variant="destructive">Error</Badge>
<Badge variant="success">Success</Badge>
<Badge variant="warning">Warning</Badge>
<Badge variant="info">Info</Badge>

// Sentiment Variants (for AI/ML data)
<Badge variant="positive">Positive</Badge>
<Badge variant="neutral">Neutral</Badge>
<Badge variant="negative">Negative</Badge>
```

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | See above | `'default'` | Visual style |

---

### Input

Text input with error state support.

```tsx
import { Input } from '@/components/ui'

// Basic
<Input placeholder="Enter text..." />

// With Error
<Input error="This field is required" />

// Types
<Input type="email" placeholder="email@example.com" />
<Input type="password" placeholder="Password" />
<Input type="number" min={0} max={100} />
```

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `error` | `string` | `undefined` | Error message to display |
| `...rest` | `InputHTMLAttributes` | - | Standard input props |

---

### Textarea

Multi-line text input.

```tsx
import { Textarea } from '@/components/ui'

<Textarea 
  placeholder="Enter description..." 
  rows={4}
  error="Description is required"
/>
```

---

### Skeleton

Loading placeholder component.

```tsx
import { Skeleton } from '@/components/ui'

// Basic
<Skeleton className="h-12 w-full" />

// Card skeleton
<Skeleton className="h-32 w-full rounded-xl" />

// Multiple
{[...Array(5)].map((_, i) => (
  <Skeleton key={i} className="h-24 w-full mb-4" />
))}
```

---

## Layout Components

### Sidebar

Collapsible navigation sidebar with animated transitions.

```tsx
import { Sidebar } from '@/components/layout'

// Used in DashboardLayout
<Sidebar />
```

**Features:**
- Collapsible (72px collapsed, 256px expanded)
- Animated transitions (Framer Motion)
- Active route highlighting
- Pulse branding with gradient logo
- Bottom settings link

**Navigation Items:**
- Dashboard
- Product DNA
- Content
- Analytics
- AI Agents
- Interactions
- Brands
- Settings

---

### Header

Top navigation bar with search and user actions.

```tsx
import { Header } from '@/components/layout'

<Header 
  title="Dashboard" 
  subtitle="Welcome back!" 
/>
```

**Props:**
| Prop | Type | Description |
|------|------|-------------|
| `title` | `string` | Page title |
| `subtitle` | `string` | Optional subtitle |

**Features:**
- Responsive to sidebar collapse
- Global search input
- Notification bell with count badge
- User menu button

---

### DashboardLayout

Main layout wrapper combining Sidebar, Header, and content area.

```tsx
import { DashboardLayout } from '@/components/layout'

// Used as route element with Outlet
<Route element={<DashboardLayout />}>
  <Route path="/dashboard" element={<DashboardPage />} />
</Route>
```

---

## Usage Guidelines

### Importing Components

Always use the barrel exports for cleaner imports:

```tsx
// ✅ Good
import { Button, Card, Badge } from '@/components/ui'

// ❌ Avoid
import { Button } from '@/components/ui/button'
```

### Styling Customization

Use the `className` prop to add custom styles:

```tsx
<Card className="border-pulse-primary hover:shadow-lg">
  <CardContent className="p-8">
    Custom padding
  </CardContent>
</Card>
```

### Accessibility

All components include:
- Proper ARIA attributes
- Keyboard navigation
- Focus visible states (`focus-visible:ring-2`)
- Screen reader support

---

## Design Tokens

Reference these CSS variables in custom components:

```css
/* Colors */
var(--color-pulse-primary)     /* #6366F1 */
var(--color-pulse-secondary)   /* #8B5CF6 */
var(--color-background)        /* #0F0F0F */
var(--color-surface)           /* #1A1A1A */
var(--color-surface-elevated)  /* #242424 */
var(--color-border)            /* #333333 */
var(--color-text-primary)      /* #FAFAFA */
var(--color-text-secondary)    /* #A1A1AA */
var(--color-text-muted)        /* #71717A */

/* Semantic */
var(--color-success)           /* #10B981 */
var(--color-warning)           /* #F59E0B */
var(--color-error)             /* #EF4444 */
var(--color-info)              /* #3B82F6 */

/* Sentiment */
var(--color-sentiment-positive) /* #10B981 */
var(--color-sentiment-neutral)  /* #6B7280 */
var(--color-sentiment-negative) /* #EF4444 */

/* Border Radius */
var(--radius-sm)   /* 0.25rem */
var(--radius-md)   /* 0.5rem */
var(--radius-lg)   /* 0.75rem */
var(--radius-xl)   /* 1rem */
var(--radius-full) /* 9999px */
```
