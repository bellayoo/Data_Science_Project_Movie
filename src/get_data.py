# This file contains functions and methods that are used to get the raw data
import os
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from fredapi import Fred

#create a path to save data
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir)) 
file_path = os.path.join(parent_path, 'data', 'raw')
os.makedirs(file_path, exist_ok=True)

#Real GDP Growth Rate from FRED API
def get_gdp_data():
    fred_key = '2059f44e4276f1789469b121dc95653a'
    fred = Fred(api_key = fred_key)
    
    #annual real gdp growth rate series
    gdp = fred.get_series('A191RL1A225NBEA')  
    
    #Save the result as csv to the raw folder
    gdp_raw_df = pd.DataFrame(gdp)
    gdp_raw_df.to_csv(file_path+'\gdp_raw.csv', index=True) 



#Market Share Precentage by Genre from The Numbers 
def get_movie_data():
    #Scrape numbers from the web
    url = 'https://www.the-numbers.com/current/cont/graphs/market/all-items/genre/genres/7/Genres'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    genre_data = ''
    for item in soup:
        if 'data.setValue' in item.text:
            genre_data = item.text
            
    #Store necessary values in a list
    pattern = r"data.setValue\((\d+), (\d+), ([\d.]+)\);" #got help from ChatGPT to get the regular expression of the data entries
    data_entries = re.findall(pattern, genre_data)
    data_entries
    data_list = []
    for entry in data_entries:
        year = int(entry[0])  
        genre = int(entry [1])  
        value = float(entry[2])  
        data_list.append((year, genre, value))

    #Save the result as csv to the raw folder 
    mov_df = pd.DataFrame(data_list, columns=['Year', 'Genre', 'Market Share'])
    mov_df = mov_df[30:]
    mov_df.to_csv(file_path+'\movie_raw.csv', index=True) 

get_gdp_data()
get_movie_data()