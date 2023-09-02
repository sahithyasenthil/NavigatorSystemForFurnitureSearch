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


# Fetch search results from AptDeco
def get_aptdeco_search_results(base_url):
    url = base_url + "1"
#   print("Scrape Page: 1")

#   - To extract html file
#   html = urlopen(url)
#   bsyc = BeautifulSoup(html.read(), "lxml")
#   fout = open('aptdeco_html.csv', 'wt', encoding='utf-8')
#   fout.write(str(bsyc))
#   fout.close()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
#   pages = int(soup.find('button', {'class': 'DropdownMenu__DropdownButton-f6rgh0-3 jirxVq'}).find('div', {'class': 'DropdownMenu__DropdownButtonText-f6rgh0-4 cGOHFZ'}).text.split('of ')[1])
    product_results = soup.find_all('div', {'class': 'styles__ProductGridCell-sc-1859r2o-0 bFDJTu'})

#   - To print products html    
#   for product in product_results:
#       print(product.prettify())
        
    products_info = []
    
    for product in product_results:
        title = product.find('div', {'class': 'Card__ItemName-rr6223-2 hKSDjR'}).text
        product_url = 'https://www.aptdeco.com' + product.find('a', {'class': 'Card__CardLink-rr6223-1 gfTIJo'})['href']
        new_price = product.find('div', {'class': 'Flex__Container-sc-14qf74e-0 Flex__Row-sc-14qf74e-1 dVjRzf djUejJ'}).text
        separator_new_index = new_price.index('•')-1
        if product.find('s', {'class': 'Card__StrikeThrough-rr6223-3 iwsrff'}) != None:
            new_price_index = new_price.index('$',1)
            new_price = new_price[new_price_index:separator_new_index]
        else:
            separator_new_index = new_price.index('•')-1
            new_price = new_price[:separator_new_index]
            
        product_page = requests.get(product_url)
        product_soup = BeautifulSoup(product_page.content, "html.parser")
        location = product_soup.find('p', {'class': 'PDPFooter__FooterText-sc-1ngdbbr-5 PDPFooter__SpacedFooterText-sc-1ngdbbr-6 ddMTKT CcsNI'})
        if(location != None):
            location = location.text
            separator_location_index = location.index(':')+2
            location = location[separator_location_index:]
            
        products_info.append([product_url, title, new_price, location])
    
#   print("Finished")
    
    columns = ('Post URL', 'Post Title', 'Price', 'Location')
    df = pd.DataFrame(products_info, columns=columns)
   
#   for page in range(2,pages+1): # - if you want to scrape all pages
    for page in range(2,4):
        url = base_url + str(page)
#       print("Scrape Page: " + str(page))
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        product_results = soup.find_all('div', {'class': 'styles__ProductGridCell-sc-1859r2o-0 bFDJTu'})
        
        products_info = []
    
        # Gather all products 
        for product in product_results:
            title = product.find('div', {'class': 'Card__ItemName-rr6223-2 hKSDjR'}).text
            product_url = 'https://www.aptdeco.com' + product.find('a', {'class': 'Card__CardLink-rr6223-1 gfTIJo'})['href']
            new_price = product.find('div', {'class': 'Flex__Container-sc-14qf74e-0 Flex__Row-sc-14qf74e-1 dVjRzf djUejJ'}).text
            separator_new_index = new_price.index('•')-1
            if product.find('s', {'class': 'Card__StrikeThrough-rr6223-3 iwsrff'}) != None:
                new_price_index = new_price.index('$',1)
                new_price = new_price[new_price_index+1:separator_new_index]
            else:
                separator_new_index = new_price.index('•')-1
                new_price = new_price[:separator_new_index]
            
            product_page = requests.get(product_url)
            product_soup = BeautifulSoup(product_page.content, "html.parser")
            location = product_soup.find('p', {'class': 'PDPFooter__FooterText-sc-1ngdbbr-5 PDPFooter__SpacedFooterText-sc-1ngdbbr-6 ddMTKT CcsNI'})
            if(location != None):
                location = location.text
                separator_location_index = location.index(':')+2
                location = location[separator_location_index:]
            
            df.loc[len(df)] = [product_url, title, new_price, location]
        
#       print("Finished")
        
    # Saves to CSV    
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'AptDeco Results ({timestamp}).csv', index=False)
        
    return df

if __name__ == '__main__':
    aptdeco_base_url = "https://www.aptdeco.com/catalog/furniture?region=Northeast+%28NY%2C+NJ%2C+CT%2C+PA%2C+DE%29&page="
    data = get_aptdeco_search_results(aptdeco_base_url)
    print(data)