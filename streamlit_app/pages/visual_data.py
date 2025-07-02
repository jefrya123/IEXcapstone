import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visual Data")
st.title("Titanic Data")

#Loading data from API
try:
    response = requests.get("http://localhost:5000/passengers")
    if response.status_code == 200:
        passengers = response.json()
        df = pd.DataFrame(passengers)
        st.dataframe(df)
    else:
        st.error("Failed to retrieve data from API.")
except requests.exceptions.ConnectionError:
    st.error("Flask API is not running.")
    st.stop()

#Bar Chart for suvival
st.subheader("Survival Count")
survival_counts = df['Survived'].value_counts().sort_index()
st.bar_chart(survival_counts)

#Pie chart for Class
st.subheader("Passenger Class Distribution")
pclass_counts = df['Pclass'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(pclass_counts, labels=pclass_counts.index, autopct="%1.1f%%")
st.pyplot(fig1)

#Histogram for Age
st.subheader("Age Distribution")
fig2, ax2 = plt.subplots()
df['Age'].dropna().hist(bins=30, ax=ax2)
ax2.set_xlabel('Age')
st.pyplot(fig2)

