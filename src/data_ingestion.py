import pandas as pd

def load_transactions(path):
    df = pd.read_csv(path)
    df.fillna(0, inplace=True)
    return df