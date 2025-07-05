import streamlit as st
import requests

st.set_page_config(page_title="🧾 Add or Update Passenger", layout="centered")
st.title("🧾 Titanic - Add or Update Passenger")
st.caption("Use the form below to **add** a new passenger or **update** an existing one.")

st.divider()

# Mode selector
mode = st.radio("Choose Action:", ["➕ Add", "🛠️ Update"], horizontal=True)

with st.form("passenger_form"):
    passenger_id = st.number_input("🆔 Passenger ID", min_value=1, step=1)
    survived = st.selectbox("🎯 Survived?", options=["0", "1"])
    pclass = st.selectbox("🏷️ Class (1 = 1st, 2 = 2nd, 3 = 3rd)", options=["1", "2", "3"])
    name = st.text_input("🧍 Name")
    sex = st.selectbox("⚧️ Sex", ["male", "female"])
    age = st.number_input("🎂 Age", min_value=0.0)
    sibsp = st.number_input("👨‍👩‍👧 Siblings/Spouses Aboard", min_value=0)
    parch = st.number_input("👶 Parents/Children Aboard", min_value=0)
    ticket = st.text_input("🎫 Ticket")
    fare = st.number_input("💵 Fare", min_value=0.0)
    cabin = st.text_input("🛌 Cabin")
    embarked = st.selectbox("🛳️ Embarked From", options=["C", "Q", "S"])

    submit_button = st.form_submit_button(f"{'Add' if mode.startswith('➕') else 'Update'} Passenger")

    if submit_button:
        if not name:
            st.error("❌ Name is required.")
            st.stop()

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
            "Embarked": embarked,
        }

        if mode.startswith("➕"):
            response = requests.post("http://flask_api:5000/passengers", json=data)
            if response.status_code == 201:
                st.success("✅ Passenger added successfully!")
            else:
                st.error(f"❌ Failed to add passenger: {response.json().get('error', 'Unknown error')}")
        else:
            response = requests.put(f"http://flask_api:5000/passengers/{passenger_id}", json=data)
            if response.status_code == 200:
                st.success("✅ Passenger updated successfully!")
            else:
                st.error(f"❌ Failed to update passenger: {response.json().get('error', 'Unknown error')}")
