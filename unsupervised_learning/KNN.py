'''This program creates a model using K-Nearest Neighbors to define some distance
metric between the items in the dataset, and find the K closest items. It is going
to use the MovieLens dataset and tries to guess the rating of a movie by looking at
the 10 movies that are closest to it in terms of genres and popularity.
'''

import pandas as pd
import numpy as np
from scipy import spatial
import operator

#READING RATINGS DATA (READING 3 COLUMNS AND DEFINING THEIR NAMES)
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/home/markjr/Documents/Data_science/unsupervised_learning/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

#LOOKING AT THE DATA
print(ratings.head())

#GROUPPING BY MOVIE_ID AND GETTING RATING SIZE AND MEAN
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print(movieProperties.head())

#CREATING NEW DATAFRAME NORMALIZING THE SIZE VALUE (BETWEEN 0-LESS POPULAR 1-MOST POPULAR)
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print(movieNormalizedNumRatings.head())

#GENRE INFORMATION
movieDict = {}
with open('/home/markjr/Documents/Data_science/unsupervised_learning/ml-100k/u.item', encoding = "ISO-8859-1") as f:
    temp = ''
    for line in f: #LOOPPING OVER LINES
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|') #REMOVING |, 
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

#DEFINING FUNCTION TO COMPUTE THE DISTANCE BETWEEN TWO MOVIES BASED ON GENRES AND POPULARITY
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

#CHECKING DISTANCE OF MOVIES WITH ID 2 AND 4     
print(movieDict[2])
print(movieDict[4])   
print(ComputeDistance(movieDict[2], movieDict[4]))

#DEFINING FUNCTION TO COMPUTE THE DISTANCE BETWEEN SOME TEST MOVIE AND ALL THE MOVIES IN OUR DATASET
def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        #movie is the id number for each movie
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie]) #get distances
            distances.append((movie, dist)) #distances has (id, distances)
    
    #sorting distance values from lower to higher values                                        
    distances.sort(key=operator.itemgetter(1))
    
    neighbors = []
    for x in range(K): #CHECKING THE MOST K MOVIES
        neighbors.append(distances[x][0]) #appending the k lower distances id's, where lower distance        
    return neighbors                      #means the movies are related to each other

K = 10
avgRating = 0
neighbors = getNeighbors(1, K) #calling function choosing movie with id 1 to check the k most
print(movieDict[1])
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3])) #printing the k most movie               
                                                                       #(name,rating mean)
#AVERAGE RATING        
avgRating /= K

print(avgRating)
