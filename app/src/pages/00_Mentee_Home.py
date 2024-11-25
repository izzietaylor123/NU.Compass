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

if st.button('Chat with a Mentor', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Simple_Chat_Bot.py')

if st.button('Contact the Global Experience Office', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Global_experience_office.py')

if st.button('Find location',
             type = 'primary',
             use_container_width = True) :
  st.switch_page('pages/05_Locations.py')