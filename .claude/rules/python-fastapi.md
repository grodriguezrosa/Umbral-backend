---
paths:
  - "app/**/*.py"
---

# Python and FastAPI

- Python ≥ 3.11 with type hints on every signature. Use `X | None`, not `Optional[X]`.
- Requests and responses use Pydantic v2 models in `app/schemas/`. Always set a `response_model` or return type; never return an untyped `dict` from a public endpoint.
- Inject dependencies with `Depends` / `Annotated[..., Depends(...)]`: settings (`get_settings`), the authenticated user, external clients. Don't instantiate clients inside handlers.
- Never read `os.environ` outside `app/config.py`.
- Async end to end: `async def` handlers when doing I/O, with async clients (`httpx.AsyncClient`, async Supabase client). No blocking calls (`requests`, `time.sleep`) inside `async def`.
- Long-lived HTTP clients are created and closed in the `lifespan`.
- Errors: `HTTPException` with the correct status and a clear `detail`. Never expose stack traces or upstream provider messages to clients; log them with `logging`.
- One router per domain (`APIRouter(prefix="/x", tags=["x"])`), registered in `app/main.py`.
- Don't add dependencies without need; when needed, `uv add <pkg>`.
- All comments, docstrings, and error/log messages in English.
