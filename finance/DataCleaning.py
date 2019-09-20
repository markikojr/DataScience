'''
This program is going to load the .csv, print some basic info, check missing data,
remove wrong records (zeros and strings not expected and outliers) and save
the data to .csv
'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

# Define style
style.use('ggplot')

# Get data
#df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
df = pd.read_csv('returns_20181228.csv', parse_dates=True, low_memory=True)

# Return first rows of data
print ("-----------CHECKING DATA-------------")
print(df.head())

#print ("-----------CHECKING THE DATA FIRST ROW-------")
print (df.loc[0, "stock_0"])

# Describe data
print ("-----------CHECKING STATISTICS-------------")
print(df.describe())

# Inspect the index 
print ("-----------CHECKING INDEX-------------")
print(df.index)

# Inspect the columns
print ("-----------CHECKING COLUMNS-------------")
print(df.columns)

# Check the type of `df`
print ("-----------CHECKING DATA TYPE-------------")
print(type(df))

#CHECKING MISSING DATA AND CLEANING UP
print ("-----------CHECKING MISSING DATA-------------")
print ("Any Null:",df.isnull().values.any())
print ("Nul Sum Per Column:")
print(df.isnull().sum())
print ("Total Null:",df.isnull().sum().sum())

# Remove NaN values and empty sttings
df.dropna(inplace=True)

#CHECKING AMOUNT DATA AND NAN MESSY DATA 
print ("-----------CHECKING STOCKS DATA AND NAN MESSY DATA--")

del_columns =[]
columns_array = df.columns
#LOOPING OVER ALL STOCKS DATA FOR MESSY INFO
for column in columns_array:
    #print("-----------CHECKING STOCK", column, "------------")
    nzero = 0
    if column == 'Date':
        continue 
    for idx in df.index:
        #print("-----------CHECKING ROW------------")
        #print(column, idx, df[column].loc[idx], type(df[column].loc[idx]))
        try:
            #print ("-----------CHECKING NUMBER------------")
            float(df[column].loc[idx]) # Check if value can be float
            n = float(df[column].loc[idx]) # Check if value can be float
            if (n == 0): # Find zero 
                 #print ("-----------Found 0------------")
                 #print(df[column].loc[idx])
                 #print ("-----------NAN MESSY DATA (zero)------------------")
                 df[column].loc[idx]=np.nan # If it's not a number (maybe a string) convert to NaN value
                 #print(df[column].loc[idx])
                 nzero +=1
                 if nzero > 100: # For columns with more than 10% of zeros
                     del_columns.append(column) 
                     del df[column] # Delete column
                     break
        except ValueError:
            #print ("-----------NAN MESSY DATA (can be float)------------------")
            df[column].loc[idx]=np.nan # If it's not a number (maybe a string) convert to NaN value
            #print(df[column].loc[idx])
            pass

        #if idx == 997: 
        #print(nzero) 

#REMOVING NAN VALUES
df.dropna(inplace=True)

# Return first rows of data
print ("-----------CHECKING DATA-------------")
print(df.head())

# Describe data
print ("-----------CHECKING STATISTICS-------------")
print(df.describe())

#REMOVING COLUMNS WITH ZEROS
print ("-----------LIST OF COLUMNS REMOVED (THOSE WITH ZEROS)-------------")
print(del_columns)

#REMOVING OUTLIERS (it filters out anything beyond two standard deviations of the median value in the data set)
for column in columns_array:
    if column not in del_columns:
        if column == 'Date':
            continue 
        u = df[column].median() # Get the median
        s = df[column].std()    # Get standard deviation
        #print("-----------CHECKING OUTLIERS------------")
    
        for idx in df.index:
            #print (column, idx, u, s, df[column].loc[idx], type(df[column].loc[idx]))
            e = float(df[column].loc[idx]) # Check if value can be float

            if e > (u + (3 * s)) or e < -(u + (3 * s)) : # Check if value is within 3 standard deviations

               #print("-----------FOUND OUTLIER------------")
               #print (u, s, idx, df[column].loc[idx])
               df[column].loc[idx]=np.nan # Convert value to NaN
               #print (u, s, idx, df[column].loc[idx])
         
#REMOVING NAN VALUES
df.dropna(inplace=True)

# Return first rows of data
print ("-----------CHECKING DATA-------------")
print(df.head())

# Describe data
print ("-----------CHECKING STATISTICS-------------")
print(df.describe())

# Save data
df.to_csv('data_corrected.csv')

