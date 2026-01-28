import * as React from 'react'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const badgeVariants = cva(
    'inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-pulse-primary focus:ring-offset-2',
    {
        variants: {
            variant: {
                default:
                    'border-transparent bg-pulse-primary text-white',
                secondary:
                    'border-transparent bg-pulse-secondary text-white',
                destructive:
                    'border-transparent bg-error text-white',
                outline:
                    'border-border text-text-secondary',
                success:
                    'border-transparent bg-success text-white',
                warning:
                    'border-transparent bg-warning text-white',
                info:
                    'border-transparent bg-info text-white',
                // Sentiment variants
                positive:
                    'border-transparent bg-sentiment-positive/20 text-sentiment-positive',
                neutral:
                    'border-transparent bg-sentiment-neutral/20 text-sentiment-neutral',
                negative:
                    'border-transparent bg-sentiment-negative/20 text-sentiment-negative',
            },
        },
        defaultVariants: {
            variant: 'default',
        },
    }
)

export interface BadgeProps
    extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> { }

function Badge({ className, variant, ...props }: BadgeProps) {
    return (
        <div className={cn(badgeVariants({ variant }), className)} {...props} />
    )
}

export { Badge, badgeVariants }
