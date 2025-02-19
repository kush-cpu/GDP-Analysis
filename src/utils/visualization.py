import pandas as pd
import matplotlib.pyplot as plt

def plot_gdp_trends(data: pd.DataFrame, country: str):
    """
    Plots GDP trends for a specified country.

    Parameters:
    data (pd.DataFrame): DataFrame containing GDP data.
    country (str): The country for which to plot the GDP trends.
    """
    country_data = data[data['Country'] == country]
    plt.figure(figsize=(10, 5))
    plt.plot(country_data['Year'], country_data['GDP'], marker='o')
    plt.title(f'GDP Trends for {country}')
    plt.xlabel('Year')
    plt.ylabel('GDP in Trillions')
    plt.grid()
    plt.show()

def plot_gdp_comparison(data: pd.DataFrame, countries: list):
    """
    Plots a comparison of GDP trends for multiple countries.

    Parameters:
    data (pd.DataFrame): DataFrame containing GDP data.
    countries (list): List of countries to compare.
    """
    plt.figure(figsize=(12, 6))
    for country in countries:
        country_data = data[data['Country'] == country]
        plt.plot(country_data['Year'], country_data['GDP'], marker='o', label=country)
    
    plt.title('GDP Comparison')
    plt.xlabel('Year')
    plt.ylabel('GDP in Trillions')
    plt.legend()
    plt.grid()
    plt.show()