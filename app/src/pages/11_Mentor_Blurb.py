import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(page_title="About Me: Mentor", layout="centered")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title(f"About me, Mentor {st.session_state['first_name']}")

st.subheader("Meet Your Mentor")

st.image("assets/Tim_Waltz_headshot.png", width=200)

st.write("""
I am a second-year Northeastern student studying Business who recently returned from my 
transformative Dialogue of Civilizations in Rome. I’m eager to mentor incoming students 
and help them navigate their global journeys. I aim to share practical advice, 
leave a positive impact, and stay connected with the Dialogue of Civilizations community. 
         
My passion lies in guiding others to unlock their potential. 
Together, we’ll work on building skills, 
overcoming challenges, and exploring new opportunities.

When I’m not mentoring, I enjoy tennis, Stardew Valley, chocolate chip cookies, 
and I’m always on the lookout for new ways to inspire and grow with others. 
I look forward to connecting with you, feel free to reach out to me at w.tim@northeastern.edu!
""")