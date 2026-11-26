"""Subject/body templates for seed tickets, grouped by category.

Placeholders are filled with str.format(). Every call should pass all of:
    {month} {invoice} {amount} {feature} {email} {browser}
Unused keyword arguments are ignored, so one format call works for any template.
"""

from app.models.ticket import Category

TEMPLATES: dict[Category, list[tuple[str, str]]] = {
    Category.BILLING: [
        (
            "Charged twice for {month}",
            (
                "Hi, I was billed twice for my {month} subscription. Both charges of "
                "{amount} show on my card statement. Can you refund the duplicate?"
            ),
        ),
        (
            "Invoice {invoice} has the wrong amount",
            (
                "Invoice {invoice} says {amount}, but our plan should cost less than "
                "that. Did the price change? We weren't notified."
            ),
        ),
        (
            "Need to update the card on file",
            (
                "Our company card expires this month. I can't find where to change the "
                "payment method in settings. Please advise before the {month} renewal."
            ),
        ),
        (
            "Refund request after downgrade",
            (
                "We downgraded our plan in {month} but were still charged the old "
                "price of {amount}. Can we get the difference refunded?"
            ),
        ),
        (
            "Need a VAT number on our invoices",
            (
                "Our finance team needs our VAT number on invoice {invoice} and on all "
                "future invoices. Where can I add it?"
            ),
        ),
    ],
    Category.BUG: [
        (
            "{feature} page won't load",
            (
                "Since this morning the {feature} page just shows a spinner. I've tried "
                "{browser} and cleared my cache. Other pages work fine."
            ),
        ),
        (
            "Export to CSV is missing rows",
            (
                "When I export from {feature}, the CSV has fewer rows than the screen "
                "shows. It looks like the last page is cut off."
            ),
        ),
        (
            "Error when saving changes in {feature}",
            (
                "Every time I click Save in {feature} I get 'Something went wrong'. "
                "My changes are lost. This happens in {browser}."
            ),
        ),
        (
            "Notifications sent to the wrong address",
            (
                "Notification emails are going to {email}, which isn't my address any "
                "more. I updated it in my profile but nothing changed."
            ),
        ),
        (
            "Dates show in the wrong time zone",
            (
                "All timestamps in {feature} are several hours off. My profile time "
                "zone is set correctly. It started after the last update."
            ),
        ),
    ],
    Category.ACCOUNT: [
        (
            "Can't log in after password reset",
            (
                "I reset my password but the new one is rejected on login. The reset "
                "email went to {email}. I'm locked out of my account."
            ),
        ),
        (
            "Add a new admin to our workspace",
            (
                "Our previous admin left the company. Please make {email} an admin so "
                "we can manage users again."
            ),
        ),
        (
            "Two-factor codes not working",
            (
                "My authenticator codes are rejected every time. I've checked the "
                "clock on my phone. I need to get into my account today."
            ),
        ),
        (
            "Merge two accounts",
            (
                "I accidentally created a second account with {email}. Can you merge "
                "it into my main account so I don't lose my data?"
            ),
        ),
        (
            "Delete my account and data",
            (
                "Please delete my account and all associated data. The account email "
                "is {email}. Let me know when it's done."
            ),
        ),
    ],
    Category.HOW_TO: [
        (
            "How do I share {feature} with my team?",
            (
                "I set up {feature} and want my teammates to see it, but I can't find "
                "a share option. Is that possible on our plan?"
            ),
        ),
        (
            "Bulk import from a spreadsheet",
            (
                "We have about 2,000 records in a spreadsheet. Is there a way to "
                "import them into {feature} without entering each one by hand?"
            ),
        ),
        (
            "Set up an integration with our CRM",
            (
                "Is there a guide for connecting our CRM? I'd like new contacts to "
                "sync automatically into {feature}."
            ),
        ),
        (
            "Change the default view in {feature}",
            (
                "Every time I open {feature} it resets to the default view. How do I "
                "make my filters stick?"
            ),
        ),
        (
            "Where are the API docs?",
            (
                "I want to pull data from {feature} into our own dashboard. Where can "
                "I find the API documentation and how do I get a key?"
            ),
        ),
    ],
    Category.FEATURE_REQUEST: [
        (
            "Dark mode, please",
            (
                "Would love a dark mode option. I use the app most evenings and the "
                "bright background is hard on the eyes."
            ),
        ),
        (
            "Allow custom fields in {feature}",
            (
                "We need to track a few extra fields that aren't built in. Custom "
                "fields in {feature} would save us a separate spreadsheet."
            ),
        ),
        (
            "Scheduled reports by email",
            (
                "It would be great to get a weekly summary of {feature} sent to "
                "{email} automatically instead of exporting it each time."
            ),
        ),
        (
            "Keyboard shortcuts",
            (
                "Power users on our team would move much faster with keyboard "
                "shortcuts, especially for navigating {feature}."
            ),
        ),
        (
            "More granular permissions",
            (
                "We'd like to give some users read-only access to {feature}. Right now "
                "it's all or nothing."
            ),
        ),
    ],
}
