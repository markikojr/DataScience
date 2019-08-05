#!/usr/bin/python 
#%matplotlib inline

#IMPORTING MODULES
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.stats as sp
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

print ("------")
print ("Some statistics info:")

#GENERATING RANDOM NUMBERS WITH NORMAL DISTRIBUTION (CENTERED, STD, #)
incomes = np.random.normal(27000, 15000, 10000)

#GETTING THE MEAN VALUE
print ("------")
print ("Mean:", np.mean(incomes))

#GETTING THE MEDIAN VALUE
print ("------")
print ("Median:", np.median(incomes))

#GETTING THE STANDARD DEVIATION VALUE (measure used to quantify the amount of variation or dispersion of a set of data values)
print ("------")
#print ("Standard Deviation:", incomes.std())
print ("Standard Deviation:", np.std(incomes))

#GETTING THE VARIANCE VALUE (measures how far a set of (random) numbers are spread out from their average value.)
print ("------")
#print ("Variance:", incomes.var())
print ("Variance:", np.var(incomes))

#GETTING THE SKEW VALUE (Positive: Distribution to the left; Zero: Symmetrical distribution; Negative: Distribution to the right)
print ("------")
print ("Skew:", sp.skew(incomes))

#GETTING THE KURTOSIS VALUE (measure of the "tailedness" of the probability distribution; measure of outliers present in the distribution)
print ("------")
print ("Kurtosis:", sp.kurtosis(incomes))

#PERCENTILE (measure used in statistics indicating the value below which a given percentage of observations in a group of observations falls)
print ("------")
#print ("Percentile 50:",np.percentile(incomes, 50))
print ("Percentile 80:",np.percentile(incomes, 80))

#GENERATING RANDOM NUNBERS (INITIAL, FINAL, #)
ages = np.random.randint(18, high=90, size=500)

#GETTING THE MODE VALUE
print ("------")
print ("Mode:", stats.mode(ages))

print ("------")
print ("Distributions:")
#CHOOSE DISTRIBUTION (NORMAL:0, 2 OR 3; UNIFORM:1; EXPONENTIAL:4; BINOMIAL:5; POISSON:6)
v = 0

if (v == 0):
   #PLOT HISTOGRAM WITH 50 BINS
   plt.hist(incomes, 50)
   #plt.hist(ages, 50)
   #plt.show()
   d = "Normal Distribution"

if (v == 1):
   #UNIFORM DISTRIBUTION (INITIAL, FINAL, #)
   values = np.random.uniform(-10.0, 10.0, 100000)
   plt.hist(values, 50)
   #plt.show()
   d = "Uniform Distribution"

if (v == 2):
   #NORMAL/GAUSSIAN DISTRIBUTION
   #(INITIAL, FINAL, INCREMENT)
   x = np.arange(-3, 3, 0.001)
   plt.plot(x, norm.pdf(x))
   #plt.show()
   d = "Normal Distribution"

if (v == 3):
   #GENERATING RANDOM NUMBERS WITH NORMAL DISTRIBUTION (CENTERED, STD, #)
   mu = 5.0
   sigma = 2.0
   values = np.random.normal(mu, sigma, 10000)
   plt.hist(values, 50)
   #plt.show()
   d = "Normal Distribution"
   
if (v == 4):
   #EXPONENTIAL PDFnp.percentile
   #(INITIAL, FINAL, INCREMENT)
   x = np.arange(0, 10, 0.001)
   plt.plot(x, expon.pdf(x))
   #plt.show()
   d = "Exponential Distribution"
   
if (v == 5):
   #BINOMIAL PROBABILITY MASS FUNCTION
   #BINOMIAL PARAMETERS n(# of attemps) and p(probability of success)
   n, p = 10, 0.5
   #(INITIAL, FINAL, INCREMENT)
   x = np.arange(0, 10, 0.001)
   plt.plot(x, binom.pmf(x, n, p))
   #plt.show()
   d = "Binomial Distribution"
   
if (v == 6):
   #POISSON PROBABILITY MASS FUNCTION
   mu = 500
   x = np.arange(400, 600, 0.5)
   plt.plot(x, poisson.pmf(x, mu))
   d = "Poisson Distribution"

print ("------")
print ("YOU CHOSE:", d)      
plt.show()
