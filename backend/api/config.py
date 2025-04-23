from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="/opt/.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    model: str = "gpt-4o-mini-2024-07-18"
    openai_api_key: str = ""
    mcp_server_port: int = 8050

    postgres_dsn: PostgresDsn = (
        "postgresql://postgres:password@example.supabase.com:6543/postgres"
    )


settings = Settings()
