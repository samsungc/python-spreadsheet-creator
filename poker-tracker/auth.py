import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# no clue what this line does, just keeping it here for now
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_authed():
    '''Gets the user authenticated'''

    creds = None
    # first time auth, user will be prompted and token.json will be created automatically

    # if token.json exists, use that instead of prompting user to redo
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # if token.json doesnt exist or if creds are not valid, prompt user to log in again
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
            )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds

if __name__ == '__main__':
    get_authed()

    
    