'''
This program is going to load the stock data from Apple, Microsoft, IBM, and Google, gather them 
into one big DataFrame. For IBM and Apple it calculates and plot the percentage change (returns)
from 'Adj Close' in scatter plot. Use Machine Learning OLS algoritm to predict comparison between companies. 
'''
import pandas_datareader.data as web
import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import statsmodels.api as sm
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

# Isolate the adjusted closing price
all_adj_close = all_data[['Adj Close']]

# Calculate the returns 
all_returns = np.log(all_adj_close / all_adj_close.shift(1))

# Isolate the AAPL returns 
aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'AAPL']
aapl_returns.index = aapl_returns.index.droplevel('Ticker')

# Isolate the MSFT returns
msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'MSFT']
msft_returns.index = msft_returns.index.droplevel('Ticker')

# Build up a new DataFrame with AAPL and MSFT returns
return_data = pd.concat([aapl_returns, msft_returns], axis=1)[1:]
return_data.columns = ['AAPL', 'MSFT']

# Add a constant 
X = sm.add_constant(return_data['AAPL'])

# Construct the model
model = sm.OLS(return_data['MSFT'],X).fit()

# Print the summary
print(model.summary())

# Plot returns of AAPL and MSFT
plt.plot(return_data['AAPL'], return_data['MSFT'], 'r.')

# Add an axis to the plot
ax = plt.axis()

# Initialize `x`
x = np.linspace(ax[0], ax[1] + 0.01)

# Plot the regression line
plt.plot(x, model.params[0] + model.params[1] * x, 'b', lw=2)

# Show the plot
plt.show()

