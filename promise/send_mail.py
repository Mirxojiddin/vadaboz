import requests
import json
from django.conf import settings


def send_email(subject, message, from_email, to_emails):
    url = "https://api.brevo.com/v3/smtp/email"

    data = {
        "sender": {"email": from_email},
        "to": [{"email": to_emails}],
        "replyTo": {"email": to_emails},
        "textContent": f"{message}",
        "subject": f"{subject}",
    }

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print the response
    if response.status_code == 201:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email: {response.status_code}")
        print(response.json())
