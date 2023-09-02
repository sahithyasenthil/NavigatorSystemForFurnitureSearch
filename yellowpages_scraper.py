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

# Fetch search results from YellowPages
def get_yellowpages_search_results(base_url, location):

#   fout = open('Yellowpages.txt', 'wt',encoding='utf-8')
#   fclean = open('yellowpages.txt', 'wt')
    search_results = []
    
    url = base_url + location + '&page=3'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    
#   - if you want to scrape all pages
#   totalpage = int(soup.find("div", {'class':'pagination'}).find('span').text.split('of ')[1])//30
#   totalpage += 1
#   print(totalpage)
    
    totalpage = 6
    page = 1
#   titles = []
    while page < totalpage:
        url = base_url + location + '&page=' + str(page)
#       url = f"https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms=Pittsburgh%2C+PA&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
#       fout.write(str(soup))
        mydivs = soup.find_all("div", {"class": "result"})
        for item in mydivs: 
            try: 
#               print('-------------------------')
                post_url = "https://www.yellowpages.com/" + (item.find("a", {'class':'business-name'}).attrs['href'])
                name = (item.find("a", {'class':'business-name'}).find('span').text)
                phone = (item.find("div", {'class':'phones phone primary'}).get_text().strip())
                street_Address = (item.find("div", {'class':'street-address'}).get_text().strip())
                locality = (item.find("div", {'class':'locality'}).get_text().strip())
                business_years = (item.find("div", {'class':'years-in-business'}).get_text().strip())
                search_results.append([post_url, name, phone, street_Address, locality, business_years])
            except: 
                # raise e 
                b = 0
                # print("Failed to Add New Data")
        page = page + 1
    
#   fout.close()
#   fclean.close()    
    
    columns = ('Store URL', 'Name', 'Phone', 'Street_Address','Locality','Business_years')
    df = pd.DataFrame(search_results, columns=columns)
    
    # Save to CSV
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Yellowpages Results ({timestamp}).csv', index=False)
    
    return df

if __name__ == '__main__':
    yellowpages_base_url = "https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms="
    location = 'pittsburgh'
    data = get_yellowpages_search_results(yellowpages_base_url, location)
    print(data)





