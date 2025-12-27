import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Stock AI", layout="wide")

# ----------------- Sidebar -----------------
st.sidebar.title("📊 Stock Market AI App")
stock = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
period = st.sidebar.selectbox("Select Duration", ["6mo","1y","3y","5y"], index=1)

st.sidebar.write("🔔 Example: AAPL, TSLA, MSFT, RELIANCE.NS, TCS.NS")
run = st.sidebar.button("Analyze Stock")

st.title("📈 Stock Market AI Predictor & Risk Analyzer")

if run:

    data = yf.download(stock, period=period)

    if data.empty:
        st.error("❌ Invalid Stock Symbol or Data Unavailable")
    else:
        st.success(f"Loaded data for **{stock}** successfully!")

        # ----------------- Price Chart -----------------
        st.subheader("📉 Price Trend")

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=data.index, y=data["Close"], name="Close Price"
        ))
        fig.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

        # ----------------- Simple Prediction (Trend) -----------------
        st.subheader("🔮 AI Trend Prediction")

        data["Returns"] = data["Close"].pct_change()
        avg_return = data["Returns"].mean()
        volatility = data["Returns"].std()

        if avg_return > 0 and volatility < 0.02:
            verdict = "VERY SAFE & POSITIVE 📗"
            color = "green"
            rec = "Good long-term buy opportunity."
        elif avg_return > 0:
            verdict = "PROMISING BUT VOLATILE 📘"
            color = "blue"
            rec = "Good but unpredictable. Invest carefully."
        elif avg_return < 0 and volatility > 0.03:
            verdict = "RISKY & DOWNWARD 📕"
            color = "red"
            rec = "Avoid for now. High downside risk."
        else:
            verdict = "UNCERTAIN / NEUTRAL ⚪"
            color = "orange"
            rec = "Wait & watch. Not ideal right now."

        st.markdown(
            f"""
            <div style="
                padding:18px;
                border-radius:10px;
                background:#f1f5f9;
                font-size:18px;">
                <b>Verdict:</b> <span style="color:{color};">{verdict}</span><br>
                <b>Recommendation:</b> {rec}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------- Risk Analysis -----------------
        st.subheader("⚠️ Risk Analysis")

        sharpe = (avg_return / volatility) * np.sqrt(252)

        col1,col2,col3 = st.columns(3)
        col1.metric("Volatility", round(volatility*100,2))
        col2.metric("Avg Return %", round(avg_return*100,2))
        col3.metric("Sharpe Ratio", round(sharpe,2))

        if sharpe > 1:
            st.success("This stock has a good risk-adjusted return 👍")
        elif sharpe > 0:
            st.warning("Moderate performance. Not the best, not the worst 😐")
        else:
            st.error("Poor investment from risk perspective 🚨")

else:
    st.info("Enter a stock symbol and click **Analyze Stock** to begin.")
