import streamlit as st
import joblib


model = joblib.load("LinearRegression.pkl")

st.set_page_config(page_title="My App", layout="wide")

st.title("Sales Prediction Dashboard")
st.logo("logo.png", size="large")



ads = st.number_input("Enter Advertisement Amount")

if st.button("Predict"):
    result = model.predict([[ads]])
    st.success(f"Expected Sales : {result}")


# data = dt.getData()
# st.subheader("Training Data")
# st.dataframe(data)


# st.subheader("Advertisement vs Sales")
# st.scatter_chart(data, x="Ads", y="Sales")