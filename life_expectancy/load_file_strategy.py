# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
import pandas as pd

class DataLoadStrategy(ABC):
    @abstractmethod
    def load_data(self, path: str) -> pd.DataFrame:
        pass

class CSVDataLoad(DataLoadStrategy):
    def load_data(self, path: str):
        initial_data = pd.read_csv(path, sep='\t', header=0)
        return initial_data

class JSONDataLoad(DataLoadStrategy):
    def load_data(self, path: str):
        initial_data = pd.read_json(path)
        return initial_data

class DataLoaderContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def load(self, path):
        return self.strategy.load_data(path)
