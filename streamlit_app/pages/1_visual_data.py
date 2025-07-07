import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visual Data", layout="centered")
st.title("📊 Titanic Data Visualizations")

# -- Fetch passenger data from Flask API --
try:
    response = requests.get("http://flask_api:5000/passengers")
    if response.status_code == 200:
        passengers = response.json()
        df = pd.DataFrame(passengers)
        st.toast("Data loaded successfully!", icon="✅")
    else:
        st.error("Failed to retrieve data from API.")
        st.stop()
except requests.exceptions.ConnectionError:
    st.error("Flask API is not running.")
    st.stop()

# -- Passenger Class Distribution --
st.subheader("Passenger Class Distribution")
pclass_counts = df["Pclass"].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.pie(pclass_counts, labels=[f"Class {i}" for i in pclass_counts.index], autopct="%1.1f%%", startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# -- Age Distribution --
st.subheader("Age Distribution")
fig2, ax2 = plt.subplots()
df["Age"].dropna().hist(bins=30, ax=ax2, color="skyblue", edgecolor="black")
ax2.set_xlabel("Age")
ax2.set_ylabel("Number of Passengers")
st.pyplot(fig2)

# -- Gender Distribution --
st.subheader("Gender Distribution")
gender_counts = df["Sex"].value_counts()
fig3, ax3 = plt.subplots()
ax3.barh(gender_counts.index, gender_counts.values, color=["lightblue", "lightcoral"])
ax3.set_xlabel("Number of Passengers")
ax3.set_ylabel("Gender")
st.pyplot(fig3)

# -- Embarked Port --
st.subheader("Embarkation Port Distribution")
port_map = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
df["Embarked"] = df["Embarked"].map(port_map)

embarked_counts = df["Embarked"].value_counts()
fig4, ax4 = plt.subplots()
wedges, text, autotexts = ax4.pie(
    embarked_counts,
    labels=embarked_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    wedgeprops=dict(width=0.3)
)
ax4.axis("equal")
ax4.axis("equal")
st.pyplot(fig4)