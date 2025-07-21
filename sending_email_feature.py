import smtplib  #email library
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "quinncerino@gmail.com"
    password = st.secrets["PASSWORD"]

    receiver = "quinncerino@gmail.com"

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)