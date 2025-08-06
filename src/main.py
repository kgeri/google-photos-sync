#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.discovery import build
from googleapiclient.errors import UnknownApiNameOrVersion
import logging
import os
import pickle
import time


class GooglePhotosService:
    def __init__(self) -> None:
        root_dir = os.path.dirname(os.path.realpath(__file__)) + '/..'
        creds = None
        if os.path.exists(f'{root_dir}/token.pickle'):
            with open(f'{root_dir}/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(f'{root_dir}/credentials.json', scopes=['https://www.googleapis.com/auth/photoslibrary.readonly'])
                creds = flow.run_local_server(port=0)
            with open(f'{root_dir}/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        print(creds)
        self.service = build('photoslibrary', 'v1', credentials=creds)

    def list_albums(self):
        page_token = None
        while True:
            results = self.service.albums().list(
                pageSize=50,
                page_token=page_token
            ).execute()
            
            albums = results.get('albums', [])

            if not albums:
                logging.error('No albums found.')
                break
            
            for album in albums:
                # Print the title of each album
                logging.info(f"- {album['title']}")
            
            page_token = results.get('nextPageToken')
            if not page_token:
                break

if __name__ == '__main__':
    # Logging config
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%dT%H:%M:%SZ')
    logging.Formatter.converter = time.gmtime
    
    GooglePhotosService().list_albums()
