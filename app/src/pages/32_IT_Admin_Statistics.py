import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title('User Statistics')
st.write('')

# Importing the data
mentor_data = requests.get('http://api:4000/s/mentors').json()
mentee_data = requests.get('http://api:4000/s/mentees').json()

abroad_programs_data = requests.get('http://api:4000/ap/abroad_programs').json()
locations = requests.get('http://api:4000/l/locations').json()

