import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("titanic_model.pkl", "rb"))

st.title("Titanic Survival Prediction App")

Pclass = st.selectbox("Passenger Class", [1,2,3])
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.number_input("Age", 1, 100)
SibSp = st.number_input("Siblings/Spouse", 0, 10)
Parch = st.number_input("Parents/Children", 0, 10)
Fare = st.number_input("Fare", 0.0, 600.0)

Sex = 1 if Sex == "male" else 0

input_data = pd.DataFrame({
    'Pclass':[Pclass],
    'Sex':[Sex],
    'Age':[Age],
    'SibSp':[SibSp],
    'Parch':[Parch],
    'Fare':[Fare],
    'Embarked_Q':[0],
    'Embarked_S':[1]
})

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")