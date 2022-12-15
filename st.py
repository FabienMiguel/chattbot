import streamlit as st

st.title("Testing My app")
st.text_area("This is my app", height=100, key="text_area")
st.text_input("Enter your name",key="name")
st.button("Submit")
for i in range(10):
    st.date_input("Enter your date of birth", min_value=None, max_value=None, value=None, key=f"{i}")
    st.text_input("Enter your name",key=f"{i+11}")
