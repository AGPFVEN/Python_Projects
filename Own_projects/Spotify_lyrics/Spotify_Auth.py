import Spotify_Credentials
from spotipy.oauth2 import SpotifyOAuth
from requests.auth import HTTPBasicAuth
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)
#-m python flask run

app.config['SESSION_COOKIE_NAME'] = 'Jasons Cookie'

@app.route('/')
def index():
    sp_oauth = create_spotify_Oauth()
    auth_url = sp_oauth.get
    return redirect(auth_url)

@app.route('/redirect')
def redirect():
    return 'redirect'

@app.route('/getTracks')
def getTracks():
    return 'song'

# Request token
# request = requests.get(url_token, )

def create_spotify_Oauth():
    return spotifyOAuth(
        client_id = Spotify_Credentials.client_id,
        client_secret = Spotify_Credentials.client_secret,
        redirect_uri = url_for('/redirect', _external = True),
        scope = "user-library-read"
    )

#Define Credentials
url_token = 'https://accounts.spotify.com/authorize'
client_id = Spotify_Credentials.client_id
response_type = 'code'

if __name__ == "__main__":
    app.run(debug=True)