from Spotify_Get_Track import Get_Track
from Google_Search_Song import Show_Lyrics
import time

current_song_info_name = None

while True:

    new_song_info = Get_Track()

    if(new_song_info['name'] != current_song_info_name):

        current_song_info_artist = new_song_info['artists']
        current_song_info_name = new_song_info['name']
        Show_Lyrics(current_song_info_artist, current_song_info_name)
        print("\n\n",Show_Lyrics(current_song_info_artist, current_song_info_name))
    else:
        time.sleep(2)
