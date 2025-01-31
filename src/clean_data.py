# This file contains functions and methods that are used to clean and preprocess your raw data
import os
import pandas as pd


#create a path to save data
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir)) 
raw_file_path = os.path.join(parent_path, 'data', 'raw')
processed_file_path = os.path.join(parent_path, 'data', 'processed')
os.makedirs(processed_file_path, exist_ok=True)

#GDP Growth Rate data cleaning
def clean_gdp_data():
    #read csv file
    file_name = 'gdp_raw.csv'
    file_path = os.path.join(raw_file_path, file_name)
    df = pd.read_csv(file_path)
    df.rename(columns = {'Unnamed: 0':'date','0':'GDP_growth_rate'}, inplace = True)

    #reformat and filter data
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['Year'] = df['date'].dt.year
    df = df[df['Year'] >= 1995]
    df.reset_index(inplace = True)
    df = df.drop(df.columns[[0,1]], axis = 1)

    #Save the result as csv to the raw folder
    df.to_csv(processed_file_path+'\gdp.csv', index=True) 



#Market Share Precentage data cleaning 
def clean_movie_data():
    #read csv file
    file_name = 'movie_raw.csv'
    file_path = os.path.join(raw_file_path, file_name)
    df = pd.read_csv(file_path)

    #reassign values for year and genre columns
    genre_ID = {1: 'Adventure',2: 'Action',3: 'Comedy',4: 'Drama',5: 'Thriller_Suspense',6: 'Horror',7: 'Romantic_Comedy'}
    year_ID = {
        0: 1995, 1: 1996, 2: 1997, 3: 1998, 4: 1999, 5: 2000, 6: 2001, 7: 2002, 8: 2003,9: 2004, 10: 2005, 11: 2006,
        12: 2007, 13: 2008, 14: 2009, 15: 2010, 16: 2011, 17: 2012, 18: 2013, 19: 2014, 20: 2015, 21: 2016, 22: 2017, 
        23: 2018, 24: 2019, 25: 2020, 26: 2021, 27: 2022, 28: 2023, 29: 2024
    }
    df['Genre'] = df['Genre'].replace(genre_ID)
    df['Year'] = df['Year'].replace(year_ID)

    #filter data and calculate market share change rate
    df['Market Share Delta'] = df.groupby('Genre')['Market Share'].diff()
    df = df[df['Year'].between(1996, 2023)]
    df = df.drop(df.columns[0], axis = 1)
    df = df.reset_index(drop = True)

    df.to_csv(processed_file_path+'\movie.csv', index=True) 


#Merge two data
def aggregate_data():
    #read csv files and create two data frames
    file_name1 = 'movie.csv'
    file_name2 = 'gdp.csv'
    file_path1 = os.path.join(processed_file_path, file_name1)
    file_path2 = os.path.join(processed_file_path, file_name2)
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)

    #merge
    merged_df = pd.merge(df1, df2, on='Year', how='inner')
    merged_df = merged_df[['Year','Genre','Market Share','Market Share Delta','GDP_growth_rate']]
    merged_df.to_csv(processed_file_path+'\merged.csv', index=True) 




clean_gdp_data()
clean_movie_data()
aggregate_data()
