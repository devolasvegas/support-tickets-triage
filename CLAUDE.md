# Triage: Claude Instructions

## Purpose

Triage is a portfolio project. Its main job is to give me real, explainable experience with a Python backend (FastAPI, SQLAlchemy, Alembic, pytest). I need to be able to walk an interviewer through any part of this code and explain why it works the way it does.

## Learning mode (most important rule)

I'm an experienced TypeScript/Node developer learning Python. Work with me as a pair, not a code generator.

**In `api/` (Python):**
- Let me write the code. Give me the next step, point me to the relevant docs or concept, and review what I write.
- When I'm stuck, explain the idea and show a small example, then let me apply it. Don't write whole files or whole features unless I explicitly ask.
- When you introduce a Python idiom, explain it briefly and compare it to the TypeScript/Node equivalent where one exists (for example, `async with` vs. try/finally, Pydantic models vs. Zod schemas, uv vs. npm).
- In reviews, point out anything un-Pythonic and tell me why.
- Boilerplate and config (Docker Compose, Alembic setup, CI YAML) are fine for you to write, but explain what each part does.

**In `web/` (Next.js/TypeScript):** this is familiar ground. You can move faster and write more directly here, but keep the code idiomatic and explain any TanStack patterns that are new to me.

## Stack and conventions

**Backend (`api/`)**
- Python 3.12+, managed with **uv** (`uv add`, `uv run`). No pip or requirements.txt.
- FastAPI + Pydantic v2; settings via `pydantic-settings` reading `.env`.
- SQLAlchemy 2.0 **async** style (`AsyncSession`, `select()`), with asyncpg. No legacy `Query` API.
- Alembic for every schema change; never edit tables by hand.
- **Ruff** for lint and format. Type hints everywhere.
- **pytest** + **httpx** for API tests.
- Anthropic Python SDK for AI suggestions, using tool use with a strict schema for structured output.

**Frontend (`web/`)**
- Next.js App Router + TypeScript (strict).
- TanStack Query for server state and optimistic updates; TanStack Table + Virtual for the queue.
- API client generated from the FastAPI OpenAPI spec. Regenerate it; never hand-edit generated files.
- Filters and sort live in the URL.

**Local infra**
- Docker Compose runs Postgres.

## Domain

Support tickets. Core models: `Ticket` (subject, body, customer, plan tier, status, priority, category, assignee, created/updated timestamps, SLA due date), `SavedView` (named filter and sort JSON per user), `Suggestion` (cached AI output: suggested priority and team, confidence, reasons citing ticket fields), and a decision log of accepts and overrides.

## Scope guardrails

- **No auth** beyond a hardcoded user picker.
- **No real-time collaboration.** It's listed as a possible extension in the README.
- **Keep the AI feature small and well done.** One structured suggestion with visible, field-cited reasoning. No chatbot.
- If a task starts to grow beyond its milestone, flag it rather than expanding scope.

## Planning

The build plan lives in GitHub milestones (one per phase) with an issue per task. Each phase should end in something that works on its own.
