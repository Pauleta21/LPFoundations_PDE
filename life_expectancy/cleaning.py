import os
import pandas as pd
import numpy as np

def load_data():
    initial_data = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep='\t', header=0)
    return initial_data

def clean_data(initial_data):
    initial_data[['unit', 'sex', 'age','region']] = initial_data['unit,sex,age,geo\\time'].str.split(',', expand=True)
    initial_data = initial_data.drop(['unit,sex,age,geo\\time'], axis=1)

    var_columns = initial_data.iloc[:, 62:66]
    var_values = initial_data.iloc[:, :62]
    data_clean = pd.melt(initial_data, id_vars=var_columns, value_vars=var_values,
                        var_name='year', value_name='value')

    data_clean['year'].replace([np.inf, -np.inf], np.nan, inplace=True)
    data_clean.dropna(subset=['year'], inplace=True)
    data_clean['value'] = data_clean['value'].str.replace('e', '')
    data_clean = data_clean[data_clean['year'] != 'unit']

    data_clean['year'] = pd.to_numeric(data_clean['year'], errors='coerce').astype('int')
    data_clean['value'] = pd.to_numeric(data_clean['value'], errors='coerce').astype('float')
    data_clean.dropna(subset=['value'], inplace=True)

    data_pt = data_clean[data_clean['region'] == 'PT']

    return data_pt

def save_data(data_pt):
    new_directory = os.path.join('life_expectancy/data', 'pt_life_expectancy.csv')
    data_pt.to_csv(new_directory, index=False)

def main_function():
    initial_data = load_data()
    if initial_data is not None:
        data_pt = clean_data(initial_data)
        save_data(data_pt)

if __name__ == "__main__":
    main_function()
