import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Passenger List")
st.title("Passenger List")
st.sidebar.markdown("### 📋 Passengers Info Dashboard")

# Getting Data from API
try:
    response = requests.get("http://flask_api:5000/passengers")
    if response.status_code == 200:
        passengers = response.json()
        df = pd.DataFrame(passengers)
        st.dataframe(df)
    else:
        st.error("Failed to retieve from API.")
except requests.exceptions.ConnectionError:
    st.error("Flask API is not running.")
