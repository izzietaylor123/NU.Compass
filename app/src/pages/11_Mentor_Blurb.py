import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(page_title="About Me: Mentor", layout="centered")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title(f"About me, Mentor Tim")

st.subheader("Meet Your Mentor")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("assets/Tim_Waltz_headshot.png")


timRoute = f'http://api:4000/s/tim'
timBlurb = requests.get(timRoute).json()

st.write('')
st.write(timBlurb)