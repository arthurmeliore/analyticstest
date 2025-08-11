import streamlit as st
from streamlit_gtag import st_gtag

st_gtag(
    key="gtag_send_event_a",
    id="G-4BGMRKV2LJ",
    event_name="app_main_page",
    params={
        "event_category": "test_category_a",
        "event_label": "test_label_a",
        "value": 97,
    },
)
#import streamlit.components.v1 as components

# Include Google Analytics tracking code
#with open("google_analytics.html", "r") as f:
#    html_code = f.read()
#    components.html(html_code, height=0)

st.title("Simple Analytics App")
st.write("Welcome to the Simple Analytics App!")

number = st.number_input("Pick a number", min_value=0, max_value=100, value=50)
st.write(f"You picked: {number}")
