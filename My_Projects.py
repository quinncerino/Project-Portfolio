import streamlit as st
from csv import DictReader

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
        '>My Projects</h1>""", 
        unsafe_allow_html=True)

col1, middle, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    with open("projects.csv") as file:
        csv_reader = list(DictReader(file, delimiter=";"))
        for index, row in enumerate(csv_reader[:4]):
            st.header(row['title'])
            st.write(row['description'])
            st.markdown(f"""
    <div style='font-size:30px; margin-bottom: 20px;'>
        {row['emojis']}</span>
    </div>""", unsafe_allow_html=True)
            if row['link']:
                st.write(f"[Web App Link]({row['link']})")
            st.write(f"[Source Code]({row['url']})")
            st.image("images/" + row['image'])
            st.write(" ")
            st.write(" ")
            st.write(" ")

with col2:
    with open("projects.csv") as file:
        csv_reader = list(DictReader(file, delimiter=";"))
        for index, row in enumerate(csv_reader[4:]):
            st.header(row['title'])
            st.write(row['description'])
            st.markdown(f"""
    <div style='font-size:30px; margin-bottom: 20px;'>
        {row['emojis']}</span>
    </div>""", unsafe_allow_html=True)
            if row['link']:
                st.write(f"[Web App Link]({row['link']})")
            st.write(f"[Source Code]({row['url']})")
            st.image("images/" + row['image'])
            st.write(" ")
            st.write(" ")
            st.write(" ")

