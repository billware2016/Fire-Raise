import pandas as pd
from binance.client import Client
import streamlit as st
client = Client()

logo_image = "logo.png"

st.sidebar.image(logo_image, width=170)
st.sidebar.title("DCA vs LumpSump Estrategies")

#2.- Seleccionamos las cryptos

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

#3.- Desarrollamos los inputs de streamlit
dropdown = st.sidebar.selectbox("Choose a crypto:", tickers)

start = st.sidebar.date_input("Start date:", value=pd.to_datetime("2021-10-31"))

investment = st.sidebar.number_input("Choose investment per month:")


#4.- Creamos una funcion para obtener datos históricos

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

#5.- Creamos el dataframe
df = get_data(dropdown, start)

#6.- Creación de fechas de compra y precios de compra
buydates = pd.date_range(df.index[0], df.index[-1], freq="1M")
buyprices = df[df.index.isin(buydates)].Close

#7.- Calculo de la cantidad de criptomonedas compradas
coin_amt = investment/buyprices
coin_amt_LS = investment * len(buyprices) / buyprices[0]

#8.- Calculo del portafolio en la estrategia DCA
coin_amt_sum = coin_amt.cumsum()
coin_amt_sum.name = "coin_amt_DCA"
df_tog = pd.concat([coin_amt_sum, df], axis=1).ffill()
df_tog["Portfolio_DCA"] = df_tog.coin_amt_DCA * df_tog.Close

#9.- Calculo del rendimiento de la estrategia DCA

performance_DCA = (df_tog["Portfolio_DCA"][-1] / (investment * len(buyprices)) - 1)

#10.- Calculo del portafolio en la estrategia LS

df_tog["coin_amt_LS"] = coin_amt_LS
df_tog["Portfolio_LS"] = df_tog.coin_amt_LS * df_tog.Close

#11.- Calculo del rendimiento en la estrategia LS

performance_LS = (df_tog["Portfolio_LS"][-1] / (investment * len(buyprices)) - 1)

#12.- Display de graficos y performance

st.subheader("DCA performance: " + str(round(performance_DCA * 100, 2))+ " %")
st.line_chart(df_tog["Portfolio_DCA"])
st.subheader("LS performance: " + str(round(performance_LS * 100, 2))+ " %")
st.line_chart(df_tog["Portfolio_LS"])





