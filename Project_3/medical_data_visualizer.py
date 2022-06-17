import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

# Import data
df = pd.read_csv('medical_examination.csv')


# Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100)**2)
df['overweight'] = [1 if x > 25 else 0 for x in df.BMI]


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [0 if x == 1 else 1 for x in df.cholesterol]
df['gluc'] = [0 if x == 1 else 1 for x in df.gluc]




# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Draw the catplot with 'sns.catplot()'       
    fig = sns.catplot(x = 'variable', hue = 'value', order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], col='cardio', data = df_cat, kind = 'count', col_wrap = 2)
    fig.set(ylabel = 'total')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
   

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.drop((df[df.ap_hi < df.ap_lo]).index)
    df_heat = df_heat.drop(df_heat[(df_heat['height'] < df['height'].quantile(0.025))].index)
    df_heat = df_heat.drop(df_heat[(df_heat['height'] > df['height'].quantile(0.975))].index)
    
    df_heat = df_heat.drop(df_heat[(df_heat['weight'] < df['weight'].quantile(0.025))].index)
    df_heat = df_heat.drop(df_heat[(df_heat['weight'] > df['weight'].quantile(0.975))].index)

    df_heat = df_heat.drop(['BMI'],axis = 1)


    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype = np.bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (15,15))


    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, annot = True, fmt = '.1f')
    plt.subplots_adjust(bottom = 0.25, left = 0.15)
    print(type(fig.axes[0]))
    
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
