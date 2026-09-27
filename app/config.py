from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    supabase_url: str
    supabase_anon_key: SecretStr
    # Optional until the AI features are built.
    ai_gateway_api_key: SecretStr | None = None


@lru_cache
def get_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as exc:
        missing = ", ".join(str(err["loc"][0]).upper() for err in exc.errors())
        raise RuntimeError(
            f"Missing or invalid configuration: {missing}. "
            "Copy .env.example to .env and fill in the values."
        ) from None
