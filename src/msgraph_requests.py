"""
Helpers to create proper requests for the Microsoft Graph API
"""

from src.email import Email


# convenient type definitions for JSON data
JSON = str | int | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]


def construct_message_json(email: Email) -> JSONObject:
    """Use the Email information to create the appropriate JSON for a request to the Microsoft Graph API"""
    return {
        "subject": email.subject,
        "body": {"contentType": "Text", "content": email.body},
        "toRecipients": add_recipients(email.recipients),
        "ccRecipients": add_recipients(email.cc_recipients),
        "bccRecipients": add_recipients(email.bcc_recipients),
    }


def add_recipients(recipients: list[str]) -> JSON:
    """Create a list of recipient addresses, in the JSON data format as expected."""
    return [{"emailAddress": {"address": email}} for email in recipients]
