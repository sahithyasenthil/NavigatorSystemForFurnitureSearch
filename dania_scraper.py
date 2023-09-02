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
from apify_client import ApifyClient

# Fetch search results from Dania. This requires a token since this is our API source
def get_dania_search_results():
        
    token = "apify_api_Q8Nb6XkPh9ZdZnhkYCZL7BgKB5ZZF531g2xb"
    
    # Initialize the ApifyClient with your API token
    client = ApifyClient(token)

    # Prepare the actor input
    run_input = {
        "maxRequestsPerCrawl": 100,
        "extendOutputFunction": """async ({ data, item, product, images, fns, name, request, variants, context, customData, input, Apify }) => {
    return item;
    }""",
        "extendScraperFunction": """async ({ fns, customData, Apify, label }) => {
    
    }""",
        "customData": {},
        "maxConcurrency": 100,
        "maxRequestRetries": 3,
    }

    # Run the actor and wait for it to finish
    run = client.actor("mshopik/dania-furniture-scraper").call(run_input=run_input)
    list1=[]
    # Fetch and print actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        list1.append(item)
    
    df1 = pd.DataFrame(list1)
    # print(df1)
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df1 = df1[['url','color','size','title','id','description','price','currency','product_type','images_urls','additional']]
    df1.to_csv(f'Dania Results ({timestamp}).csv', index=False)