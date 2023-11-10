import pandas as pd
import streamlit as st
from binance.client import Client
import plotly.express as px


client = Client()

st.title("Selected Crypto:")
logo_image = "logo.png"

st.sidebar.image(logo_image, width = 150)

tickers = ['BTCUSDT','XRPUSDT',
 'TRXUSDT',
 'WAVESUSDT',
 'ZILUSDT',
 'ONEUSDT',
 'COTIUSDT',
 'SOLUSDT',
 'EGLDUSDT',
 'AVAXUSDT',
 'NEARUSDT',
 'FILUSDT',
 'AXSUSDT',
 'ROSEUSDT',
 'ARUSDT',
 'MBOXUSDT',
 'YGGUSDT',
 'BETAUSDT',
 'PEOPLEUSDT',
 'EOSUSDT',
 'ATOMUSDT',
 'FTMUSDT',
 'DUSKUSDT',
 'IOTXUSDT',
 'OGNUSDT',
 'CHRUSDT',
 'MANAUSDT',
 'XEMUSDT',
 'SKLUSDT',
 'ICPUSDT',
 'FLOWUSDT',
 'WAXPUSDT',
 'FIDAUSDT',
 'ENSUSDT',
 'SPELLUSDT',
 'LTCUSDT',
 'IOTAUSDT',
 'LINKUSDT',
 'XMRUSDT',
 'DASHUSDT',
 'MATICUSDT',
 'ALGOUSDT',
 'ANKRUSDT',
 'COSUSDT',
 'KEYUSDT',
 'XTZUSDT',
 'RENUSDT',
 'RVNUSDT',
 'HBARUSDT',
 'BCHUSDT',
 'COMPUSDT',
 'ZENUSDT',
 'SNXUSDT',
 'SXPUSDT',
 'SRMUSDT',
 'SANDUSDT',
 'SUSHIUSDT',
 'YFIIUSDT',
 'KSMUSDT',
 'DIAUSDT',
 'RUNEUSDT',
 'AAVEUSDT',
 '1INCHUSDT',
 'ALICEUSDT',
 'FARMUSDT',
 'REQUSDT',
 'GALAUSDT',
 'POWRUSDT',
 'OMGUSDT',
 'DOGEUSDT',
 'SCUSDT',
 'XVSUSDT',
 'ASRUSDT',
 'CELOUSDT',
 'RAREUSDT',
 'ADXUSDT',
 'CVXUSDT',
 'WINUSDT',
 'C98USDT',
 'FLUXUSDT',
 'ENJUSDT',
 'FUNUSDT',
 'KP3RUSDT',
 'ALCXUSDT',
 'ETCUSDT',
 'THETAUSDT',
 'CVCUSDT',
 'STXUSDT',
 'CRVUSDT',
 'MDXUSDT',
 'DYDXUSDT',
 'OOKIUSDT',
 'CELRUSDT',
 'RSRUSDT',
 'ATMUSDT',
 'LINAUSDT',
 'POLSUSDT',
 'ATAUSDT',
 'RNDRUSDT',
 'NEOUSDT',
 'ALPHAUSDT',
 'XVGUSDT',
 'KLAYUSDT',
 'DFUSDT',
 'VOXELUSDT',
 'LSKUSDT',
 'KNCUSDT',
 'NMRUSDT',
 'MOVRUSDT',
 'PYRUSDT',
 'ZECUSDT',
 'CAKEUSDT',
 'HIVEUSDT',
 'UNIUSDT',
 'SYSUSDT',
 'BNXUSDT',
 'GLMRUSDT',
 'LOKAUSDT',
 'CTSIUSDT',
 'REEFUSDT',
 'AGLDUSDT',
 'MCUSDT',
 'ICXUSDT',
 'TLMUSDT',
 'MASKUSDT',
 'IMXUSDT',
 'XLMUSDT',
 'BELUSDT',
 'HARDUSDT',
 'NULSUSDT',
 'TOMOUSDT',
 'NKNUSDT',
 'BTSUSDT',
 'LTOUSDT',
 'STORJUSDT',
 'ERNUSDT',
 'XECUSDT',
 'ILVUSDT',
 'JOEUSDT',
 'SUNUSDT',
 'ACHUSDT',
 'TROYUSDT',
 'YFIUSDT',
 'CTKUSDT',
 'BANDUSDT',
 'RLCUSDT',
 'TRUUSDT',
 'MITHUSDT',
 'AIONUSDT',
 'ORNUSDT',
 'WRXUSDT',
 'WANUSDT',
 'CHZUSDT',
 'ARPAUSDT',
 'LRCUSDT',
 'IRISUSDT',
 'UTKUSDT',
 'QTUMUSDT',
 'GTOUSDT',
 'MTLUSDT',
 'KAVAUSDT',
 'DREPUSDT',
 'OCEANUSDT',
 'UMAUSDT',
 'FLMUSDT',
 'UNFIUSDT',
 'BADGERUSDT',
 'PONDUSDT',
 'PERPUSDT',
 'TKOUSDT',
 'GTCUSDT',
 'TVKUSDT',
 'MINAUSDT',
 'RAYUSDT',
 'LAZIOUSDT',
 'AMPUSDT',
 'BICOUSDT',
 'CTXCUSDT',
 'FISUSDT',
 'BTGUSDT',
 'TRIBEUSDT',
 'QIUSDT',
 'PORTOUSDT',
 'DATAUSDT',
 'NBSUSDT',
 'EPSUSDT',
 'TFUELUSDT',
 'BEAMUSDT',
 'REPUSDT',
 'PSGUSDT',
 'WTCUSDT',
 'FORTHUSDT',
 'BONDUSDT',
 'ZRXUSDT',
 'FIROUSDT',
 'SFPUSDT',
 'VTHOUSDT',
 'FIOUSDT',
 'PERLUSDT',
 'WINGUSDT',
 'AKROUSDT',
 'BAKEUSDT',
 'ALPACAUSDT',
 'FORUSDT',
 'IDEXUSDT',
 'PLAUSDT',
 'VITEUSDT',
 'DEGOUSDT',
 'XNOUSDT',
 'STMXUSDT',
 'JUVUSDT',
 'STRAXUSDT',
 'CITYUSDT',
 'JASMYUSDT',
 'DEXEUSDT',
 'OMUSDT',
 'MKRUSDT',
 'FXSUSDT',
 'ETHUSDT',
 'ADAUSDT',
'BNBUSDT',
'SHIBUSDT']

crypto_selected = st.sidebar.selectbox("Choose a crypto:", tickers)

start = st.sidebar.date_input("Start date:", value = pd.to_datetime("2021-10-31"))

def get_data(symbol, start):
    start = str(start)
    frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                      "1d",
                                                      start))
    frame = frame.iloc[:,:6]
    frame.columns = ["Time", "Open", "High", "Low", "Close", "Volume"]
    frame.set_index("Time", inplace=True)
    frame.index = pd.to_datetime(frame.index, unit="ms")
    frame = frame.astype(float)
    return frame

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





