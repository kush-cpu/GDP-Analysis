import pandas as pd
import numpy as np

def load_data(file_path="D:\\ML Projects\\GDP Analysis\\gdp-analysis\\src\\data\\raw_data.xls", file_type='xls'):
    """
    Load data from either CSV or Excel files
    """
    try:
        if file_type.lower() == 'csv':
            df = pd.read_csv(file_path)
        elif file_type.lower() in ['excel', 'xls', 'xlsx']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type. Use 'csv' or 'excel'")
        
        print(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        return None

def clean_data(df):
    """
    Clean the GDP dataset with improved numeric handling
    """
    if df is None:
        return None
        
    # Create a copy to avoid modifying the original dataframe
    df = df.copy()
    
    # Remove rows with all NaN values
    df = df.dropna(how='all')
    
    # Function to convert string to numeric
    def convert_to_numeric(val):
        if pd.isna(val):
            return np.nan
        if isinstance(val, (int, float)):
            return val
        try:
            # Remove currency symbols, commas and convert to float
            cleaned = str(val).replace('$', '').replace(',', '').strip()
            return float(cleaned)
        except:
            return val

    # Apply conversion to all columns except obvious string columns
    string_columns = ['Country', 'Region', 'Year']  # Add other string columns as needed
    for col in df.columns:
        if col not in string_columns:
            df[col] = df[col].apply(convert_to_numeric)
            # Convert to numeric type, coerce errors to NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
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