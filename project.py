import streamlit as st  
st.title("welcome to chennai")
name = st.text_input('Enter your name:')
S=st.button("submit")
if S:
    st.write(f"Hi {name}, welcome to chennai")

