import sys
import os
import json


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


from config import STATE_FILE
from gmail_service import get_gmail_service
from sheets_service import get_sheets_service, append_row
from email_parser import parse_email


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"processed_ids": []}

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "processed_ids" not in data:
                return {"processed_ids": []}
            return data
    except (json.JSONDecodeError, ValueError):
        return {"processed_ids": []}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def main():
    state = load_state()

    gmail = get_gmail_service()
    sheets = get_sheets_service(gmail._http.credentials)

    results = gmail.users().messages().list(
        userId="me",
        labelIds=["INBOX", "UNREAD"]
    ).execute()

    messages = results.get("messages", [])

    for msg in messages:
        if msg["id"] in state["processed_ids"]:
            continue

        full_msg = gmail.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        email = parse_email(full_msg)

        
        MAX_CELL_LENGTH = 45000
        content = email.get("content", "") or ""

        if len(content) > MAX_CELL_LENGTH:
            content = content[:MAX_CELL_LENGTH] + "\n\n[Content truncated]"

        append_row(
            sheets,
            [
                email.get("from", ""),
                email.get("subject", ""),
                email.get("date", ""),
                content
            ]
        )

        
        gmail.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        state["processed_ids"].append(msg["id"])

    save_state(state)


if __name__ == "__main__":
    main()
