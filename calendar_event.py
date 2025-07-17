# calendar_event.py

from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def create_calendar_event(task, deadline_date, assignee_email=None):
    """Adds task to Google Calendar and invites the assignee."""
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': task,
        'description': f'Task assigned to: {assignee_email}' if assignee_email else task,
        'start': {
            'date': deadline_date,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'date': deadline_date,
            'timeZone': 'Asia/Kolkata',
        },
    }

    # ➕ Add assignee as guest if provided
    if assignee_email:
        event['attendees'] = [{'email': assignee_email}]

    event = service.events().insert(calendarId='primary', body=event, sendUpdates='all').execute()
    return event.get('htmlLink')
