import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')
st.write('')
st.write('')
st.write(f"Hello {st.session_state['first_name']}, what would you like to do today?")

if st.button('Current Abroad Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Programs.py')

if st.button("See Mentee Statuses",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/28_Mentee_Management.py')

if st.button("See Mentor Statuses",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Mentor_Management.py')

if st.button('View User Statistics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_IT_Admin_Statistics.py')