import base64
import re
from bs4 import BeautifulSoup


def safe_base64_decode(data: str) -> str:
    if not data:
        return ""

    # Remove non-ASCII characters
    data = data.encode("ascii", errors="ignore").decode("ascii")

    # Fix padding
    missing_padding = len(data) % 4
    if missing_padding:
        data += "=" * (4 - missing_padding)

    try:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
    except Exception:
        return ""


def parse_email(message):
    headers = message["payload"]["headers"]

    email_data = {
        "from": "",
        "subject": "",
        "date": "",
        "content": ""
    }

    for h in headers:
        if h["name"] == "From":
            email_data["from"] = h["value"]
        elif h["name"] == "Subject":
            email_data["subject"] = h["value"]
        elif h["name"] == "Date":
            email_data["date"] = h["value"]

    body_text = ""

    payload = message.get("payload", {})

    if "parts" in payload:
        for part in payload["parts"]:
            mime = part.get("mimeType", "")
            data = part.get("body", {}).get("data", "")

            if mime == "text/plain":
                body_text = safe_base64_decode(data)
                break

            if mime == "text/html" and not body_text:
                html = safe_base64_decode(data)
                body_text = BeautifulSoup(html, "html.parser").get_text()

    else:
        data = payload.get("body", {}).get("data", "")
        body_text = safe_base64_decode(data)

    email_data["content"] = body_text.strip()
    return email_data
