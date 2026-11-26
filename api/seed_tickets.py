import random

from faker import Faker

from app.models.ticket import Category, PlanTier, Priority, Status, Ticket

fake = Faker()
Faker.seed(42)

SUBJECTS: dict[Category, list[str]] = {
    Category.BILLING: ["Charged twice for {month}", "Invoice {n} is wrong"]
}

rng = random.Random(42)

customers = {fake.unique.company(): rng.choice(list(PlanTier)) for _ in range(300)}


def make_ticket(
    rng: random.Random, fake: Faker, customers: dict[str, PlanTier]
) -> Ticket:
    category = rng.choice(list(Category))
    subject = rng.choice(SUBJECTS[category]).format(
        month=fake.month_name(), n=fake.random_int(1000, 9999)
    )
    customer = rng.choice(list(customers))

    # assignee should be None for NEW tickets and filled in for the other statuses, so the data matches how the statuses work.
    # Set created_at and updated_at explicitly. Otherwise server_default=func.now() stamps all 10,000 rows with the same moment.

    return Ticket(
        status=rng.choice(list(Status)),
        priority=rng.choices(list(Priority), weights=[5, 20, 50, 25])[0],
        plan_tier=customers[customer],
        category=category,
        subject=subject,
        customer=customer,
    )


def main() -> None:
    [make_ticket(rng, fake, customers) for _ in range(10_000)]


if __name__ == "__main__":
    main()
