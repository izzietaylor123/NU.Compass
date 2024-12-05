import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['program'] = -1

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Mentee, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Reach Out to Your Mentor', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Mentor_Blurb.py')

if st.button('Contact the Global Experience Office', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_GEO_Contact.py')

if st.button('Find Program',
             type = 'primary',
             use_container_width = True) :
  st.switch_page('pages/05_Programs.py')

