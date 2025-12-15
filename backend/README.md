# Pulse Platform - Backend API

FastAPI backend for the Pulse Multi-Agent Social Media Platform.

## Features

- ✅ **FastAPI** - Modern, fast web framework
- ✅ **Clean Architecture** - Organized directory structure with separation of concerns
- ✅ **Pydantic Settings** - Environment-based configuration management
- ✅ **Loguru Logging** - Structured logging with rotation and JSON support
- ✅ **CORS Support** - Configurable cross-origin resource sharing
- ✅ **Exception Handling** - Custom error handlers with detailed responses
- ✅ **Health Checks** - `/health` and `/api/v1/status` endpoints
- ✅ **OpenAPI Docs** - Auto-generated Swagger UI and ReDoc

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Pydantic settings configuration
│   ├── routers/
│   │   ├── health.py        # Health check endpoints
│   │   └── status.py        # System status endpoint
│   ├── models/
│   │   └── responses.py     # Pydantic response models
│   ├── services/
│   │   └── system.py        # System info service
│   ├── middleware/
│   │   └── cors.py          # CORS configuration
│   ├── exceptions/
│   │   └── handlers.py      # Custom exception handlers
│   └── utils/
│       └── logging.py       # Loguru logging setup
├── tests/
│   └── test_health.py       # Health endpoint tests
├── .env.template            # Environment template
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Setup

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the template and configure your environment variables:

```bash
cp .env.template .env
```

Edit `.env` and set your configuration:
- Set `OPENAI_API_KEY` if you have one (optional for now)
- Adjust `CORS_ORIGINS` for your frontend URLs
- Set `LOG_LEVEL` (DEBUG, INFO, WARNING, ERROR)

### 4. Run the Server

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Root
- **GET /** - API information and links

### Health
- **GET /health** - Simple health check
  - Returns: `{"status": "healthy", "timestamp": "..."}`

### Status
- **GET /api/v1/status** - Detailed system information
  - Returns: App name, version, Python version, uptime, environment, dependencies

### Documentation
- **GET /docs** - Swagger UI (interactive API documentation)
- **GET /redoc** - ReDoc (alternative documentation)
- **GET /openapi.json** - OpenAPI schema

## Testing

### Manual Testing

Start the server and test endpoints:

```bash
# Terminal 1: Start server
uvicorn app.main:app --reload

# Terminal 2: Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/status
```

Or visit in your browser:
- http://localhost:8000/docs - Interactive API documentation
- http://localhost:8000/health - Health check
- http://localhost:8000/api/v1/status - System status

### Automated Tests

Run the test suite:

```bash
pytest tests/ -v
```

## Development

### Adding New Endpoints

1. Create a new router in `app/routers/`
2. Define Pydantic models in `app/models/`
3. Implement business logic in `app/services/`
4. Register the router in `app/main.py`

### Environment Variables

All configuration is managed through Pydantic Settings in `app/config.py`. Add new settings by:

1. Add field to `Settings` class
2. Update `.env.template`
3. Document in this README

## Next Steps (Sprint 1)

- [ ] MongoDB integration for data persistence
- [ ] Redis caching layer
- [ ] JWT authentication
- [ ] User management endpoints
- [ ] Content creation endpoints
- [ ] WebSocket support

## License

Part of the Pulse Multi-Agent Platform graduation project.
