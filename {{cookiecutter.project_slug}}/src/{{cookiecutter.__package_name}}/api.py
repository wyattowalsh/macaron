"""FastAPI application for {{ cookiecutter.project_name }}.

This module provides a modern REST API with:
- Automatic OpenAPI documentation
- Pydantic models for request/response validation
- Error handling
- Health checks
- Metrics
- Authentication (optional)
"""

{% if cookiecutter.include_api %}
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from loguru import logger

from .config import Config, get_default_config
from .core import hello_world, {{ cookiecutter.__package_name.title().replace('_', '') }}Error
{% if cookiecutter.include_async %}from .core import async_hello_world{% endif %}

# Pydantic models
class HealthResponse(BaseModel):
    """Health check response model."""
    status: str = Field(..., description="Health status")
    timestamp: datetime = Field(..., description="Check timestamp")
    version: str = Field(..., description="Application version")
    uptime: Optional[float] = Field(None, description="Uptime in seconds")


class GreetingRequest(BaseModel):
    """Greeting request model."""
    name: str = Field(..., min_length=1, max_length=100, description="Name to greet")
    uppercase: bool = Field(False, description="Convert greeting to uppercase")


class GreetingResponse(BaseModel):
    """Greeting response model."""
    message: str = Field(..., description="Greeting message")
    timestamp: datetime = Field(..., description="Response timestamp")


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    timestamp: datetime = Field(..., description="Error timestamp")


# App startup time for uptime calculation
app_start_time = datetime.utcnow()


def get_config() -> Config:
    """Dependency to get configuration."""
    return get_default_config()


def create_app(config: Optional[Config] = None) -> FastAPI:
    """Create and configure FastAPI application."""
    if config is None:
        config = get_default_config()
    
    # Create FastAPI app
    app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.project_description }}",
        version=config.version,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Add trusted host middleware for production
    if config.is_production():
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=[config.api_host, "localhost", "127.0.0.1"]
        )
    
    # Exception handlers
    @app.exception_handler({{ cookiecutter.__package_name.title().replace('_', '') }}Error)
    async def handle_app_error(request, exc: {{ cookiecutter.__package_name.title().replace('_', '') }}Error):
        """Handle application-specific errors."""
        logger.error(f"Application error: {exc}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=ErrorResponse(
                error=exc.__class__.__name__,
                message=str(exc),
                timestamp=datetime.utcnow()
            ).dict()
        )
    
    @app.exception_handler(ValueError)
    async def handle_value_error(request, exc: ValueError):
        """Handle value errors."""
        logger.error(f"Value error: {exc}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ErrorResponse(
                error="ValidationError",
                message=str(exc),
                timestamp=datetime.utcnow()
            ).dict()
        )
    
    # Routes
    @app.get("/health", response_model=HealthResponse, tags=["Health"])
    async def health_check(config: Config = Depends(get_config)):
        """Health check endpoint."""
        uptime = (datetime.utcnow() - app_start_time).total_seconds()
        
        return HealthResponse(
            status="healthy",
            timestamp=datetime.utcnow(),
            version=config.version,
            uptime=uptime
        )
    
    @app.get("/", tags=["Root"])
    async def root():
        """Root endpoint."""
        return {
            "message": "Welcome to {{ cookiecutter.project_name }}",
            "docs": "/docs",
            "health": "/health"
        }
    
    @app.post("/greet", response_model=GreetingResponse, tags=["Greetings"])
    async def greet(request: GreetingRequest):
        """Generate a greeting message."""
        try:
            message = hello_world(request.name)
            if request.uppercase:
                message = message.upper()
            
            return GreetingResponse(
                message=message,
                timestamp=datetime.utcnow()
            )
        except Exception as e:
            logger.error(f"Error generating greeting: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate greeting"
            )
    
    {% if cookiecutter.include_async %}
    @app.post("/async-greet", response_model=GreetingResponse, tags=["Greetings"])
    async def async_greet(request: GreetingRequest):
        """Generate a greeting message asynchronously."""
        try:
            message = await async_hello_world(request.name)
            if request.uppercase:
                message = message.upper()
            
            return GreetingResponse(
                message=message,
                timestamp=datetime.utcnow()
            )
        except Exception as e:
            logger.error(f"Error generating async greeting: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate async greeting"
            )
    {% endif %}
    
    @app.get("/info", tags=["Info"])
    async def app_info(config: Config = Depends(get_config)):
        """Get application information."""
        return {
            "name": config.app_name,
            "version": config.version,
            "environment": config.environment,
            "debug": config.debug,
            "uptime": (datetime.utcnow() - app_start_time).total_seconds()
        }
    
    # Startup event
    @app.on_event("startup")
    async def startup_event():
        """Application startup event."""
        logger.info(f"Starting {{ cookiecutter.project_name }} API v{config.version}")
        logger.info(f"Environment: {config.environment}")
        logger.info(f"Debug mode: {config.debug}")
    
    # Shutdown event
    @app.on_event("shutdown")
    async def shutdown_event():
        """Application shutdown event."""
        logger.info("Shutting down {{ cookiecutter.project_name }} API")
    
    return app


# Create default app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    from .config import get_default_config
    
    config = get_default_config()
    uvicorn.run(
        "{{ cookiecutter.__package_name }}.api:app",
        host=config.api_host,
        port=config.api_port,
        reload=config.api_reload,
        workers=config.api_workers if not config.api_reload else 1,
        log_level=config.log_level.lower(),
    )
{% else %}
# API module placeholder when FastAPI is not included
def create_app():
    """Placeholder when API is not enabled."""
    raise NotImplementedError("API functionality not included in this configuration")

app = None
{% endif %}