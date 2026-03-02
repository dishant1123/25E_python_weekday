import pandas as pd

movies = pd.read_csv("pandas\movies.csv")

movies.drop(columns= "Unnamed: 0" ,inplace=True)
directors=pd.read_csv("pandas\directors.csv")
directors.drop(columns= "Unnamed: 0" ,inplace=True)


# print(movies.head())
# print(directors.head())

df =movies.merge(directors,left_on="director_id",right_on="id")
df.rename(columns={"id_x":"movie_id"},inplace=True)
df.drop(columns=["id_y"],inplace=True)

# print(df.head())


# task  :1 vote_average >7   ==> select * from movies where vote_average >7
# task  :2 select title , revenue , director_name from movies where vote_average >7 . 
# task :3 Get me the movies which were released in or after 2015 and having vote_average more than 7
"""vote_avg_greater = df.loc[df["vote_average"]>7]
print(vote_avg_greater.head(50))"""

vote = df.loc[df["vote_average"]>7,["title","revenue","director_name"]]
print(vote.head(20))

