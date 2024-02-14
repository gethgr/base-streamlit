import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Jumps Metrics App | SPESS",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
st.sidebar.write("Hey")
st.write("### Hey")

url = "https://sportsmetrics.geth.gr"
response = requests.get(url)
st.write(response)

csv_url = "https://sportsmetrics.geth.gr/storage/NISOPP_POST20_CJ2_2023-12-30_09-44-31.csv"

df = pd.read_csv(csv_url)

df