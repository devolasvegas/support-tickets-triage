from datetime import datetime, timedelta

from app.models.ticket import PlanTier, Priority

sla_table = {(Priority.URGENT, PlanTier.ENTERPRISE): timedelta(hours=1)}


def compute_sla_due_at(
    created_at: datetime, priority: Priority, plan_tier: PlanTier
) -> datetime:
    time_delta = sla_table[(priority, plan_tier)]
    sla_due_at = created_at + time_delta
    return sla_due_at
