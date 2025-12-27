import pandas as pd

def create_features(df):
    df = df[['Close']]
    df['Return'] = df['Close'].pct_change()
    df.dropna(inplace=True)
    return df
