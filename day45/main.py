"""
Scraping Best 100 Movie's Titles
"""

from bs4 import BeautifulSoup
import requests

TARGET_URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'


res = requests.get(TARGET_URL)

html = res.text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(name='h3', class_='title')

titles = [ title.getText() for title in titles]
titles.reverse() # or titles = titles[::-1]

with open('movie_titles.txt', 'w') as file:
    for title in titles:
        file.write(f"{title}\n")
        
