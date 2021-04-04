import os
import sys
import json
import spotipy
import base64
import requests
import datetime
import spotipy.util as util
from json.decoder import JSONDecodeError
import Spotify_Credentials

#Define Credentials
url_token = 'https://accounts.spotify.com/authorize'
client_id = Spotify_Credentials.client_id
response_type = 'code'
redirect_uri = 

# Request token
request = requests.get(url_token, )