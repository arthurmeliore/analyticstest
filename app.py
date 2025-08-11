import streamlit as st

# Inject Google Analytics tag
st.markdown(
    """
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4BGMRKV2LJ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-4BGMRKV2LJ');
    </script>
    <!-- Google tag (gtag.js) -->
    """,
    unsafe_allow_html=True
)

st.title("Simple Analytics App")
st.write("Welcome to the Simple Analytics App!")

number = st.number_input("Pick a number", min_value=0, max_value=100, value=50)
st.write(f"You picked: {number}")
