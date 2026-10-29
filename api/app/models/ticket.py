from datetime import datetime
from enum import IntEnum, StrEnum
from typing import ClassVar

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    SmallInteger,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Status(StrEnum):
    NEW = "new"
    OPEN = "open"
    PENDING = "pending"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Priority(IntEnum):
    URGENT = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4


class PlanTier(StrEnum):
    FREE = "free"
    PRO = "pro"
    BUSINESS = "business"
    ENTERPRISE = "enterprise"


class Category(StrEnum):
    BILLING = "billing"
    BUG = "bug"
    ACCOUNT = "account"
    HOW_TO = "how_to"
    FEATURE_REQUEST = "feature_request"


def _enum_values(e: type[StrEnum]) -> list[str]:
    return [m.value for m in e]


def _str_enum(enum_cls: type[StrEnum], name: str) -> Enum:
    return Enum(
        enum_cls,
        name=name,
        native_enum=False,
        create_constraint=True,
        values_callable=_enum_values,
    )


class Ticket(Base):
    __tablename__ = "tickets"
    __table_args__ = (
        CheckConstraint(
            f"priority BETWEEN {min(Priority)} AND {max(Priority)}", name="priority"
        ),
    )
    __mapper_args__: ClassVar = {"eager_defaults": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[Status] = mapped_column(_str_enum(Status, "status"))
    priority: Mapped[int] = mapped_column(SmallInteger)
    plan_tier: Mapped[PlanTier] = mapped_column(_str_enum(PlanTier, "plan_tier"))
    category: Mapped[Category] = mapped_column(_str_enum(Category, "category"))
    subject: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    customer: Mapped[str] = mapped_column(String(255))
    assignee: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )
    sla_due_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
