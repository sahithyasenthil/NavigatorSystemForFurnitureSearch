"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

import os
import pandas as pd
from datetime import datetime
import re

# Get Craigslist
def get_data_craigslist():
    files = os.listdir()
    #print(files)
    files_list = []
    pat = r'^Craigslist Results'
    for file in files:
        if re.search(pat, file) != None:
            files_list.append(file)
    #print(files_list)
    max = files_list[0]
    datetime.strptime(files_list[0][20:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[20:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[20:-5], '%m_%d_%y %H%M%S')):
            max = file
    #print(max)
    df = pd.read_csv(max)
    #print(df)
    return df

# Get Dania
def get_data_dania():
    files = os.listdir()
    files_list = []
    pat = r'^Dania Results'
    for file in files:
        if re.search(pat, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][15:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[15:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[15:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get Etsy
def get_data_etsy():
    files = os.listdir()
    files_list = []
    pat = r'^Etsy Results'
    for file in files:
        if re.search(pat, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][14:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[14:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[14:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get AptDeco
def get_data_aptdeco():    
    files = os.listdir()
    files_list = []
    pat1 = r'^AptDeco Results'
    for file in files:
        if re.search(pat1, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][17:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[17:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[17:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get YellowPages
def get_data_yellowpages():    
    files = os.listdir()
    files_list = []
    pat1 = r'^Yellowpages Results'
    for file in files:
        if re.search(pat1, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][21:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[21:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[21:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get UHaul
def get_data_uhaul():
    files = os.listdir()
    files_list = []
    pat1 = r'^Uhaul Results'
    for file in files:
        if re.search(pat1, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][15:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[15:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[15:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get RealSimple
def get_data_realsimple():
    files = os.listdir()
    files_list = []
    pat1 = r'^RealSimple Results'
    for file in files:
        if re.search(pat1, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][22:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[22:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[22:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df

# Get Ikea
def get_data_ikea():
    files = os.listdir()
    files_list = []
    pat1 = r'^IKEA Results'
    for file in files:
        if re.search(pat1, file) != None:
            files_list.append(file)
    max = files_list[0]
    datetime.strptime(files_list[0][14:-5], '%m_%d_%y %H%M%S')
    for file in files_list:
        if (datetime.strptime(max[14:-5], '%m_%d_%y %H%M%S') < datetime.strptime(file[14:-5], '%m_%d_%y %H%M%S')):
            max = file
    df = pd.read_csv(max)
    return df
    
if __name__ == '__main__':
    get_data_ikea()