import streamlit as st

st.title("Simple Analytics App")
st.write("Welcome to the Simple Analytics App!")

number = st.number_input("Pick a number", min_value=0, max_value=100, value=50)
st.write(f"You picked: {number}")
