from src.email import Email
from src.msgraph_service import construct_message_json


def main():
    """
    Main idea:
    ----
    1. Assume you upload a file with contacts exported from Microsoft Outlook (no need for API call + for sure not exposing the customer data)
    2. Sanitize this list
        a. Remove missing entries (no email addresses)
        b. Remove invalid email addresses
        c. Remove selected names --> these have unsubscribed from the mailing or are not students
    3. use inp=ut parameter (number of recipients per email) > determine which recipients go into which email
        `max_num_recipients:int` ==> `list[tuple[to_recipients, cc_recipients, bcc_recipients]]`, with each of these three being list[EmailAddress]
    4. internal representation ==> list of Email objects (easier to work with). The above is just a helper method basically
    5. Loop over these emails:
        a. Create MSGraph API request to POST them as a draft
            - Add them to a httpx.Session instance to do this async
            - Ensure things cancel if any of the requests fails (after some timeout I guess).
            - Possibly: Add some retry mechanism to guard against timeouts due to some temporary connection problem that is not an issue with our code.
        b. Send API requests
    6. Logging for monitoring:
        - How many email addresses are in contacts ?
        - How many valid addresses after sanitization?
        - What emails where created?
        - Which drafts where successfully created?
        -
    """

    print("Hello from pilates-by-judith-mailing-list!")


if __name__ == "__main__":
    main()
