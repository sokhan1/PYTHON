#this code is run by jupyter
#you need to download the excel files

import pandas as pd
import numpy as np

df1 =pd.read_csv('tmdb_5000_credits.csv')
df2 =pd.read_csv('tmdb_5000_movies.csv')

df2.head(3)

df1.shape, df2.shape

df1['title'].equals(df2['title'])

df1.columns

df1.columns=['id', 'title', 'cast', 'crew']
df1.columns

df1[['id', 'cast', 'crew']]

df2 = df2.merge(df1[['id', 'cast', 'crew']], on='id')
df2.head(3)

C=df2['vote_average'].mean()
C

m = df2['vote_count'].quantile(0.9)
m

q_movies = df2.copy().loc[df2['vote_count'] >=m ]
q_movies.shape

q_movies['vote_count'].sort_values()

def weight_rating(x, m=m, C=C):
    v= x['vote_count']
    R= x['vote_average']
    return ( v /(v+m)*R)+(m/(m+v)*C)

q_movies['score']=q_movies.apply(weight_rating, axis=1)
q_movies.head(3)

q_movies = q_movies.sort_values('score',ascending=False)
q_movies[['title','vote_count','vote_average','score']].head(10)

pop= df2.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center', # Data visualization
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")










