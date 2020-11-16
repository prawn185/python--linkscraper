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
    for url in array:
        sslinks = []
        page = urlopen(url)

        soup = BeautifulSoup(page, "html.parser")
        for link in soup.findAll('a'):
        //find what?
            if "find what" in link.get('href'):
                sslinks.append(link.get('href'))
                //prints url found on & the link it found
        if len(sslinks) > 0:
            print(url)
            print(sslinks)


getLinks(array)
print("Done!")
