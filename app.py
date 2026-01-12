import streamlit as st
import pickle
import numpy as np

with open("titanic.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class(1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", 2, 80, 15)
sibsp = st.number_input("Number of Siblings", 0, 10, 0)
parch = st.number_input("Number of Parents", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 30.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

sex_num = 1 if sex == "male" else 0
embarked_dict = {"C": 0, "Q": 1, "S": 2}
embarked_num = embarked_dict[embarked]
input_data = np.array([[pclass, sex_num, age, sibsp, parch, fare, embarked_num]])

if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("The passenger is likely to survive.")
    else:
        st.error("The passenger is unlikely to survive.")
