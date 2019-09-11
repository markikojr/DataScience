'''
This program is going to load the .csv, print some useful info, apply resamplying and make a full comparison between prices.
'''
import matplotlib.pyplot as plt
from matplotlib import style
import mpl_finance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd

# Define style
style.use('ggplot')

# Get the data
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Return first rows of data
print(df.head())

# Describe data
print(df.describe())

# Sample 20 rows
sample = df.sample(20)

# Print `sample`
print(sample)

# Resample to monthly level 
monthly_df = df.resample('M').mean()

# Print `monthly_df`
print(monthly_df)

# Resample open, high, low and close
df_ohlc = df['Adj Close'].resample('10D').ohlc()

# Resample sum
df_volume = df['Volume'].resample('10D').sum()

# Check the data
print(df_ohlc.head())

# Reset index
df_ohlc.reset_index(inplace=True)

# Check the data
print(df_ohlc.head())

# Convert date to number
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# Check the data
print(df_ohlc.head())

# Plot 
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
