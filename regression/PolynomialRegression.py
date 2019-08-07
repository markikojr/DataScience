from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#GENERATING NON LINEAR DATA
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

#SCATTER PLOT
#plt.scatter(pageSpeeds, purchaseAmount)
#plt.show()

#CREATING POLYNOMIAL MODEL
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)
p4 = np.poly1d(np.polyfit(x, y, 8))

xp = np.linspace(0, 7, 100)

plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')

plt.show()

##CORRELATION COEFFICIENT
r2 = r2_score(y, p4(x))
print ('R-squared value:', r2 )

