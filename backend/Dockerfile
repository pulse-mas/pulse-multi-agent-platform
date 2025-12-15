# Multi-stage Dockerfile for Pulse Platform Backend

# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim

# Add labels for metadata
LABEL org.opencontainers.image.title="Pulse Platform Backend"
LABEL org.opencontainers.image.description="AI-Powered Multi-Agent Social Media Platform API"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.source="https://github.com/pulse-platform/pulse-multi-agent-platform"

# Create non-root user for security
RUN groupadd --gid 1000 pulse \
    && useradd --uid 1000 --gid pulse --shell /bin/bash --create-home pulse

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/pulse/.local

# Copy application code
COPY --chown=pulse:pulse ./app ./app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH=/home/pulse/.local/bin:$PATH

# Switch to non-root user
USER pulse

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
