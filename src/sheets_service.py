import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from googleapiclient.discovery import build
from config import SPREADSHEET_ID, SHEET_NAME

def get_sheets_service(creds):
    return build("sheets", "v4", credentials=creds)

def append_row(service, row):
    body = {"values": [row]}
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()
