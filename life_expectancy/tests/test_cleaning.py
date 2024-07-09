from pathlib import Path
from unittest.mock import patch
import pandas as pd
import pytest

from . import FIXTURES_DIR

from life_expectancy.cleaning import main_function, clean_data

@pytest.fixture
def input_data():
    return pd.read_csv(FIXTURES_DIR/"eu_life_expectancy_raw.tsv", sep = '\t')

@pytest.fixture
def expected_eu():
    return pd.read_csv(FIXTURES_DIR/"eu_life_expectancy_expected.csv", sep = '\t')

@pytest.fixture
def expected_pt():
    return pd.read_csv(FIXTURES_DIR/"pt_life_expectancy_expected.csv")

def test_clean_data(input_data, expected_eu):
    input_data = input_data.drop(['Unnamed: 0'], axis=1)
    expected_eu = expected_eu.drop(['Unnamed: 0'], axis=1)
    cleaned_data = clean_data(input_data)
    cleaned_data.reset_index(drop=True, inplace=True)
    expected_eu.reset_index(drop=True, inplace=True)
    pd.testing.assert_frame_equal(cleaned_data, expected_eu)

@patch('life_expectancy.cleaning.load_data')
@patch('life_expectancy.cleaning.clean_data')
@patch('life_expectancy.cleaning.save_data')
def test_main_function(mock_save_data, mock_clean_data, mock_load_data, input_data, expected_pt):
    mock_load_data.return_value = input_data
    mock_clean_data.return_value = expected_pt

    main_function(country='PT')
    mock_save_data.assert_called_once()
    args, kwargs = mock_save_data.call_args
    pd.testing.assert_frame_equal(args[0], expected_pt)
