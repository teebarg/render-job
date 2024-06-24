from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URLs: List[str] = ["http://localhost:8000"]

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()
