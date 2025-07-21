import streamlit as st
from sending_email_feature import send_email

st.set_page_config(layout = 'wide')

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    f"""<h1 style='
        color: black; 
        font-family: "Julius Sans One", sans-serif;
        font-size: 95px; 
        text-align: center;
        '>Contact Me</h1>""", 
        unsafe_allow_html=True)


with st.form(key="send_email_form"):
    user_email = st.text_input(label = "Enter your email address:", key="email")
    raw_message = st.text_area(label = "Enter your message:", key="message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    
    button = st.form_submit_button(label = "Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")