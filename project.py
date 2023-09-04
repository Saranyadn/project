import streamlit as st  
st.title("welcome DT12-Demo")
name = st.text_input('Enter your name:')
B=st.button("submit")
if B:
    st.write(f"Hi {name},welcome DT12")
    
