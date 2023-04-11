import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv', header=0)
    x_df, y_df = [df['Year'],df['CSIRO Adjusted Sea Level']]
    
    df2 = df.loc[df['Year']>=2000]
    x_df2, y_df2 = [df2['Year'],df2['CSIRO Adjusted Sea Level']]

    # Create scatter plot
    fig, axes = plt.subplots()
    plt.scatter(x=x_df, y=y_df)

    # Create first line of best fit
    res = linregress(x_df, y_df)
    axes.axline((0, res.intercept), slope=res.slope, color ='r')
    # Create second line of best fit
    res = linregress(x_df2, y_df2)
    axes.axline((0, res.intercept), slope=res.slope, color ='g')
    # Add labels and title
    axes.set(xlim=(1879,2050),ylim=0, xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()