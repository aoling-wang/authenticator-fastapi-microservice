from pydantic_settings import BaseSettings, SettingsConfigDict

# Create link to .env for environement variable, database URL

class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

# Load database URL into application for use

settings = Settings()