# -*- coding: utf-8 -*-
'''This program fabricates some data that shows a roughly linear
relationship between page speed and amount purchased and it creates a
linear regression prediction for the data points'''

# -*- coding: utf-8 -*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats

#GENERATING DATA (linear relationship between page speed and amount purchased)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

#GETTING SOME LINEAR REGRESSION PARAMETERS
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

#CORRELATION COEFFICIENT
print ('R-squared value:', r_value**2 )

#USING SLOPE (inclinação da curva) AND INTERCEPT () TO PLOT PREDICTED VALUES
def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

#SCATTER PLOT
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()