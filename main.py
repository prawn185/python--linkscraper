import json
import urllib

import requests
import sitemap as sitemap
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

@todo: Let it scrape sitemap

array = ['LINK GOES IN HERE']

def getLinks(array):
    i = 0
    for url in array:
        i += 1
        print(str(round(i / len(array) * 100, 2)) + "%")
        sslinks = []

        soup = BeautifulSoup(urlopen(url), "html.parser")
        for link in soup.findAll('a'):
            if "https://ss." in link.get('href'):
                sslinks.append(link.get('href'))
        if len(sslinks) > 0:

            print(url)
            print(sslinks)



getLinks(array)
print("Done!")
