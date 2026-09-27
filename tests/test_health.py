import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.main import app

ENV_VARS = ("SUPABASE_URL", "SUPABASE_ANON_KEY", "AI_GATEWAY_API_KEY")


@pytest.fixture(autouse=True)
def isolated_env(monkeypatch):
    """Ignore the developer's real environment and .env file."""
    for var in ENV_VARS:
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setattr(Settings, "model_config", {**Settings.model_config, "env_file": None})
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


def set_supabase_env(monkeypatch):
    monkeypatch.setenv("SUPABASE_URL", "https://example.supabase.co")
    monkeypatch.setenv("SUPABASE_ANON_KEY", "test-anon-key")


def test_health(monkeypatch):
    set_supabase_env(monkeypatch)
    monkeypatch.setenv("AI_GATEWAY_API_KEY", "test-gateway-key")

    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_starts_without_ai_gateway_key(monkeypatch):
    set_supabase_env(monkeypatch)

    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert get_settings().ai_gateway_api_key is None


def test_missing_env_fails_with_clear_message():
    with pytest.raises(RuntimeError, match="SUPABASE_URL.*Copy .env.example to .env"):
        get_settings()
