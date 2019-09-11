'''
This program is going to load the .csv data with 'Adj Close' for each company, get the correlation
between companies and plot them in a heatmap
'''
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')


def visualize_data():
    # Read the data
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['MMM'].plot()
    #plt.show()

    # Get correlation
    df_corr = df.corr()
    print(df_corr.head())

    data = df_corr.values

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111) # Add subplot

    # Create heatmap for colors
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)

    # Set up ticks and plot    
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)

    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()

# Call the function to plot the correlation between companies
visualize_data()
                  
