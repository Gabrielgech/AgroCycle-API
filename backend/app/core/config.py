from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AgroAdapt API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://usuario:contraseña@localhost:5432/agroadapt"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()