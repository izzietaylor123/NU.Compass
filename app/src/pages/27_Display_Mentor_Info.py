import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

sID = st.session_state.mentor

mentor_data = requests.get('http://api:4000/s/mentors').json()

# Ensure only specific mentor's profile is being accessed
for mentor in mentor_data:
    if mentor['sID'] == sID:
        selected_mentor = mentor
        break


if selected_mentor:
    last_name = selected_mentor['lName']
    first_name = selected_mentor['fName']
    email = selected_mentor['email']
    blurb = selected_mentor['blurb']
    title = str(last_name) + ", " + str(first_name)

    pg_title = f"Welcome to {last_name}, {first_name}'s Profile:"

    st.title(pg_title)
    st.write(f"Student ID: {selected_mentor['sID']}")
    st.write(f"Full Name: {first_name} {last_name}")
    st.write(f"Email: {email}")
    st.write(f"Here is {first_name}'s blurb:")
        