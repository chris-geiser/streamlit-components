import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid

st.set_page_config(layout='wide')

st.title("Streamlit AgGrid Example: Penguins")
penguins_df = pd.read_csv("penguins.csv")

st.write("AgGrid DataFrame")
response = AgGrid(
    penguins_df, 
    height = 500,
    editable = True,
)
df_edited = response["data"]
st.write("Edited DataFrame")
st.dataframe(df_edited)