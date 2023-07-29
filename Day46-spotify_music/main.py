import spotipy as spotipy
from bs4 import BeautifulSoup
import requests
import os
import sys
import json
import webbrowser
import spotipy.util as util
# from json.decoder import JSONDecoderError
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

username = sys.argv[1]

# User_ID = 31ilxbwdzcbj75a6qy3cextbgd3i
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)
    # auth_manager = SpotifyOAuth(scope=scope)
    # spotipy.Spotify(auth_manager=auth_manager)

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

print(json.dumps(user, sort_keys=True, indent=4))



















#
#
# URL = "https://www.billboard.com/charts/hot-100"
#
# SPOTIPY_CLIENT_ID = "a2c96455e32f4ef09c9dce667ddc0625"
# SPOTIPY_CLIENT_SECRET = "f4ca367a9773422d8208d89aa671e0c8"
# APP_REDIRECT_URI = "https://developer.spotify.com/dashboard/applications/a2c96455e32f4ef09c9dce667ddc0625"
#
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
#                                                            client_secret=SPOTIPY_CLIENT_SECRET))
#
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
#
# response = requests.get(f"{URL}/{date}/")
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
# print(soup.title)
# songs = []
# song_name = soup.select("h3#title-of-a-story.c-title.a-no-trucate.a-font-primary-bold-s")
# for song in song_name:
#     text = song.getText()
#     songs.append(text)
#
# songs = [text.getText().strip("\t\n") for text in song_name[:100]]
# print(songs)
