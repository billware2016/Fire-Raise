import streamlit as st

logo_image = "logo.png"

st.title("Welcome to Fire&Rise")
st.write(
    "Dive into crypto with Fire&Raise: 35+ assets, real-time analytics, interactive charts, and investment simulations."
    "Elevate your strategy effortlessly Introducing ´Fire&Raise' – Your Premier Streamlit App for Cryptocurrency Enthusiasts.")
st.subheader("Select the application you'd like to explore:")

apps = {
    'crypto_des.py': 'Descriptive Analysis of Cryptocurrency',
    'crypto_at.py': 'Technical Analysis of Cryptocurrency',
    'crypto_invest.py': 'Investment Analysis of Cryptocurrency'
}

selected_app = st.selectbox("App:", list(apps.values()))

selected_script = [key for key, value in apps.items() if value == selected_app][0]

if selected_script == 'crypto_des.py':
    with open('crypto_des.py', 'r', encoding='utf-8') as file:
        exec(file.read())
elif selected_script == 'crypto_at.py':
    with open('crypto_at.py', 'r', encoding='utf-8') as file:
        exec(file.read())
elif selected_script == 'crypto_invest.py':
    with open('crypto_invest.py', 'r', encoding='utf-8') as file:
        exec(file.read())
