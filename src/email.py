"""
Internal representation of an Email
"""

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Email:
    """
    basic representation of an email.

    #Todo: maybe use Pydantic to use the EmailStr type if that is beneficial
    """

    subject: str
    body: str
    recipients: list[str] = field(default_factory=list[str])
    cc_recipients: list[str] = field(default_factory=list[str])
    bcc_recipients: list[str] = field(default_factory=list[str])

    def __post_init__(self) -> None:
        self.recipients = [""]
        self.cc_recipients = [""]
        self.bcc_recipients = [""]
