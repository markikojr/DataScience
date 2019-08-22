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
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(userRatings.head())

#GETTING THE CORRELATION BETWEEN ALL MOVIES IN THE DATASET IN PAIRS
corrMatrix = userRatings.corr()
print(corrMatrix.head())

#GETTING THE CORRELATION BETWEEN ALL MOVIES IN THE DATASET IN PAIRS (at least 100 views)
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print(corrMatrix.head())

#PRODUCING MOVIES RECOMMENDATIONS FOR USER ID 0
myRatings = userRatings.loc[0].dropna()
print(myRatings)

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))

#ADDING TOGETHER SCORES FROM MOVIES THAT SHOW UP MORE THAN ONCE
simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

#FILTERING OUT MOVIES I'VE ALREADY RATED
filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))