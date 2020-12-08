#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
from requests import get

url = 'https://www.albumoftheyear.org/list/1500-rolling-stones-500-greatest-albums-of-all-time-2020/'

soup = bs(get(url).text, 'html.parser')

albums = soup.find_all('div', attrs={'class', 'albumListCover'})

def download(img):
    print(img)
    with open(img.split('https://cdn2.albumoftheyear.org/400x/album/')[1],
    'wb') as file:
        file.write(get(img).content)

for album in albums[:2]: 
    source = album.find_all('source')[0]
    img = source['data-srcset'].split(', ')[1].split(' 2x')[0].strip()
    download(img)
    

