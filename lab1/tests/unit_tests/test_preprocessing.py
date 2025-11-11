"""
test_preprocessing.py
------------
Unit tests for data preprocessing functions: load_data, clean_data, and save_data.

This test suite ensures:
    - Data is correctly loaded from CSV
    - Cleaning operations (strip, dropna, deduplicate) are applied correctly
    - Cleaned data is properly saved to disk

Each test uses fixtures defined in `conftest.py` for reproducibility.
"""

import pandas as pd
from pathlib import Path
from lab1.src.lab1.data_preprocessing.preprocessing import load_data, clean_data, save_data



# -------------------------------------------------------------------
#  Expected Columns (for validation)
# -------------------------------------------------------------------
expected_columns = [
    "age",
    "workclass",
    "fnlgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary",
]


# -------------------------------------------------------------------
#  Test: Load Data
# -------------------------------------------------------------------
def test_load_data(raw_census_data_path):
    """Ensure load_data() correctly loads CSV into a valid DataFrame."""

    # Load data from pytest fixture
    df = load_data(raw_census_data_path) 

    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame"

    assert df.shape[0] > 0 , "DataFrame is empty" 

    assert df.shape[1] == len(expected_columns), "DataFrame has unexpected number of columns"


# -------------------------------------------------------------------
#  Test: Clean Data
# -------------------------------------------------------------------
def test_clean_data(raw_census_data_df):
    """Ensure clean_data() removes duplicates, strips whitespace, and drops NaNs."""

    # 👉 YOUR CODE HERE:
    # - Call clean_data() using raw_census_data_df
    # - Check that:
    #   → All column names are stripped (no whitespace)
    #   → No duplicates remain
    #   → No missing values remain
    pass


# -------------------------------------------------------------------
#  Test: Save Data
# -------------------------------------------------------------------
def test_save_data(clean_census_data_df, clean_census_data_path):
    """Ensure save_data() writes cleaned data correctly to expected path."""

    # 👉 YOUR CODE HERE:
    # - Save data using save_data()
    # - Assert that the saved file exists
    # - Read the file back using pandas
    # - Validate:
    #   → Column names are clean (no whitespace)
    #   → No duplicates
    #   → No missing values
    pass
