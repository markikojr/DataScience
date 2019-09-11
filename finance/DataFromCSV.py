'''
This program is going to load the .csv data, check first rows, print some statistics, check and plot prices.
'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

# Define style
style.use('ggplot')

# Get data
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Return first rows of data
print(df.head())

# Describe data
print(df.describe())

# Check Open and High
print(df[['Open','High']].head())

# Plot 
df[['Open','High']].plot()
plt.show()
