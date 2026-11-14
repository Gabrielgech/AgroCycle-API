from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AgroAdapt API"
    API_V1_STR: str = "/api/v1"  # <--- Añadimos este campo que faltaba
    SUPABASE_URL: str
    SUPABASE_PUBLISHABLE_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()