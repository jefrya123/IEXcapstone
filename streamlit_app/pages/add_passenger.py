import streamlit as st
import requests
st.set_page_config(page_title="Add Passenger")
st.title("Add Passenger")

#Input form
with st.form("add_passenger_form"):
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

    submitted = st.form_submit_button("Add Passenger")

    #Send to API
    if submitted:
        data = {
            "PassengerId": passenger_id,
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
            embarked: embarked
        }

        response = requests.post("http://flask_api:5000/passengers", json=data)
        if response.status_code == 201:
            st.success("Passenger added successfully!")
        else:
            st.error(f"Failed to add passenger: {response.json().get('error', 'Unknown error')}")