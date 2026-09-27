---
paths:
  - "tests/**/*.py"
---

# Testing

- pytest with `fastapi.testclient.TestClient`, used as a context manager (`with TestClient(app) as client:`) so the lifespan runs.
- Set env vars with `monkeypatch.setenv` followed by `get_settings.cache_clear()`. If this repeats, move it into a fixture in `tests/conftest.py`.
- No real network: replace Supabase and the AI Gateway with `app.dependency_overrides` or service mocks.
- Every endpoint gets at least a happy-path test and a test for its main error case (401 without token, 422 on invalid input, etc.).
- One file per router: `tests/test_<domain>.py`.
- Never weaken or delete a test to make it pass. If the test is wrong, explain why.
