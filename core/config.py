import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Optional
load_dotenv()


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_TRUST_HOST: str = os.getenv("APP_TRUST_HOST", "0.0.0.0")
    APP_PORT: int = os.getenv("APP_PORT", "8000")
    WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "fastapi")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    SENTRY_SDN: Optional[str] = None
    CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://root:{os.getenv('MYSQL_PASSWORD','admin')}@db:3306/{os.getenv('MYSQL_DATABASE', 'pentest_serverside')}"
    READER_DB_URL: str = f"mysql+aiomysql://root:{os.getenv('MYSQL_PASSWORD','admin')}@db:3306/{os.getenv('MYSQL_DATABASE', 'pentest_serverside')}"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    ENV: str = "dev"
    DEBUG: bool = True


class LocalConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://root:admin@localhost:3306/pentest_serverside"
    READER_DB_URL: str = f"mysql+aiomysql://root:admin@localhost:3306/pentest_serverside"
    ENV: str = "local"
    DEBUG: bool = True


class ProductionConfig(Config):
    DEBUG: bool = False
    WRITER_DB_URL: str = f"mysql+aiomysql://root:{os.getenv('MYSQL_PASSWORD','admin')}@db:3306/{os.getenv('MYSQL_DATABASE', 'pentest_serverside')}"
    READER_DB_URL: str = f"mysql+aiomysql://root:{os.getenv('MYSQL_PASSWORD','admin')}@db:3306/{os.getenv('MYSQL_DATABASE', 'pentest_serverside')}"
    ENV: str = "production"
    DEBUG: bool = False


def get_config():
    load_dotenv()
    env = os.getenv("APP_ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
