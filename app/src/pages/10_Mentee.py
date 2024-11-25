import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Alumni Mentor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('My blurb: learn about me!', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Prediction.py')

if st.button('Take a look at my course, accomodations, and atmosphere ratings!', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

if st.button("Take a look at my mentorship replies!",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')

if st.button("Take a look at my personal mentor view",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')