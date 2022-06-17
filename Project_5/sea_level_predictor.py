import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
pd.set_option('display.max_columns', None)


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter('Year', 'CSIRO Adjusted Sea Level', data = df)
    # fig = fig.figure
    
    
    # Create first line of best fit
    lin_one = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_fit = np.arange(1880, 2051)
    y_fit = x_fit * lin_one.slope + lin_one.intercept 
    ax.plot(x_fit, y_fit, 'r')
    
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    lin_two = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_fit_two = np.arange(2000, 2051)
    y_fit_two = x_fit_two * lin_two.slope + lin_two.intercept
    ax.plot(x_fit_two, y_fit_two, color='black')

    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

    
draw_plot()
