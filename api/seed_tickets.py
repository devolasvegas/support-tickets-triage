import asyncio
import random
from datetime import UTC, datetime, timedelta

from faker import Faker
from sqlalchemy import delete

from app.agents import AGENTS
from app.db import SessionLocal, engine
from app.models.ticket import Category, PlanTier, Priority, Status, Ticket
from app.sla import compute_sla_due_at
from seed_templates import TEMPLATES


def make_ticket(
    rng: random.Random, fake: Faker, customers: dict[str, PlanTier], now: datetime
) -> Ticket:
    status = rng.choices(list(Status), weights=[15, 35, 20, 15, 15])[0]
    priority = rng.choices(list(Priority), weights=[5, 20, 50, 25])[0]
    category = rng.choice(list(Category))
    subject_tpl, body_tpl = rng.choice(TEMPLATES[category])
    placeholder_vals = {
        "month": fake.month_name(),
        "invoice": f"INV-{fake.random_int(1000, 9999)}",
        "amount": f"${rng.randint(9, 499)}.00",
        "feature": rng.choice(["Reports", "Dashboards", "Billing"]),
        "email": fake.email(),
        "browser": rng.choice(["Safari", "Chrome", "Edge", "Firefox", "Opera"]),
    }
    subject = subject_tpl.format(**placeholder_vals)
    body = body_tpl.format(**placeholder_vals)
    customer = rng.choice(list(customers))
    plan_tier = customers[customer]
    assignee = None if status == Status.NEW else rng.choice(AGENTS)
    start = "-90d" if status in (Status.RESOLVED, Status.CLOSED) else "-18h"
    created_at = fake.date_time_between(start_date=start, end_date=now, tzinfo=UTC)
    gap = timedelta(hours=rng.uniform(0.5, 72))
    updated_at = created_at if status == Status.NEW else min(created_at + gap, now)
    sla_due_at = compute_sla_due_at(created_at, priority, plan_tier)

    return Ticket(
        status=status,
        priority=priority,
        plan_tier=plan_tier,
        category=category,
        subject=subject,
        body=body,
        customer=customer,
        assignee=assignee,
        created_at=created_at,
        updated_at=updated_at,
        sla_due_at=sla_due_at,
    )


async def main() -> None:
    fake = Faker()
    Faker.seed(42)

    rng = random.Random(42)

    customers = {fake.unique.company(): rng.choice(list(PlanTier)) for _ in range(300)}

    now = datetime.now(UTC)

    tickets = [make_ticket(rng, fake, customers, now) for _ in range(10_000)]

    async with SessionLocal() as session:
        await session.execute(delete(Ticket))
        session.add_all(tickets)
        await session.commit()

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
