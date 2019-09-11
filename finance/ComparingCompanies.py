'''
This program is going to load the stock data from Apple, Microsoft, IBM, and Google, gather 
them into one big DataFrame, calculate and plot the percentage change (returns) from 'Adj Close' in 
histograms and the scatter plot. It is going to calculate short-term and long-term moving average and 
compare them to 'Adj Close'. It calculates the volatily(measurement of the change in variance in the 
returns of a stock over a specific period of time). 
'''
import pandas_datareader.data as web
import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np

import yfinance as yf
yf.pdr_override()

# Function to load tickers, start and end dates, load data from web and concatenate datas 
def get(tickers, startdate, enddate):
  # Function to load data from web
  def data(ticker):
    return (web.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

# Passing companies tickers
tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']

# Call function to load concatenated data
all_data = get(tickers, dt.datetime(2000, 10, 1), dt.datetime(2019, 1, 1))
print(all_data.head())

# RETURNS
#-------------------------
# Isolate the `Adj Close` values and transform the DataFrame
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')

# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

# Plot the distributions
daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

# Plot a scatter matrix with the `daily_pct_change` data
scatter_matrix(daily_pct_change, diagonal='kde', alpha=0.1,figsize=(12,12))
#-------------------------

# MOVING AVERAGE
#-------------------------
# Load Apple data
aapl = web.get_data_yahoo('AAPL', start='2000-10-1', end='2019-1-1')

# Isolate the adjusted closing prices 
adj_close_px = aapl['Adj Close']

# Calculate the moving average
moving_avg = adj_close_px.rolling(window=40).mean()

# Inspect the result
print(moving_avg[-10:])

# Short moving window rolling mean
aapl['40'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean
aapl['252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
aapl[['Adj Close', '40', '252']].plot()
#-------------------------

# VOLATILITY
#-------------------------
# Define the minumum of periods to consider 
min_periods = 75 

# Calculate the volatility
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 

# Plot the volatility
vol.plot(figsize=(10, 8))
#-------------------------

# Show the resulting plot
plt.show()
