import yfinance as yf
import pandas as pd

def load_data(symbol, period="5y"):
    df = yf.download(symbol, period=period)
    df = df[['Open','High','Low','Close','Volume']]
    df.dropna(inplace=True)
    return df
