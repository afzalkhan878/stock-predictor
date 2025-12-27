import streamlit as st
import yfinance as yf
import numpy as np

st.title("⚠️ Risk Analysis")

ticker = st.text_input("Enter Stock Symbol", "AAPL")
data = yf.download(ticker, period="3y")

returns = data["Close"].pct_change().dropna()

st.write("Volatility:", np.std(returns))
st.write("Mean Return:", np.mean(returns))

st.success("More risk metrics coming shortly 🔥")
