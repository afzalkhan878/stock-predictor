import yfinance as yf

def load_data(symbol, period='5y'):
    data = yf.download(symbol, period=period)
    data.dropna(inplace=True)
    return data
