import streamlit as st 

# Date range picker that requires beginning and end dates
from streamlit_extras.mandatory_date_range import date_range_picker 
result = date_range_picker("Select a date range")
st.write("Result:", result)

# Notion toggles
from streamlit_extras.stoggle import stoggle 
stoggle(
    "Click Me!",
    """🥷 Surprise! Here's some addtitional content""",
)