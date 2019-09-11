'''
This program is going to load the .csv and print some basic info
'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

# Define style
style.use('ggplot')

# Get data
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Return first rows of data
print(df.head())

# Describe data
print(df.describe())

# Inspect the index 
print(df.index)

# Inspect the columns
print(df.columns)

# Check the type of `df`
print(type(df))













































































