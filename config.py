from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL: str = "http://localhost:8000"

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()
