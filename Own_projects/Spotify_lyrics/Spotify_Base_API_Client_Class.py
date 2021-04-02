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

class SpotifyAPI(object):
    access_token = None
    client_id = None
    client_secret = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 string
        """
        client_id = self.client_id
        client_secret = self.client_secret

        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client secret")

        client_credentials = f"{client_id}:{client_secret}"
        client_credentials_base_64 = base64.b64encode(client_credentials.encode())
        return client_credentials_base_64.decode()

    def get_token_header(self):
        client_credentials_base_64 = self.get_client_credentials()
        return {
            "Authorization" : f"Basic {client_credentials_base_64}"
        }

    def get_token_data(self):
        return {
            "grant_type" : "client_credentials"
        }

    def perform_auth(self):
        # Request token
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_header()
        request = requests.post(token_url, data=token_data, headers=token_header)

        if request.status_code not in range(200, 299):
            return False
         
        data = request.json()
        access_token = data['access_token']
        now = datetime.datetime.now()                         #Refresh Token
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

client = SpotifyAPI(Spotify_Credentials.client_id, Spotify_Credentials.client_secret)
print(client.perform_auth())
print(client.access_token)