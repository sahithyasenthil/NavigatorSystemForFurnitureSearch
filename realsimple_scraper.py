"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

import pandas as pd
import numpy as np
import datetime
from bs4 import BeautifulSoup
import urllib3
import requests
import time
import re
import os
import math
import pip

# Fetch search results from RealSimple
def get_realsimple_search_results(base_url):
        
    page = requests.get(base_url)
    data=[]

    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.prettify())

    list1 = soup.find('div',{"class" : "comp three-post__inner card-list mntl-document-card-list mntl-card-list mntl-block"})
    list2 = list1.find_all('a')

    for title in list2:
        details = []
        details.append(title.find("div",{"class":"card__content"}).get("data-tag"))
        details.append(title.get("href")) #link to the article
        details.append(title.find('span',{"class":"card__title"}).contents[0].contents[0])
        details.append(title.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
        data.append(details)
    
    # print(data)

    links = soup.find("div",{"class":"comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block"})
    a = links.find_all('a')
    len(links)

    for atags in a:
        details = []
        details.append(atags.find("div",{"class":"card__content"}).get("data-tag"))
        details.append(title.get("href")) #link to the article
        details.append(atags.find('span',{"class":"card__title"}).contents[0].contents[0])
        details.append(atags.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
        data.append(details)
        # count = count + 1
    
    df = pd.DataFrame (data, columns = ['Category','Link','Title','Image_Link'])
    # print(df)

    # Save to CSV
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'RealSimple Results ({timestamp}).csv', index=False)