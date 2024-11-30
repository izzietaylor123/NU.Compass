import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Mentee, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Reach Out to Your Mentor', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Mentor.py')

if st.button('Contact the Global Experience Office', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_Admin_Home.py')

if st.button('Find location',
             type = 'primary',
             use_container_width = True) :
  st.switch_page('pages/05_Locations.py')

if st.button("Current Programs Ratings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

