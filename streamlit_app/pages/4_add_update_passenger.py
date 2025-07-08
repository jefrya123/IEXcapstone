import streamlit as st
import requests
import pandas as pd
st.set_page_config(page_title="🧾 Add or Update Passenger", layout="centered")
st.title("🧾 Titanic - Add or Update Passenger")
st.caption("Use the form below to **add** a new passenger or **update** an existing one.")
st.divider()

try:
    response = requests.get("http://flask_api:5000/passengers")
    if response.status_code == 200:
        passengers = response.json()
        df = pd.DataFrame(passengers)
        next_id = df["PassengerId"].max() + 1

    else:
        st.error("❌ Failed to fetch passenger data. Please check the Flask API.")
        st.stop()
except requests.exceptions.ConnectionError:
    st.error("❌ Unable to connect to the Flask API. Please ensure it is running.")
    st.stop()


# Mode selector
mode = st.radio("Choose Action:", ["➕ Add", "🛠️ Update"], horizontal=True)

embark_options = {
    "Southampton (S)": "S",
    "Cherbourg (C)": "C",
    "Queenstown (Q)": "Q"
}

with st.form("passenger_form"):
    if mode.startswith("➕"):
        st.markdown(f"**Next Passenger ID:** {next_id}")
        passenger_id = next_id
    else:
        passenger_id = st.number_input("🆔 Passenger ID", min_value=1, step=1, help="Enter the ID of the passenger you want to update."
                                       )
    
    pclass = st.selectbox("🏷️ Class (1 = 1st, 2 = 2nd, 3 = 3rd)", options=["1", "2", "3"])
    name = st.text_input("🧍 Name")
    sex = st.selectbox("⚧️ Sex", ["male", "female"])
    age = st.number_input("🎂 Age", min_value=0)
    sibsp = st.number_input("👨‍👩‍👧 Siblings/Spouses Aboard", min_value=0)
    parch = st.number_input("👶 Parents/Children Aboard", min_value=0)
    ticket = st.text_input("🎫 Ticket", placeholder="e.g. A/5 21171")
    fare = st.number_input("💵 Fare", min_value=0.0)
    cabin = st.text_input("🛌 Cabin", placeholder="e.g. C85 or leave blank if unknown")
    embarked_display = st.selectbox("🛳️ Embarked From", options=["Cherbourg", "Queenstown", "Southampton"])
    port_map = {"Cherbourg": "C", "Queenstown": "Q", "Southampton": "S"}
    embarked = port_map[embarked_display]

    submit_button = st.form_submit_button(f"{'Add' if mode.startswith('➕') else 'Update'} Passenger")

if submit_button:
    if not name:
        st.error("❌ Name is required.")
        st.stop()

    # Prepare data dictionary with type conversions to avoid JSON serialization errors
    data = {
        "PassengerId": int(passenger_id),
        "Pclass": int(pclass),
        "Name": name,
        "Sex": sex,
        "Age": float(age),
        "SibSp": int(sibsp),
        "Parch": int(parch),
        "Ticket": ticket,
        "Fare": float(fare),
        "Cabin": cabin,
        "Embarked": embarked,
    }

    # Make request
    if mode.startswith("➕"):
        response = requests.post("http://flask_api:5000/passengers", json=data)
        if response.status_code == 201:
            st.success("✅ Passenger added successfully!")
        else:
            try:
                error_message = response.json().get('error', 'Unknown error')
            except ValueError:
                error_message = response.text
            st.error(f"❌ Failed to add passenger: {error_message}")
    else:
        response = requests.put(f"http://flask_api:5000/passengers/{passenger_id}", json=data)
        if response.status_code == 200:
            st.success("✅ Passenger updated successfully!")
        else:
            try:
                error_message = response.json().get('error', 'Unknown error')
            except ValueError:
                error_message = response.text
            st.error(f"❌ Failed to update passenger: {error_message}")
