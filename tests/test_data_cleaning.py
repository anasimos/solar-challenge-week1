# tests/test_data_cleaning.py

import pandas as pd
import numpy as np
import sys
import os

# Adjust path to import from scripts/
# Assumes tests/ is in the project root alongside scripts/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))
from scripts.data_cleaning import clean_data # Import your cleaning function

def test_clean_data_returns_dataframe():
    """
    Test that clean_data returns a pandas DataFrame.
    """
    # Create a dummy raw DataFrame for testing
    df_raw = pd.DataFrame({
        'Timestamp': ['2023-01-01 00:00:00', '2023-01-01 01:00:00'],
        'GHI': [100, 150],
        'DNI': [80, 120],
        'DHI': [20, 30],
        'ModA': [50, 70],
        'ModB': [45, 65],
        'Tamb': [25, 24],
        'RH': [70, 75],
        'WS': [2, 3],
        'Comments': ['Good', np.nan]
    })
    cleaned_df = clean_data(df_raw, country_name="TestCountry", save_to_file=False)
    assert isinstance(cleaned_df, pd.DataFrame)

def test_clean_data_handles_negative_values():
    """
    Test that clean_data converts negative GHI to NaN.
    """
    df_raw = pd.DataFrame({
        'Timestamp': ['2023-01-01 00:00:00'],
        'GHI': [-100], # Invalid negative value
        'DNI': [50],
        'DHI': [10],
        'ModA': [20],
        'ModB': [18],
        'Tamb': [20],
        'RH': [60],
        'WS': [1],
        'Comments': ['Test']
    })
    cleaned_df = clean_data(df_raw, country_name="TestCountry", save_to_file=False)
    # After cleaning, -100 should be NaN, and then imputed.
    # So we check if it's no longer negative and is a number.
    assert cleaned_df['GHI'].iloc[0] >= 0

# You would add more comprehensive tests here
# e.g., testing imputation, column types, etc.