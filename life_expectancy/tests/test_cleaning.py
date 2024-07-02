from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import patch

from life_expectancy.cleaning import main_function

FIXTURE_DIR = Path(__file__).resolve().parent.joinpath("fixtures")

@pytest.fixture
def input_data():
    return pd.read_csv(f"{FIXTURE_DIR}/eu_life_expectancy_expected.csv")

@pytest.fixture
def expected():
    return pd.read_csv(f"{FIXTURE_DIR}/pt_life_expectancy_expected.csv")

@patch('life_expectancy.cleaning.load_data')
@patch('life_expectancy.cleaning.clean_data')
@patch('life_expectancy.cleaning.save_data')
def test_main_function(mock_save_data, mock_clean_data, mock_load_data, input_data, expected):
    mock_load_data.return_value = input_data
    mock_clean_data.return_value = expected

    main_function(country='PT')
    mock_save_data.assert_called_once()
    args, kwargs = mock_save_data.call_args
    pd.testing.assert_frame_equal(args[0], expected)
