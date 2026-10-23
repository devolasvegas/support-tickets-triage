from fastapi import FastAPI
from sqlalchemy import text

from app import db

app = FastAPI(title="Triage API")


@app.get("/health")
async def health(session: db.SessionDep) -> dict[str, str]:
    await session.execute(text("SELECT 1"))

    return {"status": "ok", "database": "ok"}
