from __future__ import print_function
from asyncio import events
import json
import datetime 
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from timeConversion import timeConversion

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    service = build('calendar', 'v3', credentials=creds)        
    today=datetime.datetime.today()
    #start is current date
    start=(datetime.datetime(today.year,today.month,today.day,00,00)).isoformat()+'Z'
    tomorrow=today+datetime.timedelta(days=1)
    end=(datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day,00,00)).isoformat()+'Z'
    print('getting events')
    #print(f"start:{start} tomorrow:{tomorrow} end:{end}")
     
    events_result=service.events().list(calendarId='primary',timeMin=start,timeMax=end,singleEvents=True,orderBy='startTime').execute()
    print(events_result)
    event_dict={}
    eventCount=0
    start=start.split('T')[0]
    start=str("'"+start+"'")
    events=events_result['items']
    #print(events)
    for key in events:
        timedateInfo=key['start']
        dateInfo,timeInfo=(str(timedateInfo).split(' ')[1]).split('T')
        timeInfo=timeInfo.split('-')[0]
        dateInfo=dateInfo+"'"
        timeInfo,message=timeConversion(timeInfo,1)
        #check if event date is current date
        if dateInfo==start:
            eventCount+=1
            #print(f"event:{key['summary']} start time:{timeInfo} count: {eventCount}")
            event_dict[key['summary']]=timeInfo
    

    #print(event_dict)
    return event_dict,eventCount
        

    

def getGoogleMain():
    return main()


