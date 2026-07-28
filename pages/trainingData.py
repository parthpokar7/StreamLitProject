import streamlit as st
import data as dt

st.title("Training Data")
st.logo("logo.png", size="large")

data = dt.getData()
st.subheader("Training Data")
st.dataframe(data)