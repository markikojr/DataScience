'''This program creates a model using Support Vector Machines  
to get clustering from fake income/age clustered data.
Let's make some fake data that includes people clustered
by income and age, randomly. Then classify those clusters in
different color regions.
'''

import numpy as np
from pylab import *
from sklearn import svm, datasets
from numpy import random, float

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(8)
    pointsPerCluster = float(N)/k
    X = []
    y = []
    for i in range (k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y
    
(X, y) = createClusteredData(100, 4)

plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.show()   

#PARTITION GRAPH INTO CLUSTERS
C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X, y)

#setting up a dense mesh of points in the grid and classifying all of them, 
#we can render the regions of each cluster as distinct colors
def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(0, 250000, 10),
                     np.arange(10, 70, 0.5))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
    plt.show()
    
plotPredictions(svc)