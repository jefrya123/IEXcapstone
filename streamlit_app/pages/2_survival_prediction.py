import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="Titanic Survival Prediction")
st.title("Titanic Survival Prediction")
st.markdown("---")

# Load model

model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'titanic_model.pkl')
model_path = os.path.abspath(model_path)
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Form for user input


with st.form("Prediction Form"):
    st.subheader("Enter passenger information:")
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Sex", ["Male", "Female"])
    age = st.slider("Age", 1, 80, 25)
    sibsp = st.slider("Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.slider("Parents/Children Aboard", 0, 10, 0)
 
    submitted = st.form_submit_button("Predict Survival")


if submitted:

    sex_encoded = 1 if sex == "Male" else 0

    features = np.array([[pclass, sex_encoded, age, sibsp, parch]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("The passenger is predicted to **survive**! 🎉")
    else:
        st.error("The passenger is predicted to **not survive**. 😢")
