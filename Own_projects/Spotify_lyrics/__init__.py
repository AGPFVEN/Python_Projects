from Spotify_Get_Track import Get_Track
from Google_Search_Song import Show_Lyrics

song_info = Get_Track()
print(song_info)
Show_Lyrics(song_info['artists'], song_info['name'])
