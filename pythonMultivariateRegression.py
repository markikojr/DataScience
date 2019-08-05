import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

#ACCESSING THE DATA
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

#CHECKING THE DATA
print (df.head())

#SCALING THE DATA (Standardize features by removing the mean and scaling to unit variance, z = (x - u) / s, u is the mean and s is the std )
scale = StandardScaler()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

#SCALE, FIT, TRNASFORM and CONVERT (Fit to data, then transform it, then convert the frame to its Numpy-array representation.)
X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())

print (X)

#MODEL (A simple ordinary least squares model.)
est = sm.OLS(y, X).fit()

#MODEL SUMMARY
print (est.summary())

#GROUP PRICE BY DOORS AND GET THE MEAN 
print (y.groupby(df.Doors).mean())