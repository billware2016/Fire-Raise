import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import ta
from binance.client import Client

client = Client()

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

start = st.sidebar.date_input("Start date:", value = pd.to_datetime("2019-01-01"))

indicator_selected = st.sidebar.multiselect("Select an indicator to analyze:",
                                             ['SMA', 'Bollinger Bands', 'Stochastic Oscillator', 'RSI', 'MACD'])

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

st.title(f"Selected crypto: {crypto_selected}")

# Función para trazar el gráfico de precios

def plot_price(df, indicator_selected):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,
                             y=df["Close"],
                             name="Close Price",
                             line=dict(color="dodgerblue", width=1)))
    
    #Condicional y BB:
    if "Bollinger Bands" in indicator_selected:

        bb = ta.volatility.BollingerBands(df["Close"], window=20)

        fig.add_trace(go.Scatter(x=df.index,
                                 y=bb.bollinger_mavg(),
                                 name="Mean of Bollinger Bands",
                                 line=dict(color="yellow", width=1)
                                 ))
        #Area de las bandas de bollinger
        fig.add_trace(go.Scatter(x=df.index,
                                 y=bb.bollinger_hband(),
                                 fill="tonexty",
                                 fillcolor="rgba(128,128,128,0.3)",
                                 line=dict(color="rgba(128,128,128,0.3)"),
                                 name="High Bollinger Band"
                                 ))
        fig.add_trace(go.Scatter(x=df.index,
                                 y=bb.bollinger_lband(),
                                 fill="tonexty",
                                 fillcolor="rgba(128,128,128,0.3)",
                                 line=dict(color="rgba(128,128,128,0.3)"),
                                 name="Low Bollinger Band"
                                 ))
    fig.update_layout(title=f"{crypto_selected} Price",
                      xaxis_title="Date",
                      yaxis_title="USD",
                      xaxis_rangeslider_visible=True
                      )

    if "SMA" in indicator_selected:

        sma_50 = ta.trend.sma_indicator(df["Close"], window=50)
        sma_200 = ta.trend.sma_indicator(df["Close"], window=200)

        #Agregamos el sma de 50 y 200
        fig.add_trace(go.Scatter(x=df.index,
                                 y=sma_50,
                                 mode="lines",
                                 name="SMA 50",
                                 line=dict(color="orange", width=1)))
        fig.add_trace(go.Scatter(x=df.index,
                                 y=sma_200,
                                 mode="lines",
                                 name="SMA 200",
                                 line=dict(color="purple", width=1)))

        fig.update_layout(title=f"Simple Moving Average (SMA) of {crypto_selected}",
                          xaxis_title="Date",
                          yaxis_title="SMA",
                          xaxis_rangeslider_visible=True,
                          xaxis=dict(tickangle=-45, showgrid=True, gridwidth=0.2, gridcolor="gray"),
                          yaxis=dict(showgrid=True, gridwidth=0.2, gridcolor="gray"),
                          margin=dict(l=10, r=10, t=40, b=10)
                          )

    return fig

def plot_RSI(df):

    rsi = ta.momentum.RSIIndicator(df["Close"])
    rsi_values = rsi.rsi()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index,
                             y=rsi_values,
                             mode="lines",
                             name="RSI",
                             line=dict(color="green", width=1)))
    fig.add_shape(dict(type="line",
                       x0=df.index[0],
                       x1=df.index[-1],
                       y0=30,
                       y1=30,
                       line=dict(color="red", dash="dash")))
    fig.add_shape(dict(type="line",
                       x0=df.index[0],
                       x1=df.index[-1],
                       y0=70,
                       y1=70,
                       line=dict(color="red", dash="dash")
                       ))
    #Personalizamos el diseño del gráfico
    fig.update_layout(title=f"Relative Strength Index (RSI) of {crypto_selected}",
                      xaxis_title="Date",
                      yaxis_title="RSI",
                      xaxis_rangeslider_visible=True,
                      xaxis=dict(tickangle=-45, showgrid=True, gridwidth=0.2, gridcolor="gray"),
                      yaxis=dict(showgrid=True, gridwidth=0.2, gridcolor="gray"),
                      margin=dict(l=10, r=10, t=40, b=10)
                      )

    return fig

def plot_MACD(df):
    
    fig = go.Figure()

    macd = ta.trend.MACD(df["Close"])

    #Agregamos línea del MACD
    fig.add_trace(go.Scatter(x=df.index,
                             y=macd.macd(),
                             mode="lines",
                             name="MACD",
                             line=dict(color="cyan", width=1)))
    #Agregamos la línea de la señal del MACD
    fig.add_trace(go.Scatter(x=df.index,
                             y=macd.macd_signal(),
                             mode="lines",
                             name="Signal MACD",
                             line=dict(color="magenta", width=1)))
    #Creamos el gráfico de barras para la diferencia del MACD
    fig.add_trace(go.Bar(x=df.index,
                         y=macd.macd_diff(),
                         name="Difference MACD",
                         marker=dict(color="gray", opacity=0.5)))
    
    fig.update_layout(title=f"Moving Average Convergence Divergence (MACD) Indicator of {crypto_selected}",
                      xaxis_title="Date",
                      yaxis_title="MACD",
                      xaxis_rangeslider_visible=True,
                      xaxis=dict(tickangle=-45,
                                 showgrid=True,
                                 gridwidth=0.2,
                                 gridcolor="gray"
                                 ),
                      yaxis=dict(showgrid=True,
                                 gridwidth=0.2,
                                 gridcolor="gray"
                                 ),
                      margin=dict(l=10, r=10, t=40, b=10))
    return fig

def plot_SO(df):

    #calculamos el oscilador
    stoch = ta.momentum.StochasticOscillator(high=df["High"], low=df["Low"], close=df["Close"])
    K = stoch.stoch()
    D = stoch.stoch_signal()

    #creamos la figura
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,
                             y=K,
                             mode='lines',
                             name='%K',
                             line=dict(color='blue', width=1)))
    fig.add_trace(go.Scatter(x=df.index,
                             y=D,
                             mode='lines',
                             name='%D',
                             line=dict(color='red', width=1)))

    #agregamos las líneas 80 y 20
    fig.add_shape(dict(type='line',
                       x0=df.index[0],
                       x1=df.index[-1],
                       y0=20,
                       y1=20,
                       line=dict(color='green', dash='dash')))
    fig.add_shape(dict(type='line',
                       x0=df.index[0],
                       x1=df.index[-1],
                       y0=80,
                       y1=80,
                       line=dict(color='red', dash='dash')))

    fig.update_layout(title=f"Stochastic Oscillator of {crypto_selected}",
                      xaxis_title="Date",
                      yaxis_title="Stochastic Oscillator",
                      xaxis_rangeslider_visible=True
                      )

    return fig

# Llamar a las funciones

plot_fig = plot_price(df, indicator_selected)
st.plotly_chart(plot_fig)

if "RSI" in indicator_selected: 
    rsi_fig = plot_RSI(df)
    st.plotly_chart(rsi_fig)

if "MACD" in indicator_selected:
    macd_fig = plot_MACD(df)
    st.plotly_chart(macd_fig)

if "Stochastic Oscillator" in indicator_selected:
    so_fig = plot_SO(df)
    st.plotly_chart(so_fig)




