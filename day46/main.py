"""
Project Music Time Machine
"""
from bs4 import BeautifulSoup
import requests
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# for dev
from pprint import pprint

# load Environment variables
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv('SECRET_KEY')

# NOTE: ex) https://www.billboard.com/charts/hot-100/2023-03-11/
BILLBOARD_ENDPOINT = 'https://www.billboard.com/charts/hot-100/'

def main():
    
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri='https://example.com/recall',
            client_id=CLIENT_ID,
            client_secret=SECRET_KEY,
            show_dialog=True,
            cache_path='token.txt'
    ))
    
    user_id = spotify.current_user()['id']
    

    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    res = requests.get(f"{BILLBOARD_ENDPOINT}/{year}-{format_month(month)}-{format_day(day)}/")
    res.raise_for_status()
    html = res.text


    soup = BeautifulSoup(html, 'html.parser')
    
    """
    NOTE:クラス名が複雑なものが多かったのでわかりやすいもの起点にsiblingを続けて要素を取得した（多分、CSSフレームワークの影響かな？）
    NOTE:next_siblingで次の兄弟要素を指定できる。previous_siblingもある。
       （https://www.crummy.com/software/BeautifulSoup/bs4/doc/#:~:text=code%20you%20write.-,.next_sibling%20and%20.previous_sibling,-You%20can%20use）
    """
    
    
    chart_results = soup.find_all(class_="o-chart-results-list-row")
    
    billboard_top_100 = []

    for song in chart_results:
        song_title = song.h3.get_text().strip('\n\t')
       
        artist = song.h3.next_sibling.next_sibling.get_text().strip('\n\t')
        print(song_title, artist)
        new_data = {
            "song": song_title,
            "artist": artist
        }
        billboard_top_100.append(new_data)
    
    song_uris = []

    for song in billboard_top_100:
        result = spotify.search(q=f"track:{song['song']} year:{year}", type='track')
        print(result)
        
        try:
            uri = result['tracks']['items'][0]['uri']
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped")
    
    playlist = spotify.user_playlist_create(user=user_id,
                                            name=f"{year}-{month}-{day} Billboard 100",
                                            public=False
                                            )
    
    pprint(playlist)
    
    spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    


def with_zero(num):
    if num < 10:
        return f"0{num}"
    return num

def format_month(num):
    return with_zero(num)

def format_day(num):
    return with_zero(num)

if __name__ == '__main__':
    main()