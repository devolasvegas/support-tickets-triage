from collections.abc import Mapping
from datetime import datetime, timedelta
from types import MappingProxyType

from app.models.ticket import PlanTier, Priority

BASE_SLA: Mapping[Priority, timedelta] = MappingProxyType(
    {
        Priority.URGENT: timedelta(hours=4),
        Priority.HIGH: timedelta(hours=8),
        Priority.NORMAL: timedelta(hours=24),
        Priority.LOW: timedelta(hours=48),
    }
)

TIER_MULTIPLIER: Mapping[PlanTier, float] = MappingProxyType(
    {
        PlanTier.ENTERPRISE: 0.25,
        PlanTier.BUSINESS: 0.5,
        PlanTier.PRO: 0.75,
        PlanTier.FREE: 1.0,
    }
)


def compute_sla_due_at(
    created_at: datetime, priority: Priority, plan_tier: PlanTier
) -> datetime:
    return created_at + BASE_SLA[priority] * TIER_MULTIPLIER[plan_tier]
