def clean_data(df):
    """
    Cleans the input DataFrame by handling missing values and removing duplicates.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be cleaned.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values with the mean of the column
    df.fillna(df.mean(), inplace=True)
    
    return df

def transform_data(df):
    """
    Transforms the input DataFrame by normalizing the GDP values.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be transformed.
    
    Returns:
    pd.DataFrame: The transformed DataFrame with normalized GDP values.
    """
    df['GDP'] = (df['GDP'] - df['GDP'].mean()) / df['GDP'].std()
    return df

def load_data(file_path):
    """
    Loads the data from a CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    import pandas as pd
    return pd.read_csv(file_path)