# This file contains functions and methods that are used to visualize the results
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt



#read file and convert it to df
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir)) 
processed_file_path = os.path.join(parent_path, 'data', 'processed')
result_file_path = os.path.join(parent_path, 'results')
file_name = 'merged.csv'
file_path = os.path.join(processed_file_path, file_name)
df = pd.read_csv(file_path)
df = df.drop(df.columns[0], axis = 1)



#Line graphs - Regression
genre_list = ['Adventure','Action','Comedy','Drama','Thriller_Suspense','Horror','Romantic_Comedy']
for i in genre_list:
    image_file_name = f'{i}_line.png'
    plot_df = df[df['Genre'] == i]
    plot_df.plot(x='Year', y=['GDP_growth_rate', 'Market Share Delta'], kind='line', marker='o')
    plt.xlabel('Year')
    plt.ylabel('%')
    plt.title(i)
    plt.legend(labels=['GDP Growth Rate', 'Market Share Change Rate']) 
    plt.savefig(os.path.join(result_file_path, image_file_name))

#Scatter plots - Regression
for i in genre_list:
    image_file_name = f'{i}_scatter.png'
    plot_df = df[df['Genre'] == i]
    plot_df.plot.scatter(x='GDP_growth_rate', y='Market Share Delta', marker='o')
    plot_df.plot.scatter(x='GDP_growth_rate', y='Market Share Delta', marker='o')
    plt.xlabel('GDP_growth_rate')
    plt.ylabel('Market Share Change Rate')
    plt.title(i)
    plt.savefig(os.path.join(result_file_path, image_file_name))

#Violin plots - Desc Stats
plt.figure(figsize=(10, 6))
sns.violinplot(x='Genre', y='Market Share', data=df, palette='Set2')
plt.xlabel('Genre')
plt.ylabel('Market Share (%)')
plt.title('Market Share Distribution by Genre')
plt.savefig(os.path.join(result_file_path, 'Market Share Distribution by Genre.png'))


#Bar graph - Desc Stats
desc_file_path = os.path.join(result_file_path, 'desc_stat_result.csv')
desc_df = pd.read_csv(desc_file_path)
plt.figure(figsize=(10, 10))
plt.bar(desc_df['Genre'], desc_df['std'], color='skyblue')
plt.xlabel('Genre')
plt.ylabel('Standard Deviation of Market Share')
plt.title('Market Share Volatility by Genre')
plt.xticks(rotation=45, ha='right')
plt.savefig(os.path.join(result_file_path, 'Market Share Volatility by Genre.png'))


#Heatmap
pivot_df = df.pivot(index='Year', columns='Genre', values='Market Share')
corr_matrix = pivot_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Market Share by Genre')
plt.savefig(os.path.join(result_file_path, 'Correlation Heatmap.png'))