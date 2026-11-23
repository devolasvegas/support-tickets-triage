from datetime import UTC, datetime, timedelta

from app.models.ticket import PlanTier, Priority
from app.sla import BASE_SLA, TIER_MULTIPLIER, compute_sla_due_at


def test_base_completeness() -> None:
    assert set(BASE_SLA) == set(Priority)


def test_multiplier_completeness() -> None:
    assert set(TIER_MULTIPLIER) == set(PlanTier)


def test_compute_sla_due_at() -> None:
    created_at = datetime(2026, 1, 1, tzinfo=UTC)
    priority = Priority.URGENT
    plan_tier = PlanTier.ENTERPRISE

    assert compute_sla_due_at(
        created_at, priority, plan_tier
    ) == created_at + timedelta(hours=1)
