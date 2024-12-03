import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('View Current Abroad Mentors')
st.write('')
st.write('')
st.write(f"Hello {st.session_state['first_name']}, what would you like to do today?")
