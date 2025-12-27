"""
Data models
"""

from pydantic import BaseModel, EmailStr, Field


class Email(BaseModel):
    """Internal representation of an email."""

    subject: str
    body: str
    recipients: list[EmailStr] = Field(default_factory=list)
    cc_recipients: list[EmailStr] = Field(default_factory=list)
    bcc_recipients: list[EmailStr] = Field(default_factory=list)


class DraftMessageResponse(BaseModel):
    """How we model the response from a POST request for an email draft message"""

    id: int
    email: Email
