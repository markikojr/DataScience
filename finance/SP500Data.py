'''
This program is going to get tickers (name of sp500 companies) from wikipedia web page, save them to pickle,
load sp500 companies data from web, create a folder 'stock_dfs' to save .csv's for each company, join all .csv's
in one .csv droping 'Open','High','Low','Close','Volume', and save 'Adj Close' as the company name.
'''
import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np

style.use('ggplot')

# Function to interact with page, get source and tables inside source, get first column names inside tables and save using pickle
def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies') # Interact with page
    soup = bs.BeautifulSoup(resp.text,features="lxml") # Get source from page
    #soup = bs.BeautifulSoup(resp.text) 
    table = soup.find('table', {'class':'wikitable sortable'}) # Search for table
    tickers = []
    for row in table.findAll('tr')[1:]: # Iterate through tables
        ticker = row.findAll('td')[0].text # Get first table element text
        ticker = ticker[:-1]
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f: #Save all the names
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

# Call the function (get all the names)
#save_sp500_tickers()  

tickers_true = []
# Function to load the data
def get_data_from_yahoo(reload_sp500=False):
    # Loading the companies names
    if reload_sp500: 
        tickers = save_sp500_tickers()

    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)

    # Check if folder exist (otherwise create folder)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    # Start and end date
    start = dt.datetime(2000,1,1)    
    end = dt.datetime(2016,12,31)   

    tickers_error = []
    # Loop over companies names
    #for ticker in tickers[:25]: # Get some data
    for ticker in tickers: # Get all data
        try:
           print(ticker)
           if not os.path.exists('stock_dfs/{}.csv'.format(ticker)): # If no .csv exists create one
                ticker = ticker.replace('.','-')
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
                tickers_true.append(ticker)
           else:
                print('Already have {}'.format(ticker))
                tickers_true.append(ticker)

        except KeyError:
           print("Error for {}".format(ticker))
           tickers_error.append(ticker)
           pass
    print(tickers_error)

# Call the function to load the data
get_data_from_yahoo()

# Function to join the data from each company in one .csv
def compile_data():
    # Get names of companies
    tickers = tickers_true

    # Create data frame
    main_df = pd.DataFrame()

    # Loop over names get each .csv join all .csv in one file
    #for count, ticker in enumerate(tickers[:25]):
    for count, ticker in enumerate(tickers):
        try:
           df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
           df.set_index('Date', inplace=True)

           df.rename(columns = {'Adj Close':ticker}, inplace=True)
           df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

           if main_df.empty:
               main_df = df
           else:
               main_df = main_df.join(df, how='outer')

           if count % 10 == 0:
               print(count)

        except KeyError:
           print("Error for {}".format(ticker))
           pass

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

# Call frunction to join the data
compile_data()


