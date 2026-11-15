from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AgroAdapt API"
    API_V1_STR: str = "/api/v1"
    SUPABASE_URL: str
    SUPABASE_PUBLISHABLE_KEY: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


    @field_validator("SUPABASE_URL", "SUPABASE_PUBLISHABLE_KEY", mode="before")
    @classmethod
    def strip_environment_whitespace(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value


settings = Settings()
