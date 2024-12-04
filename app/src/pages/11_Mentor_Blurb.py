import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(page_title="About Me: Mentor", layout="centered")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title("👨‍🏫 About Me: Mentor Tim")
st.markdown("---")

st.subheader("🌟 Meet Your Mentor 🌟")
left_col, center_col, right_col = st.columns([1, 2, 1])
with center_col:
    st.image("assets/Tim_Waltz_headshot.png", caption="Tim Waltz", use_container_width=True)

timRoute = 'http://api:4000/s/tim'
response = requests.get(timRoute)

if response.status_code == 200:
    timData = response.json()

    if isinstance(timData, list) and len(timData) > 0:
        mentor = timData[0] 

        first_name = mentor.get('fName', 'Tim')
        last_name = mentor.get('lName', 'Waltz')
        role = mentor.get('role', 'Mentor')
        blurb = mentor.get('blurb', 'Tim is passionate about mentoring.')
        email = mentor.get('email', 'w.tim@northeastern.edu')
        
        st.markdown(f"### 📖 About {first_name} {last_name}")
        st.write(f"**Role:** {role}")
        st.write(f"**Email:** [Contact {first_name}](mailto:{email})")
        st.write(f"**Blurb:** {blurb}")
    else:
        st.error("Error on the API!")
else:
    st.error("Failed")

st.markdown("---")
st.markdown(
    """
    🤝 **Want to connect with Tim?**  
    📧 Email: w.tim@northeastern.edu
    """,
    unsafe_allow_html=True
)