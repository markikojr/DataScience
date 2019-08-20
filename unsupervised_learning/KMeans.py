'''This program creates a model using KMeans Clustering 
to get clusters for fake income/age dataset for N people.
Let's make some fake data that includes people clustered
by income and age, randomly.
'''

from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

#Function to create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        #RETURNS A NUMBER IN A UNIFORM DISTRIBUTION
        incomeCentroid = random.uniform(20000.0, 200000.0)          
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])                      
    X = array(X)
    return X
   
#Generating data    
data = createClusteredData(100, 5)

#Checking the data
print(data) 

#Defining the model
model = KMeans(n_clusters=4)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can look at the clusters each data point was assigned to
print(model.labels_)

# And we'll visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()    