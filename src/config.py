from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:pass@localhost/smarket_shop"
    DB_ECHO: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


database_config = DatabaseConfig()
