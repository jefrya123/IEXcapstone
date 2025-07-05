import streamlit as st
import pickle
import numpy as np
import os
import pickle

st.set_page_config(page_title="Titanic Survival Prediction")
st.title("Titanic Survival Prediction")

# Load model

model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'titanic_model.pkl')
model_path = os.path.abspath(model_path)
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Form for user input
st.subheader("Enter passenger information:")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)

# Convert categorical input
sex_encoded = 1 if sex == "male" else 0

# Predict
if st.button("Predict Survival"):
    features = np.array([[pclass, sex_encoded, age, sibsp, parch]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("The passenger would have SURVIVED!")
    else:
        st.error("The passenger would NOT have survived.")
