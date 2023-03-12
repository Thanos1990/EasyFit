import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/TA.png")

with col2:
    st.title("Thanos Alevizos")
    content = """
    Hello, I am Thanos. I am a Python programmer and founder of the company xyz. I gratuated in 2013 with a 
    Master of Science in Financial Mathematics from the University College London. I have worked with companies from
    various fields for various mathematical projects.
    """
    st.info(content)