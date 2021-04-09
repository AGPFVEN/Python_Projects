import requests
import time
import Spotify_Credentials

def get_current_track(access_token):
    #request data using GET
    response = requests.get(
        'https://api.spotify.com/v1/me/player',
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
    )

    #Save data in a variable
    response_json = response.json()
    # print(response_json)

    #Process data
    track_id = response_json['item']['id']
    track_name = response_json['item']['name']
    artists = response_json['item']['artists']
    artists_names = ', '.join(
        [artist['name'] for artist in artists ]
    )
    time_passed = int(response_json['progress_ms'])
    time_total = int(response_json['item']['duration_ms'])
    time_rest = time_total - time_passed

    #Data processed
    current_track_info = {
        "id" : track_id,
        "name" : track_name,
        "artists" : artists_names,
        "progress" : time_passed,
        "duration" : time_total,
        "rest" : time_rest,
    }

    return current_track_info

def Get_Track():
    # while True:
        current_track_info = get_current_track(Spotify_Credentials.spotify_access_token)

        return current_track_info
        # time.sleep(9)

# Result //

#{'id': '2QjOHCTQ1Jl3zawyYOpxh6', 'name': 'Sweater Weather', 'artists': 'The Neighbourhood', 'progress': 160790, 'duration': 240400, 'rest': 79610}
#{'id': '5nujrmhLynf4yMoMtj8AQF', 'name': 'Levitating (feat. DaBaby)', 'artists': 'Dua Lipa, DaBaby', 'progress': 26874, 'duration': 203064, 'rest': 176190}