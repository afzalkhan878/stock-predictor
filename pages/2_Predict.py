import streamlit as st
from modules.data_loader import load_data
from modules.predictor import predict_next
from modules.model_trainer import train_lstm

import os

st.title("🔮 Stock Prediction")

symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Train Model"):
    df = load_data(symbol)
    train_lstm(df)
    st.success("Model trained successfully!")

if st.button("Predict Next Day Price"):
    df = load_data(symbol)
    predicted = predict_next(df)
    st.success(f"Predicted Next Close Price: {predicted:.2f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Close Price"))
    st.plotly_chart(fig, use_container_width=True)
