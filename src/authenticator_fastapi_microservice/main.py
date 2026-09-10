from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import Base, engine
from app.routes.auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

# Initializes the FastAPI application with metadata, including title, description, version, and lifespan context manager for database setup.

authenticator = FastAPI(
    title="Authentication Microservice",
    description="Secure user onboarding and authentication service.",
    version="1.0.0",
    lifespan=lifespan,
)

# Links app entry point to the authentication router, enabling the defined endpoints for user registration and authentication.

authenticator.include_router(auth_router)

# Checks router run status with a simple GET request

@authenticator.get("/health")
def health_check():
    return {"status": "healthy"}