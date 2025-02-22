import streamlit as st
import pandas as pd

df = pd.read_csv("movies.csv",delimiter=";")

st.title("This is my first website")

st.header("Machine learning")

st.info("this is information")

st.checkbox("Male")
st.checkbox("female")

#st.selectbox("select any option",["maths","science","english"])
#st.dataframe(df)

a = df["name"].to_list()

selected_movie = st.selectbox("Select any movie",a)
sd = st.button("Recommend")

if sd:
  #st.write("you selected a movie",selected_movie)
  col1,col2,col3 = st.columns(3)

  with col1:
    st.write("this is column one")
  with col2:
    st.write("this is column two")
  with col3:
    st.write("this is column three")



