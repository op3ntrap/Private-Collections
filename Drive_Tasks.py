# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:37:39 2016

@author: acer
"""
  
from __future__ import print_function
import httplib2
import os
import requests

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from apiclient.discovery import build
import urllib
from Drive_Uploader import get_credentials
def upload_file(fileurl,filename):
  
    SCOPES = 'https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = 'client_secret_458107006015-nf2svn7dvr8lsd02aa99u3dvq4bllmeb.apps.googleusercontent.com (3).json'
    APPLICATION_NAME = 'Drive API Python Quickstart'
    
    credentials = get_credentials(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    http = credentials.authorize(httplib2.Http())
    my_drive = build('drive','v3',http=http)
    urllib.urlretrieve (fileurl, filename)
    upload = my_drive.files().create(body={ "mimeType" : "application/pdf","name":filename}, media_body=filename).execute()
    return



