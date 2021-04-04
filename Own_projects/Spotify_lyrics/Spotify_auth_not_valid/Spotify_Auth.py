import os
import sys
import json
import spotipy
import webbrowser
import base64
import requests
import datetime
import spotipy.util as util
from json.decoder import JSONDecodeError
import Spotify_Credentials

#Define the Spotify Credentials
client_credentials = f"{Spotify_Credentials.client_id}:{Spotify_Credentials.client_secret}"
client_credentials_base_64 = base64.b64encode(client_credentials.encode())

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type" : "client_credentials"
}
token_header = {
    "Authorization" : f"Basic {client_credentials_base_64.decode()}"
}

# Request token
request = requests.post(token_url, data=token_data, headers=token_header)
valid_token = request.status_code in range(200, 299)

if valid_token:
    access_token = response_data_token['access_token']
    print(response_data_token, f"\n", valid_token )
    response_data_token = request.json()
    now = datetime.datetime.now()                         #Refresh Token
    expires_in = response_data_token['expires_in']
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expires = expires < now