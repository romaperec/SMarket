from pydantic_settings import BaseSettings


class Database(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:pass@localhost/smarket_shop"
    DB_ECHO: bool = False
