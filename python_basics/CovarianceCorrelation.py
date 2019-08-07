import numpy as np
from pylab import *
import matplotlib.pyplot as plt

#DEFINING FUNCTION TO CALCULATE DEVIATIONS FROM THE MEAN
def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

#DEFINING FUNCTION TO GET THE COVARIANCE ("dot product" of both vectors)
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

#DEFINING FUNCTION TO GET THE CORRELATION 
def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  #In real life you'd check for divide by zero here

#GENERATING NUMBERS
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

#CREATING SCATTER PLOT
plt.scatter(pageSpeeds, purchaseAmount)

print ("------")
#GETTING THE COVARIANCE
print("Covariance:", covariance(pageSpeeds, purchaseAmount))

print ("------")
#GETTING THE CORRELATION
print("Correlation:", correlation(pageSpeeds, purchaseAmount))

#FORCING THE RELATION TO BE INVERSE
purchaseAmount = purchaseAmount / pageSpeeds

#CREATING SCATTER PLOT
plt.scatter(pageSpeeds, purchaseAmount)

print ("------")
#GETTING THE COVARIANCE
print("Inverse Covariance:", covariance(pageSpeeds, purchaseAmount))

print ("------")
#GETTING THE CORRELATION
print("Inverse Correlation:", correlation(pageSpeeds, purchaseAmount))

print ("------")
#GETTING THE COVARIANCE
print("Inverse Covariance:", np.cov(pageSpeeds, purchaseAmount))

print ("------")
#GETTING THE CORRELATION
print("Inverse Correlation:", np.corrcoef(pageSpeeds, purchaseAmount))

#FORCING THE RELATION TO BE LINEAR
purchaseAmount = 100 - pageSpeeds * 3

#CREATING SCATTER PLOT
plt.scatter(pageSpeeds, purchaseAmount)

print ("------")
#GETTING THE COVARIANCE
print("Linear Covariance:", np.cov(pageSpeeds, purchaseAmount))

print ("------")
#GETTING THE CORRELATION
print("Linear Correlation:", np.corrcoef(pageSpeeds, purchaseAmount))

#ADJUSTING THE AXES
axes = plt.axes() #CREATING AXES
#axes.set_xlim([-5, 5]) #SETTING X LIMITS
axes.set_ylim([0, 150]) #SETTING Y LIMITS
plt.show()
