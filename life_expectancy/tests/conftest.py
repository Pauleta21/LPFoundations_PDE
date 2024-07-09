"""Pytest configuration file"""
from pathlib import Path
import pandas as pd
import pytest

FIXTURES_DIR = Path(__file__).resolve().parent / "tests" / "fixtures"

@pytest.fixture(scope="session")
def input_data() -> pd.DataFrame:
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep='\t')

@pytest.fixture(scope="session")
def expected_data() -> pd.DataFrame:
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv", sep='\t')
