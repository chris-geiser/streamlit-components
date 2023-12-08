import streamlit as st 
import pandas as pd 
import plotly.express as px 
from streamlit_plotly_events import plotly_events
import plotly.io as pio
pio.templates.default = "plotly"

st.set_page_config(layout='wide')

st.title("Streamlit Plotly Events Example: Penguins")
df = pd.read_csv("penguins.csv")
fig = px.scatter(
    df,
    x="bill_length_mm",
    y="bill_depth_mm",
    color="species",
    color_discrete_sequence=[
        "#0068c9",
        "#83c9ff",
        "#ff2b2b",
        "#ffabab",
        "#29b09d",
        "#7defa1",
        "#ff8700",
        "#ffd16a",
        "#6d3fc0",
        "#d5dae5",
    ],
)
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
    st.stop()
selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
df_selected = df[(df["bill_length_mm"]==selected_x_value) 
                 & (df["bill_depth_mm"]==selected_y_value)]
st.write("Data for the selected point:")
st.write(df_selected)