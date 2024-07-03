from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import clean_data

#pragma: no cover
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FIXTURE_DIR = BASE_DIR / "tests" / "fixtures"

raw_data_dir = DATA_DIR / "eu_life_expectancy_raw.tsv"
fixture_raw_data_dir = FIXTURE_DIR / "eu_life_expectancy_raw.tsv"
expected_data_dir = FIXTURE_DIR / "eu_life_expectancy_expected.csv"

raw_data = pd.read_csv(raw_data_dir, sep='\t')

sample_data = raw_data.sample(n=100, random_state=1)

sample_data.to_csv(fixture_raw_data_dir, sep='\t', index=False)

expected_data = clean_data(sample_data)

expected_data.to_csv(expected_data_dir, index=False)

print("Fixtures creados correctamente.")
