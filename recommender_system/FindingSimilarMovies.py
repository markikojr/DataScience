'''This program  will construct a user/movie rating matrix.
It is going to use the MovieLens dataset and the corrwith function 
to compute the pairwise correlation of Star Wars movie user rating with every other movie.
'''

import pandas as pd
import numpy as np

#READING RATINGS DATA (READING 3 COLUMNS AND DEFINING THEIR NAMES)
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/home/markjr/Documents/Data_science/recommender_system/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

#READING MOVIES DATA (READING 2 COLUMNS AND DEFINING THEIR NAMES)
m_cols = ['movie_id', 'title']
movies = pd.read_csv('/home/markjr/Documents/Data_science/recommender_system/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

#MERGING FILES
ratings = pd.merge(movies, ratings)

#LOOKING AT THE DATA
print(ratings.head())

#CREATING A TABLE WITH USER_ID AS INDEX, TITLE AS COLUMNS AND RATING AS VALUES (NAN values mean that an user haven't seen the movie)
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieRatings.head())

#GETTING STAR WARS MOVIE RATINGS
starWarsRatings = movieRatings['Star Wars (1977)']
print(starWarsRatings.head())

#GETTING THE CORRELATION BETWEEN STAR WARS AND ALL OTHER MOVIES IN THE DATASET
similarMovies = movieRatings.corrwith(starWarsRatings)

#DROPPING ALL THE NAN VALUES
similarMovies = similarMovies.dropna()

#CREATING A NEW DATAFRAME WITH THE CORRELATED RESULTS
df = pd.DataFrame(similarMovies)
print(df.head(10))

#Our results are probably getting messed up by movies that have only been viewed by 
#people who also happened to like Star Wars. So we need to get rid of movies that 
#were only watched by a few people that are producing spurious results.

#SORTING DESCENDING
similarMovies.sort_values(ascending=False)

#GROUPPING BY TITLE AND GETTING SIZE AND MEAN
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movieStats.head())

#GETTING MOVIES WHERE THE SIZE OF RATINGS ARE >= 300 (WHICH ARE POPULAR MOVIES)
popularMovies = movieStats['rating']['size'] >= 300

#SORTING DESCENDING
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

#ADDING CORREALATION 
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
print(df.head())

#SORTING DESCENDING
df.sort_values(['similarity'], ascending=False)[:15]
print(df.sort_values(['similarity'], ascending=False)[:15])