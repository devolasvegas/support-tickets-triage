# Triage

A review queue for support tickets. Agents filter and sort a large ticket queue, open a ticket, see an AI-suggested priority and routing with its reasoning, and accept, override, or escalate it.

> **Status:** In progress. See the [milestones](../../milestones) for the build plan.

## Features

- **Queue:** a virtualized table of ~10,000 seeded tickets with column sorting, multi-filter (status, priority, category, assignee, date), and **saved views** (named filter and sort combinations stored server-side).
- **Detail drawer:** the full ticket, its activity history, and the AI panel.
- **AI suggestions:** a suggested priority and team, a confidence level, and short reasons that each cite a specific ticket field. Agents accept or override (with a reason) in one click, and every decision is logged so the AI's agreement rate can be measured.
- **Optimistic updates:** status and assignee changes show in the table instantly and roll back with a toast if the API rejects them.

## Stack

| Layer | Tools |
|---|---|
| Frontend | Next.js (App Router), TypeScript, TanStack Query, TanStack Table, TanStack Virtual, typed client generated from the API's OpenAPI spec |
| Backend | Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy 2.0 (async), Alembic, PostgreSQL |
| AI | Anthropic API with tool use for structured output |
| Tooling | uv, Ruff, pytest, httpx, Docker Compose |
| Ops | Sentry (frontend and backend, connected tracing), GitHub Actions |

## Repository layout

```
api/    FastAPI service (managed with uv)
web/    Next.js frontend
```

## Running locally

_Setup instructions will be added as each part is built._

## Decisions and trade-offs

_To be written as the project develops._

## Possible extensions

- Real-time collaboration (presence and live updates when two agents view the same ticket)
- Authentication (currently a hardcoded user picker by design)
