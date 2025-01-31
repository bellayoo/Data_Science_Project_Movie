[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7A__rrid)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17102674&assignment_repo_type=AssignmentRepo)

# Analysis of Movie Box Office Trend by Genre 

## Python Version
This project is built using **Python 3.11.9**.

## Python Libraries
To run this project, you will need the following Python libraries:

- `pandas` (for data manipulation)
- `numpy` (for numerical operations)
- `matplotlib` (for data visualization)
- `seaborn` (for data visualization)
- `requests` (for making API requests and web scraping)
- `statsmodels` (for statistical modeling)
- `beautifulsoup4` (for web scraping)
- `fredapi` (for accessing FRED API data)

## Step-by-step Instructions
1. run get_data.py
- It will gather necessary data from FRED API and The Numbers web page. Raw data will be stored in csv format at data/raw directory. - The name of the files are gdp_raw.csv and movie_raw.csv
2. run clean_data.py
- Create three processed files: movie.csv, and gdp.csv, and merged.csv
- 'merged.csv' file is created using the first two files. It is aggregated data set for the analysis
- All the files will be created in data/processed directory
3. run analyze_data.py
- Conduct two types of analysis: OLS regression and descriptive statistics
- OLS regression result summary will be saved as txt files (total of 7 txt files) 
- Descriptive statistcs will be stored as a table in desc_stat_result.csv
- All the result will be saved in the results folder
5. run visualize_results.py
- All the results will be saved in the results folder
- It should create 1 heat map, 1 violin plot, 1 bar graph, 7 scatter plots, 7 line graphs

