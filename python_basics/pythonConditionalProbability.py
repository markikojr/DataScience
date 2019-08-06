#!/usr/bin/python 
#%matplotlib inline

#IMPORTING MODULES
from numpy import random
random.seed(0)

#CREATING DICTIONARIES
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

#LOOPING OVER PEOPLE
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70]) #GETTING AGE
    purchaseProbability = float(ageDecade) / 100.0 #PROBABILITY FOR EACH AGE
    totals[ageDecade] += 1 #COUTING # OF PEOPLE WITH THAT AGE
    if (random.random() < purchaseProbability): #HIGHER AGE HIGHER PROBABILITY
        totalPurchases += 1 #GETTING TOTAL PURCHASES
        purchases[ageDecade] += 1 #GETTING TOTAL PURCHASES PER AGE
        
print ("Total # of people per age =", totals)    
print ("Total purchases per age =", purchases)     
print ("Total purchases =", totalPurchases)     

#P(EF) ( The probability of someone in their 30's buying something is just the percentage of how many 30-year-olds bought something)
PEF = float(purchases[30]) / float(totals[30])
print('P(purchase | 30s): ' + str(PEF))

#P(F) (is just the probability of being 30 in this data set)
PF = float(totals[30]) / 100000.0
print("P(30's): " +  str(PF))

#P(E) (is the overall probability of buying something, regardless of your age)
PE = float(totalPurchases) / 100000.0
print("P(Purchase):" + str(PE))

#P(E)P(F)
print("P(30's)P(Purchase)" + str(PE * PF))