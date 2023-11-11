import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import ta

logo_image = "logo.png"
st.sidebar.image(logo_image, width=170)
st.sidebar.title("DCA vs LumpSump Estrategies")

# Seleccionamos las cryptos
tickers = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'XRP-USD',
    'SOL-USD', 'DOT-USD', 'DOGE-USD', 'AVAX-USD', 'LUNA-USD',
    'UNI-USD', 'LINK-USD', 'MATIC-USD', 'LTC-USD', 'BCH-USD',
    'ALGO-USD', 'ATOM-USD', 'XTZ-USD', 'FIL-USD', 'TRX-USD',
    'VET-USD', 'EOS-USD', 'AAVE-USD', 'XLM-USD', 'CRO-USD',
    'FTT-USD', 'MIOTA-USD', 'MKR-USD', 'XEM-USD', 'DASH-USD',
    'NEO-USD', 'BTT-USD', 'XTZ-USD', 'AAVE-USD',
    '1INCH-USD', 'ALICE-USD', 'FARM-USD', 'GALA-USD', 'POWR-USD']

# Desarrollamos los inputs de Streamlit
crypto_selected = st.sidebar.selectbox("Choose a crypto:", tickers)
start = st.sidebar.date_input("Start date:", value=pd.to_datetime("2021-10-31"))
indicator_selected = st.sidebar.multiselect("Select indicators:", ["SMA", "MACD", "Bollinger Bands", "RSI", "Stochastic Oscillator"])
# Creamos una función para obtener datos históricos
def get_data(symbol, start):
    data = yf.download(symbol, start=start)
    return data

# Creamos el dataframe
df = get_data(crypto_selected, start)


st.title(f"Selected crypto: {crypto_selected}")
st.write(
    "This app helps you to analyze a cryptocurrency with trading indicators. "
    "Choose a cryptocurrency, set a start date, and select indicators to visualize on the price chart. Indicators can be selected from the sidebar, and their descriptions will appear below the main chart or above."
)
# Explanation of indicators
if "SMA" in indicator_selected:
    st.write("### Simple Moving Average (SMA)")
    st.write("The Simple Moving Average is a trend-following indicator that calculates the average price of an asset over a specified time period. The SMA is useful for smoothing price data and identifying trends.")
    
if "MACD" in indicator_selected:
    st.write("### Moving Average Convergence Divergence (MACD)")
    st.write("The MACD is a trend-following momentum indicator that shows the relationship between two moving averages of an asset's price. It consists of the MACD line, signal line, and histogram. It is used to identify potential trend reversals and momentum strength.")

if "Bollinger Bands" in indicator_selected:
    st.write("### Bollinger Bands")
    st.write("Bollinger Bands consist of a middle band being an N-period simple moving average (SMA), an upper band at K times an N-period standard deviation above the middle band, and a lower band at K times an N-period standard deviation below the middle band. They are used to identify volatility and potential trend reversals.")

if "RSI" in indicator_selected:
    st.write("### Relative Strength Index (RSI)")
    st.write("The Relative Strength Index is a momentum oscillator that measures the speed and change of price movements. RSI values range from 0 to 100, and readings above 70 indicate that an asset may be overbought, while readings below 30 suggest that it may be oversold.")

if "Stochastic Oscillator" in indicator_selected:
    st.write("### Stochastic Oscillator")
    st.write("The Stochastic Oscillator is a momentum indicator that shows the location of the close relative to the high-low range over a set number of periods. The %K line is the main line, and the %D line is its signal line. Readings above 80 suggest overbought conditions, while readings below 20 suggest oversold conditions.")



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




