import streamlit as st
import streamlit.components.v1 as components

# Include Google Analytics tracking code
with open("google_analytics.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=0)

st.title("Simple Analytics App")
st.write("Welcome to the Simple Analytics App!")

number = st.number_input("Pick a number", min_value=0, max_value=100, value=50)
st.write(f"You picked: {number}")
