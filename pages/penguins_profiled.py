import streamlit as st 
import pandas as pd 
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report 

st.set_page_config(layout='wide')

st.title("YData Profiling of Penguin Dataset")
df = pd.read_csv("penguins.csv")
pr = df.profile_report()
st_profile_report(pr)