import pandas as pd
import numpy as np

def clean_dataframe(df):
    # Remove missing values
    df.dropna(inplace=True)

    # Replace invalid values
    df.replace({'invalid_value': np.nan}, inplace=True)

    # Standardize categorical variables
    df['categorical_column'] = df['categorical_column'].astype('category').cat.codes

    return df
