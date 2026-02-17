"""
Configuration management for TaskFlow API
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    
    # Server
    PORT: int = 8000
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    
    # Redis
    REDIS_URL: str
    REDIS_PASSWORD: str
    REDIS_DB: int = 0
    
    # Authentication
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # External Services
    SENDGRID_API_KEY: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET: str
    AWS_REGION: str = "us-east-1"
    
    # Webhooks
    WEBHOOK_SECRET: str
    WEBHOOK_TIMEOUT: int = 30
    
    # API Keys
    STRIPE_API_KEY: str
    OPENAI_API_KEY: str
    
    # Monitoring
    SENTRY_DSN: str
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    """Get cached settings instance"""
    return Settings()