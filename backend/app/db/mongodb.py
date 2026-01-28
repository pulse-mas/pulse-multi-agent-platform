"""MongoDB database connection and utilities."""

from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config import settings


class MongoDB:
    """MongoDB connection manager using Motor (async driver)."""

    def __init__(self):
        self._client: AsyncIOMotorClient | None = None
        self._db: AsyncIOMotorDatabase | None = None

    async def connect(self) -> None:
        """Establish connection to MongoDB."""
        if self._client is None:
            try:
                self._client = AsyncIOMotorClient(settings.MONGODB_URI)
                self._db = self._client[settings.MONGODB_DB_NAME]

                # Verify connection
                await self._client.admin.command("ping")
                logger.info(f"Connected to MongoDB: {settings.MONGODB_DB_NAME}")

            except Exception as e:
                logger.error(f"Failed to connect to MongoDB: {e}")
                raise

    async def disconnect(self) -> None:
        """Close MongoDB connection."""
        if self._client is not None:
            self._client.close()
            self._client = None
            self._db = None
            logger.info("Disconnected from MongoDB")

    @property
    def client(self) -> AsyncIOMotorClient:
        """Get the MongoDB client."""
        if self._client is None:
            raise RuntimeError("MongoDB not connected. Call connect() first.")
        return self._client

    @property
    def db(self) -> AsyncIOMotorDatabase:
        """Get the database instance."""
        if self._db is None:
            raise RuntimeError("MongoDB not connected. Call connect() first.")
        return self._db

    def get_collection(self, name: str):
        """Get a collection by name."""
        return self.db[name]


# Singleton instance
mongodb = MongoDB()


async def get_database() -> AsyncIOMotorDatabase:
    """Dependency to get database instance."""
    if mongodb._db is None:
        await mongodb.connect()
    return mongodb.db
