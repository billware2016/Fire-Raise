import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

st.title("Selected Crypto:")
logo_image = "logo.png"

st.sidebar.image(logo_image, width = 150)

tickers = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'XRP-USD',
    'SOL-USD', 'DOT-USD', 'DOGE-USD', 'AVAX-USD', 'LUNA-USD',
    'UNI-USD', 'LINK-USD', 'MATIC-USD', 'LTC-USD', 'BCH-USD',
    'ALGO-USD', 'ATOM-USD', 'XTZ-USD', 'FIL-USD', 'TRX-USD',
    'VET-USD', 'EOS-USD', 'AAVE-USD', 'XLM-USD', 'CRO-USD',
    'FTT-USD', 'MIOTA-USD', 'MKR-USD', 'XEM-USD', 'DASH-USD',
    'NEO-USD', 'BTT-USD', 'XTZ-USD', 'AAVE-USD',
    '1INCH-USD', 'ALICE-USD', 'FARM-USD', 'GALA-USD', 'POWR-USD']

crypto_selected = st.sidebar.selectbox("Choose a crypto:", tickers)

start = st.sidebar.date_input("Start date:", value = pd.to_datetime("2021-10-31"))

def get_data(symbol, start):
    data = yf.download(symbol, start=start)
    return data

df = get_data(crypto_selected, start)

variable_selected = st.sidebar.selectbox("Choose a variable for analysis:", df.columns.tolist())

#Cuerpo del Dashboard

st.header(crypto_selected)

st.markdown("""### Percentage Change in the Last 24 Hours:""")

change = df.tail(2)

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

high = change["High"].max()
low = change["Low"].min()
vol = round((((low - high)/high)*100),2)

open_price = change["Open"].iloc[0]
close_price = change["Close"].iloc[1]
open_close = round((((close_price - open_price)/open_price)*100),2)

vol1 = change["Volume"].iloc[0]
vol2 = change["Volume"].iloc[1]
volchange = round((((vol2 - vol1)/vol1)*100),2)

close_high = round((((close_price - high)/high)*100), 2)

open_high = round((((high - open_price)/open_price)*100), 2)

col1.write("Volatility")
col1.write(vol)

col5.write("Volume")
col5.write(volchange)

col2.write("Open / Close Ratio")
col2.write(open_close)

col3.write("Close / Max Ratio")
col3.write(close_high)

col4.write("Open / Max Ratio")
col4.write(open_high)

# Análisis Descriptivo

st.subheader("Descriptive Analysis:")

col7, col8 = st.columns(2)
col9, col10 = st.columns(2)

with col7:
    st.subheader("Scatter Plot Open vs Close", divider="blue") 
    fig1 = px.scatter(df,
                    x = "Open",
                    y = "Close",
                    labels = {"Open": "Open Price",
                            "Close": "Close Price"})
    fig1.update_traces(marker=dict(size=5, opacity=0.7))
    fig1.update_layout(template="plotly_dark")
    fig1.update_layout(width=400)

    st.plotly_chart(fig1)

with col8:
    st.subheader("Violin Plot and Data Points", divider = "blue")
    fig2 = px.violin(df, y = variable_selected, box = True, points = "all")
    fig2.update_layout(template = "plotly_dark")
    fig2.update_layout(width=400)

    st.plotly_chart(fig2)

with col9:
    st.subheader("Histogram", divider = "blue")
    fig3 = px.histogram(df, x= variable_selected, nbins=10)
    fig3.update_layout(template="plotly_dark")
    fig3.update_layout(width=400)

    st.plotly_chart(fig3)

with col10:
    st.subheader("Boxplot", divider="blue")
    fig4 = px.box(df, y= variable_selected)
    fig4.update_layout(template="plotly_dark")
    fig4.update_layout(width=400)
    
    st.plotly_chart(fig4)





