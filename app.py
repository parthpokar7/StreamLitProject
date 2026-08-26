import streamlit as st
import joblib


model = joblib.load("LinearRegression.pkl")

st.set_page_config(page_title="Sales Prediction", page_icon="logo.png", layout="wide")

st.title("Sales Prediction Dashboard")
st.logo("logo.png", size="large")



ads = st.number_input("Enter Advertisement Amount")

if st.button("Predict"):
    result = model.predict([[ads]])
    st.success(f"Expected Sales : {result}")
