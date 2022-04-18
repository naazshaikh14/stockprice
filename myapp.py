import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of GOOGLE


""")

tickerSymbol ='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='id',start='2010-5-31',end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
