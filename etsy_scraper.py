"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

# Fetch search results from Etsy
def get_etsy_search_results(base_url):

    search_results = []
    page = 1
    titles = []

    while page < 30:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content,'html')
        for item in soup.select('.wt-grid__item-xs-6'): 
            try: 
                title = item.select('h3')[0].get_text().strip()
                price = item.select('.currency-value')[0].get_text().strip()
                rating = item.find("input", {'name': "rating"}).attrs['value']
                search_results.append([title, price, rating])
            except Exception as e: 
                #raise e 
                b = 0  
        page = page + 1
    

    columns = ('Title', 'Price', 'Rating')
    df = pd.DataFrame(search_results, columns=columns)

    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Etsy Results ({timestamp}).csv', index=False)
    
    return df