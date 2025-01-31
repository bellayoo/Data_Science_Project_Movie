# This file contains functions and methods that are used to analyze data
import os
import pandas as pd
import statsmodels.api as sm



#read file and convert it to df
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir)) 
processed_file_path = os.path.join(parent_path, 'data', 'processed')
result_file_path = os.path.join(parent_path, 'results')
file_name = 'merged.csv'
file_path = os.path.join(processed_file_path, file_name)
df = pd.read_csv(file_path)
df = df.drop(df.columns[0], axis = 1)

#Regression Analysis
genre_list = ['Adventure','Action','Comedy','Drama','Thriller_Suspense','Horror','Romantic_Comedy']
for i in genre_list:
    plot_df = df[df['Genre'] == i]
    X = plot_df[['GDP_growth_rate']]
    Y = plot_df[['Market Share Delta']]
    X = sm.add_constant(X) 
    model = sm.OLS(Y, X).fit()

    #print & save result as txt file 
    regression_path = os.path.join(result_file_path, f'regression_summary_{i}.txt')
    with open(regression_path, 'w') as f:
        f.write(model.summary().as_text())
    print(model.summary())


#Descriptive Statistics
desc_df = df.groupby('Genre')['Market Share'].describe()
desc_df['range'] = desc_df['max'] - desc_df['min']
desc_df.to_csv(result_file_path+'\desc_stat_result.csv', index=True) 