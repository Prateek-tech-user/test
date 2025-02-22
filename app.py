import streamlit as st
import pandas as pd

df = pd.read_csv("movies.csv",delimiter=";")

st.title("This is my first website")

st.header("Machine learning")

st.info("this is information")

st.checkbox("Male")
st.checkbox("female")

st.selectbox("select any option",["maths","science","english"])
st.dataframe(df)
