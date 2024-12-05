import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['program'] = -1

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Hey there alumni Mentor, Tim!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('My blurb: learn about me!', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Student_Blurb.py')

if st.button('Take a look at my course, accomodations, and atmosphere ratings!', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Mentor_Ratings.py')

if st.button("Take a look at my mentorship replies!",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Mentorship_Replies.py')

if st.button("Take a look at my personal mentor view.",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Mentorship_View.py')