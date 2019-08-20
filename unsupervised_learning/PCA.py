'''This program creates a model using Principal Component Analysis PCA
which is dimensionality reduction technique applied to the Iris Flowers dataset.
It lets you distill multi-dimensional data down to fewer dimensions, selecting 
new dimensions that preserve variance in the data.
'''

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
from pylab import *

#LOADING THE DATA
iris = load_iris()

#CHECKING THE DATA
numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

#DIMENSION REDUCTION
X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)

#CHECKING THE PROJECTION RESULT
print(pca.components_)

#INFORMATION PRESERVED
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

#PLOTTING THE RESULTS IN THE NEW DIMENSION 
colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
pl.legend()
pl.show()
    