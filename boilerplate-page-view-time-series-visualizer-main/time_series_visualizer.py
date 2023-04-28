import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
path = 'FreeCodeCamp/boilerplate-page-view-time-series-visualizer-main/fcc-forum-pageviews.csv'
df = pd.read_csv(path)
df["date"] = df.todatetime(df["date"])
df.set_index("date",inplace = True)

# Clean data
upper_limit = df["value"].quantile(0.025)
lower_limit = df["value"].quantile(0.975)
df = df[(df["value"] <= upper_limit) & (df["value"] >= lower_limit)] 


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    sns.plot(df.index, df["value"])
    ax.xlabel('Date')
    ax.ylabel('Page Views')
    ax.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df["Date"].dt.year
    df['month'] = df["Date"].dt.strftime('%B')

    grouped = df.groupby(['year', 'month'])['value'].mean().reset_index()

    pivot = grouped.pivot(index='year', columns='month', values='value')
  
    # Draw bar plot
    ax = pivot.plot(kind='bar', figsize=(14, 6))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
