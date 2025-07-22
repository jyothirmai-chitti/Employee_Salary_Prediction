import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title("Employee Salary Prediction App")
st.divider()

st.write("This app predicts salary based on Employee ID, Occupation, and Age.")

Employee_ID = st.number_input("Enter the Employee ID", value=0, step=1, min_value=0)

# User inputs occupation as text
occupation_input = st.selectbox("Select Occupation", [
    "Farming-fishing", "Craft-Repair", "Sales", "Tech-Support", 
    "Other-service", "Machine-op-inspct", "Exec-managerial", 
    "Adm-clerical", "Transport-moving", "Handlers-cleaners", 
    "Priv-house-serv", "Prof-specialty", "Protective-serv", "Armed-Forces"
])

age = st.number_input("Enter Age:", step=1, min_value=0)

# Load model and encoder
model = joblib.load("linearmodel.pkl")
le = joblib.load("occupation_encoder.pkl")

# Encode the occupation string
try:
    occupation_encoded = le.transform([occupation_input])[0]
except ValueError:
    st.error("Occupation not recognized. Please choose a valid option.")
    st.stop()

# Final input
x = [Employee_ID, occupation_encoded, age]

predict = st.button("Predict Salary")
st.divider()

if predict:
    st.balloons()
    input_df = pd.DataFrame([x], columns=["Employee_ID", "occupation_encoded", "age"])
    prediction = model.predict(input_df)
    st.write(f"Salary prediction is ₹{prediction[0]:,.2f}")
else:
    st.write("Please press the button to get prediction.")
