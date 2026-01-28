"""Tests for health and status endpoints."""

import pytest


@pytest.mark.asyncio
async def test_health_endpoint_returns_200(client):
    """Test that /health returns HTTP 200."""
    response = await client.get("/health")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_endpoint_returns_healthy_status(client):
    """Test that /health returns status: healthy."""
    response = await client.get("/health")
    data = response.json()

    assert "status" in data
    assert data["status"] == "healthy"
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_status_endpoint_returns_200(client):
    """Test that /api/v1/status returns HTTP 200."""
    response = await client.get("/api/v1/status")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_status_contains_app_info(client):
    """Test that /api/v1/status contains required information."""
    response = await client.get("/api/v1/status")
    data = response.json()

    # Verify required fields
    assert "app_name" in data
    assert "version" in data
    assert "python_version" in data
    assert "uptime_seconds" in data
    assert "environment" in data
    assert "dependencies" in data

    # Verify values
    assert data["app_name"] == "Pulse Platform"
    assert data["version"] == "0.1.0"
    assert isinstance(data["uptime_seconds"], (int, float))
    assert data["uptime_seconds"] >= 0


@pytest.mark.asyncio
async def test_root_endpoint(client):
    """Test that root endpoint returns API information."""
    response = await client.get("/")
    data = response.json()

    assert response.status_code == 200
    assert "message" in data
    assert "version" in data
    assert "docs" in data


@pytest.mark.asyncio
async def test_openapi_docs_available(client):
    """Test that OpenAPI documentation is accessible."""
    # Test Swagger UI
    response = await client.get("/docs")
    assert response.status_code == 200

    # Test ReDoc
    response = await client.get("/redoc")
    assert response.status_code == 200

    # Test OpenAPI schema
    response = await client.get("/openapi.json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
