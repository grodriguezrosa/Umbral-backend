# Umbral Backend

FastAPI API for an AI app: exposes endpoints that call LLMs through the AI Gateway and persist data in Supabase (Postgres + Auth).

## Language

**Everything written to this repo is in English**: code, identifiers, comments, docstrings, error messages, log messages, test names, commit messages, docs, and `.claude/` config. No Spanish or mixed-language text in any file. (Chat replies to the user can be in whatever language they write in.)

## Commands

```bash
uv sync                                   # install dependencies
uv run uvicorn app.main:app --reload      # local server (requires .env)
uv run pytest                             # tests
uv run ruff format . && uv run ruff check --fix .   # format + lint
```

Always use `uv run` / `uv add`; never `pip install` or the system `python`.

## Layout

- `app/main.py`: FastAPI instance, lifespan, router registration.
- `app/config.py`: `Settings` (pydantic-settings). The only place environment variables are read.
- `tests/`: pytest + `TestClient`.

As it grows: routers in `app/routers/<domain>.py`, schemas in `app/schemas/`, business logic and external clients in `app/services/`. Keep endpoints thin; logic lives in services.

## Configuration

Variables (see `.env.example`):
- Required: `SUPABASE_URL`, `SUPABASE_ANON_KEY`. The app fails at startup if either is missing — this is intentional.
- Optional for now: `AI_GATEWAY_API_KEY`. AI features come last; until then it may be unset. When the AI work starts, make it required again.
To add a variable: add a field to `Settings`, a line to `.env.example`, and a `monkeypatch.setenv` in tests.

## Not yet defined

- **Jev**: will be used and configured later. Do not assume how it works or add code for it until it is documented here.
- Deployment target: undecided. Do not add deployment config (Dockerfile, vercel.json, etc.).

## Rules

Detailed rules live in `.claude/rules/`: Python/FastAPI, Supabase, AI Gateway, testing, security.

## Workflow

- Hooks are active (`.claude/settings.json`): ruff formats and lints every `.py` you edit, and pytest runs at the end of each turn. If they fail, fix the cause; never disable or bypass a hook.
- Every new endpoint ships with at least one test.
