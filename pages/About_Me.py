import streamlit as st

st.set_page_config(layout = 'wide')

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    f"""<h1 style='
        color: black; 
        font-family: "Julius Sans One", sans-serif;
        font-size: 90px; 
        text-align: center;
        '>About Me</h1>""", 
        unsafe_allow_html=True)

col1, middle, col2 = st.columns([2.0, 0.1, 2.0])

with col1:
    st.image("images/photo.png")



with col2:
    st.subheader("Hello! My name is Quinn Cerino.")
    st.info("I am an undergraduate student at ECU majoring in Computer Science, which has been a lifelong passion and interest of mine for as long as I can remember. In addition to my coursework, participating in the Spark and HackNC hackathons this past year has enriched my knowledge and skills in the computer science field, as well as participating in opportunities and events like the ECU Technology Summit, which I was fortunate enough to attend and serve as a volunteer at this year. Additionally, I’m very grateful that I’ve been able to connect with and take part in the tech community at ECU this year by serving on the board of the Association for Computing Machinery organization at ECU as PR Chair. I am currently a rising sophomore, and I very much enjoy learning new skills and creating projects in my free time. I'm currently learning/working with Python, HTML/CSS, SQL(SQLite), and C++. Feel free to contact me!")

