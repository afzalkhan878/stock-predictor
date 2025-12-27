import streamlit as st
from modules.data_loader import load_data
from modules.risk_analyzer import risk_metrics

st.title("⚠️ Risk Analysis")

symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Analyze Risk"):
    df = load_data(symbol)
    metrics = risk_metrics(df)

    st.write(metrics)
    st.success("Risk Evaluated Successfully!")
