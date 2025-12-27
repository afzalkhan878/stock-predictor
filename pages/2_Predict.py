import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.title("🔮 Stock Price Prediction")

ticker = st.text_input("Enter Stock Symbol", "AAPL")
data = yf.download(ticker, period="3y")

st.subheader("Historical Price")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="Close Price"))
st.plotly_chart(fig, use_container_width=True)

st.info("Next step: we'll plug LSTM prediction here.")
