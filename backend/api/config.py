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

    pg_url: str = "postgres://postgres"
    pg_user: str = "postgres"
    pg_pass: str = "postgres"


settings = Settings()
