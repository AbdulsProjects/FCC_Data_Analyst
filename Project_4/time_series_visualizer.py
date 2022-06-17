import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = 'date')
df.index = pd.DatetimeIndex(df.index)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


# Draw line plot
def draw_line_plot():
    fig = df.plot(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', figsize = (25, 5))
    fig.set_xlabel('Date')
    fig.set_ylabel('Page Views')
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy() 
    df_bar['year'] = [d.year for d in df_bar.index]
    df_bar['month'] = [d.month for d in df_bar.index]
    # df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    # df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    
    # Draw bar plot
    fig = df_bar.plot.bar(figsize = (10, 10))
    fig.set_ylabel('Average Page Views')
    fig.set_xlabel('Years')
    fig.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title = 'Month')
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
 


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    #Resets the index, making it no-longer the month, but instead numbers again
    df_box.reset_index(inplace=True)
    #Creates a column for year using the 'date' column
    df_box['year'] = [d.year for d in df_box.date]
    #Creates a column with month as a string (d.strftime) and as the first 3 letters ('%b'). Change to numbered months with ('%m'), still as string
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (15,5))
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = ax[0]).set(xlabel = 'Year', ylabel = 'Page Views', title= "Year-wise Box Plot (Trend)")
    sns.boxplot(x = 'month', y = 'value', data = df_box, ax = ax[1]).set(xlabel = 'Month', ylabel = 'Page Views', title = "Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
