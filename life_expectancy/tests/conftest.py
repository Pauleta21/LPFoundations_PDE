"""Pytest configuration file"""
from pathlib import Path
import pandas as pd
import pytest

FIXTURE_DIR = Path(__file__).resolve().parent.joinpath("fixtures")

@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    return pd.read_csv(FIXTURE_DIR / "eu_life_expectancy_raw.csv", sep='\t')

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    return pd.read_csv(FIXTURE_DIR / "eu_life_expectancy_expected.csv", sep='\t')

