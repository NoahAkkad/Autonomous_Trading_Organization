"""FastAPI application factory for organization-service."""

from fastapi import FastAPI

from .routers import agents, departments, organizations, permissions, ranks, relationships, roles


def create_app() -> FastAPI:
    """Create the organization-service FastAPI application."""
    app = FastAPI(
        title="ATO Organization Service",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.include_router(organizations.router)
    app.include_router(departments.router)
    app.include_router(agents.router)
    app.include_router(relationships.router)
    app.include_router(roles.router)
    app.include_router(ranks.router)
    app.include_router(permissions.router)
    return app
