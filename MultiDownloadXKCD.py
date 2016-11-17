#! python3
# Use multiple threads to download XKCD comics.

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True) # Store comics in ./xkcd

def downloadXKCD(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        # Download the page.
        print('Downloading page http://xkcd.com/%s' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)
