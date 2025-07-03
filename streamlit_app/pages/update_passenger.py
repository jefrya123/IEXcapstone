import streamlit as st
import requests

st.set_page_config(page_title="Update Passenger")
st.title("Update Passenger")

with st.form("update_passenger_form"):
    passenger_id = st.number_input("Passenger ID", min_value=1, step=1)
    survived = st.selectbox("Survived", options=["0", "1"])
    pclass = st.selectbox("Pclass", options=["1", "2", "3"])
    name = st.text_input("Name")
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.number_input("Age", min_value=0.0)
    sibsp = st.number_input("SibSp", min_value=0)
    parch = st.number_input("Parch", min_value=0)
    ticket = st.text_input("Ticket")
    fare = st.number_input("Fare", min_value=0.0)
    cabin = st.text_input("Cabin")
    embarked = st.selectbox("Embarked", options=["C", "Q", "S"])
    submitted = st.form_submit_button("Update Passenger")

if submitted:
    payload = {
        "Survived": survived,
        "Pclass": pclass,
        "Name": name,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Ticket": ticket,
        "Fare": fare,
        "Cabin": cabin,
        "Embarked": embarked,
    }

    response = requests.put(f"http://flask_api:5000/passengers/{passenger_id}", json=payload)
    if response.status_code == 200:
        st.success("Passenger updated successfully!")
    else:
        st.error(f"Failed to update passenger: {response.json().get('error', 'Unknown error')}")