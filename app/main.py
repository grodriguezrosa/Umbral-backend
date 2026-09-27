from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Fail fast at startup if any required environment variable is missing.
    get_settings()
    yield


app = FastAPI(title="Umbral Backend", lifespan=lifespan)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
