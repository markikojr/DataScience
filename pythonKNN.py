import pandas as pd
import numpy as np
from scipy import spatial
import operator

#READING RATINGS DATA (READING 3 COLUMNS AND DEFINING THEIR NAMES)
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/home/markjr/data_science/DataScience/DataScience-Python3/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

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
with open('/home/markjr/data_science/DataScience/DataScience-Python3/ml-100k/u.item', encoding = "ISO-8859-1") as f:
    temp = ''
    for line in f: #LOOPPING OVER LINES
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|') #REMOVING |, 
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

print(movieDict[1])

#DEFINING FUNCTION TO COMPUTE THE DISTANCE BETWEEN TWO MOVIES BASED ON GENRES AND POPULARITY
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance
    
print(ComputeDistance(movieDict[2], movieDict[4]))
print(movieDict[2])
print(movieDict[4])

#DEFINING FUNCTION TO COMPUTE THE DISTANCE BETWEEN SOME TEST MOVIE AND ALL THE MOVIES IN OUR DATASET
def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
            
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K): #CHECKING THE MOST K MOVIES
        neighbors.append(distances[x][0])
    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

#AVERAGE RATING        
avgRating /= K

print(avgRating)
print(movieDict[1])