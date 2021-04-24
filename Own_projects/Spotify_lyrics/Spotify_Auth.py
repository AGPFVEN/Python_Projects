import spotipy
from spotipy.oauth2 import SpotifyOAuth
import Spotify_Credentials
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)
#-m python flask run

app.config['SESSION_COOKIE_NAME'] = 'Jasons Cookie'

@app.route('/')
def index():
    return 'Jasons home page'

@app.route('/getTracks')
def getTracks():
    return 'song'

# Request token
# request = requests.get(url_token, )
def create_spotify_Oauth():
    return spotifyOAuth(
        client_id = Spotify_Credentials.client_id,
        client_secret = Spotify_Credentials.client_secret,
        redirect_uri = url_for('localhost:5000/redirect', _external = True),
        scope = "user-library-read"
    )

#Define Credentials
url_token = 'https://accounts.spotify.com/authorize'
client_id = Spotify_Credentials.client_id
response_type = 'code'