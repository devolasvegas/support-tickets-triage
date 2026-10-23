from functools import lru_cache
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    database_url: str
    db_echo: bool = False

    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    @field_validator("database_url")
    @classmethod
    def validate_db_url(cls, v: str) -> str:
        if "://" not in v:
            raise ValueError("Invalid URL format. Missing '://'")

        scheme, remainder = v.split("://", 1)

        # 1. Normalize "postgres" (with or without driver) to "postgresql"
        if scheme == "postgres":
            scheme = "postgresql"
        elif scheme == "postgres+asyncpg":
            scheme = "postgresql+asyncpg"

        # 2. Enforce the mandatory "+asyncpg" driver
        if scheme == "postgresql":
            scheme = "postgresql+asyncpg"
        elif scheme != "postgresql+asyncpg":
            # 3. Reject anything else (like mysql, sqlite, etc.)
            raise ValueError(
                f"Unsupported scheme '{scheme}'. Must be 'postgres' or 'postgresql' (with or without +asyncpg)"
            )

        return f"{scheme}://{remainder}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
