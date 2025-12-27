"""
Microsoft graph API related service
"""

from src.email import Email, DraftMessageResponse
import httpx

# convenient type definitions for JSON data
JSON = str | int | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONStr = dict[str, str]


class EmailService:
    """Microsoft Graph API service"""

    def __init__(self, url_base: str, api_key: str, client: httpx.Client) -> None:
        self._api_key_ = api_key
        self.client = client
        self.url_base = url_base

        # the request header is the same every time, so just create it once, so if we add more types of requests, no need to repeat
        self.header = self._construct_header()

    def create_draft_message(self, email: Email) -> DraftMessageResponse:
        """POST request for new message, return the identifier mentioned int he API's response and the Email used to construct the payload."""
        url_endpoint = f"{self.url_base}/messages"
        payload = self._construct_message_payload(email)
        response = self.client.post(url_endpoint, headers=self.header, json=payload)
        response.raise_for_status()
        return DraftMessageResponse(id=response.json()["id"], email=email)

    def _construct_header(self) -> JSONStr:
        """The header is shared for any type of response. Just create once you instantiate."""
        return {
            "Authorization": f"Bearer {self._api_key_}",
            "Content-type": "application/json",
        }

    def _construct_message_payload(self, email: Email) -> JSONObject:
        """Parse the email's data into the correct JSON format expected by the Microsoft Graph API"""
        return {
            "subject": email.subject,
            "body": {"contentType": "Text", "content": email.body},
            "toRecipients": self._add_recipients(email.recipients),
            "ccRecipients": self._add_recipients(email.cc_recipients),
            "bccRecipients": self._add_recipients(email.bcc_recipients),
        }

    def _add_recipients(self, recipients: list[str]) -> JSON:
        """Create a list of recipient addresses, in the JSON data format as expected."""
        return [{"emailAddress": {"address": email}} for email in recipients]
