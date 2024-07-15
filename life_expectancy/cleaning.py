from pathlib import Path
import argparse
import pandas as pd

def load_data(path_to_open):
    initial_data = pd.read_csv(path_to_open, sep='\t', header=0)
    return initial_data

def clean_data(initial_data):
    initial_data[['unit', 'sex', 'age','region']] = initial_data['unit,sex,age,geo\\time'].str.split(',', expand=True)
    initial_data = initial_data.drop(['unit,sex,age,geo\\time'], axis=1)

    var_columns = initial_data.iloc[:, 62:66]
    var_values = initial_data.iloc[:, :62]
    data = pd.melt(initial_data, id_vars=var_columns, value_vars=var_values,
                        var_name='year', value_name='value')

    if any(not isinstance(x, int) for x in data['year']):
        data['year'] = pd.to_numeric(data['year'], errors='coerce')

    data.dropna(subset=['year'], inplace=True)

    data['value'] = data['value'].str.replace(r'[^0-9.]', '', regex=True)

    if any(not isinstance(x, float) for x in data['value']):
        data['value'] = pd.to_numeric(data['value'], errors='coerce')

    data.dropna(subset=['value'], inplace=True)

    return data

def save_data(df, path_to_save):
    df.to_csv(path_to_save, index=False)

def main_function(country = 'PT'):
    dir = Path(__file__).resolve().parent
    path_to_open = dir / "data" / "eu_life_expectancy_raw.tsv"
    path_to_save = dir / "data" / f"{country.lower()}_life_expectancy.csv"

    initial_data = load_data(path_to_open)
    data = clean_data(initial_data)
    data_pt = data[data['region'] == country]
    save_data(data_pt, path_to_save)

    return data_pt

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", default="PT", help="Country code to filter the data")
    args = parser.parse_args()
    main_function(args.country)
