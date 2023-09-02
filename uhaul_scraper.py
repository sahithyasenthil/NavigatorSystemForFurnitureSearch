"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

# import numpy as np # - Library for numpy
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
# from urllib.request import urlopen # - Library to extract html

# Fetch search results from UHaul
def get_uhaul_search_results(base_url, zip_code):

    url = base_url + str(zip_code) + "/Results/"

#   - To extract html file    
#   html = urlopen(base_url)
#   bsyc = BeautifulSoup(html.read(), "lxml")
#   fout = open('uhaul_html.txt', 'wt', encoding='utf-8')
#   fout.write(str(bsyc))
#   fout.close()
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    store_results = soup.find_all('li', {'class': 'divider'})

#   - To print products html    
#   for store in store_results:
#       print(store.prettify())
        
    store_info = []
    
    if len(store_results) > 5:
        store_results = store_results[:-1]
    
    # Gets stores
    for store in store_results:
        name = store.find('h3', {'class': 'collapse-half medium-uncollapse'}).text
        if(store.find('small', {'class': 'text-semibold'})) != None:
            name = name[3:-55]
        else:
            name = name[3:-3]
        url = store.h3.a['href']
        location = store.find('p', {'class': 'collapse'}).text
        location = location[23:-23]
        contact = store.find('ul', {'class': 'no-bullet collapse'}).find('a').text
        contact = contact[30:-26]
        open_hours = store.find('p', {'class': 'text-callout text-semibold text-lg'}).text
        open_hours = open_hours[10:-6]
        
        store_info.append([url, name, location, contact, open_hours])
    
    columns = ('Store URL', 'Name', 'Location', 'Contact No', 'Operating Hours')
    df = pd.DataFrame(store_info, columns=columns)
    
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Uhaul Results ({timestamp}).csv', index=False)

    return df    
    
if __name__ == '__main__':
    uhaul_base_url = "https://www.uhaul.com/Locations/"
    zip_code1 = 15213
    zip_code2 = 57226
    print('Scrape 1: ' + str(zip_code1))
    data1 = get_uhaul_search_results(uhaul_base_url, zip_code1)
    print(data1)
    print('Scrape 2: ' + str(zip_code2))
    data2 = get_uhaul_search_results(uhaul_base_url, zip_code2)
    print(data2)