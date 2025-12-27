def moving_average(df, window=20):
    return df.Close.rolling(window).mean()
