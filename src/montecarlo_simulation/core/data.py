import yfinance as yf
import pandas as pd

def extraer_precios(ticker):
    precios = pd.DataFrame()
    precios[ticker] = yf.Ticker(ticker).history(start="2024-01-01")["Close"]
    return precios