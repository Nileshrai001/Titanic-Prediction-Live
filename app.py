import streamlit as st
import pickle
import numpy as np

# Model load karna
with open('titanic.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 0, 80, 25)
fare = st.number_input("Fare", 0, 500, 30)

gender = 0 if sex == "Male" else 1
input_data = np.array([[pclass, gender, age, fare]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Likely to Survive")
    else:
        st.error("Unlikely to Survive")