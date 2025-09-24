import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self, limit=5000):
        df = pd.read_csv(self.filepath, nrows=limit)
        return df
