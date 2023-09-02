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

# Fetch search results from Craigslist
def get_craigslist_search_results(base_url):
    page = requests.get(base_url)

    # print(page.content)

    soup = BeautifulSoup(page.content, "html.parser")

    total_results = int(soup.find('span', 'totalcount').text)
    # print(total_results)

    total_pages = (total_results // 120) + 1

    search_results = []

    results = soup.find('ul', {'id': 'search-results'})
    results_row = results.find_all('li', 'result-row')

    # print(results.prettify())

    """
    This code only scraps the first 2 pages. If you want to scrap all pages you can comment line 43 and instead run line 44.
    This will take a long time.
    """
    for i in range(0, 2):
    # for i in total_pages:
        
        params = {
            's': i * 120        # 120 items per page
        }

        response = requests.get(base_url, params=params)
        # print('Processing Page {0}'.format(i+1))

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        results = soup.find('ul', {'id': 'search-results'})
        result_rows = results.find_all('li', 'result-row')

        for result_row in results_row:
            post_datetime = result_row.time['datetime']
            post_id = result_row.h3.a['data-id']
            post_url = result_row.h3.a['href']
            price = result_row.find('span', 'result-price').text[1:]
            location = result_row.find('span', 'result-hood').text if result_row.find('span', 'result-hood') else ''
            post_title = result_row.h3.a.text
        # post_title = furniture_elem.find('a', class_="result-title hdrlnk")

            search_results.append([
                post_datetime, post_id, post_url, price, location, post_title
            ])

            time.sleep(1)

        columns = ('Post Date', 'Post Id', 'Post URL', 'Price', 'Location', 'Post Title')
        df = pd.DataFrame(search_results, columns=columns)

    # print(df)

    # Save to CSV
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Craigslist Results ({timestamp}).csv', index=False)
    
    return df

if __name__ == '__main__':
    craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
    data = get_craigslist_search_results(craigslist_base_url)
    print(data)