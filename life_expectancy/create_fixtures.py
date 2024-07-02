from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import clean_data

DATA_DIR = Path(__file__).resolve().parent.joinpath("data")
FIXTURE_DIR = Path(__file__).resolve().parent.joinpath("fixtures")

raw_data_dir = DATA_DIR / "eu_life_expectancy_raw.tsv"
raw_data = pd.read_csv(raw_data_dir, sep='\t')

sample_data = raw_data.sample(n=100, random_state=1)

fixture_raw_data_dir = FIXTURE_DIR / "eu_life_expectancy_raw.tsv"
sample_data.to_csv(fixture_raw_data_dir, sep='\t', index=False)

expected_data = clean_data(sample_data)

expected_data_dir = FIXTURE_DIR / "eu_life_expectancy_expected.csv"
expected_data.to_csv(expected_data_dir, sep='\t', index=False)
