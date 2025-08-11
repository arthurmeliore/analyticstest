import streamlit as st
import streamlit.components.v1 as components

# Inject Google Analytics using a hidden HTML component
components.html(
    """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4BGMRKV2LJ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-4BGMRKV2LJ');
    </script>
    """,
    height=0,
    width=0
)

st.title("Simple Analytics App")
st.write("Welcome to the Simple Analytics App!")

number = st.number_input("Pick a number", min_value=0, max_value=100, value=50)
st.write(f"You picked: {number}")
