from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
from jotform import *
api_key = ""

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = 'A2:A6'

def make_form(arr, newref_arr):
    params = { }
    if len(arr) <= 0:
        return
    new_form = requests.post("https://api.jotform.com/form", json=params, headers={"apiKey": api_key})
    form_details = new_form.json()
    form_id = form_details['content']['id']
    for line in arr:
        lineindex = arr.index(line)
        if "name" in line:
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"1":{"type":"control_fullname","text":"fullname","order":"1","name":"FullName"}}}')

        elif "email" in line:
             requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"2":{"type":"control_email","text":"Email","order":"2","name":"Email"}}}')
        elif "date" in line:
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"3":{"type":"control_datetime","text":"Date","order":"3","name":"Date"}}}')
        elif "text area" in line:
            index_line =  arr.index(line)
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"4":{"type":"control_textbox","text":"textbox","name":"textbox"}}}')
    requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"5":{"type":"control_button","text":"submit form","name":"form button"}}}')




    for line in newref_arr:
        lineindex = newref_arr.index(line)
        if "name" in line:
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"1":{"type":"control_fullname","text":{line},"order":"1","name":{line}}}}'.format(line))

        elif "email" in line:
             requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"2":{"type":"control_email","text":{line},"order":"2","name":{line}}}}'.format(line))
        elif "date" in line:
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"3":{"type":"control_datetime","text":"Date","order":"3","name":{line}}}}'.format(line))
        elif "text area" in line:
            index_line =  newref_arr.index(line)
            requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"4":{"type":"control_textbox","text":"textbox","name":{line}}}}'.format(line))



    ewquestion = requests.put(f"https://api.jotform.com/form/{form_id}/questions?apiKey=fe603c5b7d31598be598a909bc470c08", data='{"questions":{"1":{"type":"control_fullname","text":"fullname","order":"1","name":"FullName"},"2":{"type":"control_email","text":"Email","order":"2","name":"Email"}}}')













def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        ref_arr =[]
        arr = [str(row[0]) for row in values]
        for row in values:
            ref_arr.append(str(row[1]))
            print(f'{row[0]}')
        make_form(arr,ref_arr)
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()