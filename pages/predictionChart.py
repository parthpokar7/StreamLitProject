import streamlit as st
import data as dt

st.title("Prediction Chart")

data = dt.getData()
st.logo("logo.png", size="large")

st.subheader("Advertisement vs Sales")
st.scatter_chart(data, x="Ads", y="Sales")
