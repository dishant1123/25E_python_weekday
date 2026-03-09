import pandas as pd
import numpy as np

movies =pd.read_csv('pandas\movies.csv')
directors=pd.read_csv('pandas\directors.csv')

movies.drop(columns= "Unnamed: 0" ,inplace=True)
directors=pd.read_csv("pandas\directors.csv")
directors.drop(columns= "Unnamed: 0" ,inplace=True)


# print(movies.head())
# print(directors.head()) 


"""
task  :1 
Find the total budget of movies released each year. Show only years where total budget > 500M.

SQL  : select year , sum(budget) from movies group by year having sum(budget) > 500000000

"""

# result = movies.groupby("year")['budget'].sum().reset_index()
# result = result[result['budget']>500000000]
# print(result)

"""
task :2 
Find number of movies released in each month. Show only months with more than 5 movies.
"""

"""
task :3 
Find number of movies directed by each director name. Show only directors with more than 2 movies.
"""

df =movies.merge(directors,left_on="director_id",right_on="id")

# print(df.head())
result =df.groupby("director_name")['id_x'].count().reset_index()
result = result[result['id_x']>10]
print(result)

"""
task  :4 
Find average movie budget for each director. Show only directors with average budget > 150M.
"""