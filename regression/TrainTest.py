'''This program fabricates some data that shows a non-linear
relationship between page speed and amount purchased and it creates a
Polynomial model prediction for the data points making a comparison 
between train and test data'''

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#GENERATING DATA
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

#SPLITING TRAIN AND TEST DATA
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

#TRAIN DATA TO ARRAY
x = np.array(trainX)
y = np.array(trainY)

#POLYNOMIAL REGRESSION
#GETTING X AND Y POLYNOMIAL FIT (Least squares polynomial fit, Returns a vector of coefficients p that minimises the squared error)
p_values = np.polyfit(x, y, 10)
print('-------')
print ('p_values:',p_values)

#GETTING POLYNOMIAL
p4 = np.poly1d(p_values)
print('-------')
print ('Polynome:',p4)

#GENERATE NUMBERs (START,STOP,#)
xp = np.linspace(0, 7, 100) 

#TEST DATA TO ARRAY
testx = np.array(testX)
testy = np.array(testY)

#R-SQUARED VALUE ON THE TEST DATA
r2 = r2_score(testy, p4(testx))
print('-------')
print('R_squared on test data:',r2)

#R-SQUARED VALUE ON THE TRAIN DATA
r2 = r2_score(np.array(trainY), p4(np.array(trainX)))
print('-------')
print('R_squared on train data:',r2)

#FULL DATA
ax1 = plt.subplot(131)
plt.scatter(pageSpeeds, purchaseAmount)
ax1.set_xlim([0,7])
ax1.set_ylim([-20, 200])
ax1.set_title('Full Data')
ax1.set(xlabel='Page Speed (s)', ylabel='Purchase Amount')

#TRAIN DATA
ax4 = plt.subplot(132)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
ax4.set_xlim([0,7])
ax4.set_ylim([-20, 200])
ax4.set_title('Train Data Fit')
ax4.set(xlabel='Page Speed (s)', ylabel='Purchase Amount')

#TEST DATA
ax5 = plt.subplot(133)
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
ax5.set_xlim([0,7])
ax5.set_ylim([-20, 200])
ax5.set_title('Test Data Fit')
ax5.set(xlabel='Page Speed (s)', ylabel='Purchase Amount')

plt.show()