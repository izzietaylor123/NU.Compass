import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome to London, United Kingdom!")

st.write("NUBound London is a dynamic global experience program for Northeastern University students, \
         offering them the opportunity to spend their first semester abroad in London. \
         The program combines academic coursework, cultural immersion, and professional development, \
         allowing students to explore London’s rich history, diverse culture, and thriving global industries. \
         Participants take classes that focus on global perspectives while engaging in experiential learning, \
         including potential co-op opportunities or internships in sectors like finance, media, and technology. \
         With access to Northeastern’s robust support system and career services, students in NUBound London develop both personally and professionally, \
         building a global mindset and gaining practical experience in one of the world’s most influential cities.")