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
# task  :4 Print title, vote_average and director_name of top 10 popular movies

"""
vote_avg_greater = df.loc[df["vote_average"]>7]
print(vote_avg_greater.head(50))"""

"""vote = df.loc[df["vote_average"]>7,["title","revenue","director_name"]]
print(vote.head(20))
"""
top_10 = df.sort_values(by="popularity",ascending=False)[["title","vote_average","director_name"]].head(10)
print(top_10)


"""
1.Top 10 popular movies
2.Highest rated (vote_average) movies
3.Number of movies released in a year
4.Movie with the highest budget in a year
5.Most popular director
6.Director producing high budget movies
7.Highest & lowest budget movies every month
8.Directors who did not directed any movie
9.Top 10 most profitable movies
10.Print the titles of the movies directed by Christopher Nolan. Also print their count
Print number of movies directed by each director
"""