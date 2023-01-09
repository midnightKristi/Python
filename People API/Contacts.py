# Kristi LaVigne
# CSCI 236
# 03/06/2021
# Program 02 - DNA
# hours: 3
# Grade Version - N/A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

# This program utilizes the Google People API.
# Shows basic usage of the People API.
# If users Google account login credentials aren't provided,
# then the user is asked to log into their Google account.
# The contacts are scrapped from the account and stored in a list.
# Then the program prints the name of the first 10 connections.
# The program sorts the list alphabetically and prints them again.

# This program is a combination of google code samples and original code written by K. LaVigne.

from __future__ import print_function

from typing import List, Any, Union

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    # get ten contact names and display them
    print('\nList 10 connection names:')
    print('-------------------------')
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='names,emailAddresses').execute()
    connections = results.get('connections', [])

    # list for storing contact names
    name_list: List[str] = []

    for person in connections:
        names = person.get('names', [])
        if names:
            name = names[0].get('displayName')
            print(name)
            # adding this contact to the list
            name_list.append(str(name))

    # sort the list of contacts and display them again
    name_list.sort()

    print('\nList sorted connection names:')
    print('-----------------------------')

    for i in range(10):
        contact = name_list[i]
        print(contact)

if __name__ == '__main__':
    main()
