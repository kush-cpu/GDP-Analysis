import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_gdp_trends(df, countries=None, year_column='Year', gdp_column='GDP'):
    """Plot GDP trends over time for selected countries"""
    plt.figure(figsize=(12, 6))
    if countries:
        df_filtered = df[df['Country'].isin(countries)]
    else:
        df_filtered = df
    
    sns.lineplot(data=df_filtered, x=year_column, y=gdp_column, hue='Country')
    plt.title('GDP Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_gdp_distribution(df, gdp_column='GDP'):
    """Plot GDP distribution using a box plot and histogram"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Box plot
    sns.boxplot(y=df[gdp_column], ax=ax1)
    ax1.set_title('GDP Distribution (Box Plot)')
    
    # Histogram
    sns.histplot(df[gdp_column], ax=ax2, kde=True)
    ax2.set_title('GDP Distribution (Histogram)')
    
    plt.tight_layout()
    plt.show()

def plot_top_economies(df, n=10, gdp_column='GDP'):
    """Plot top n economies by GDP"""
    plt.figure(figsize=(12, 6))
    top_n = df.nlargest(n, gdp_column)
    
    sns.barplot(data=top_n, x='Country', y=gdp_column)
    plt.title(f'Top {n} Economies by GDP')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()