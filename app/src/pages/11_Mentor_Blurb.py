import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(page_title="About Me: Mentor", layout="centered")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

sID = st.session_state['userID']

title = "👨‍🏫 About Me: Mentor " + st.session_state['first_name']
st.title(title)
st.markdown("---")

st.subheader("🌟 Meet Your Mentor 🌟")
left_col, center_col, right_col = st.columns([1, 2, 1])
with center_col:
    st.image("assets/Tim_Waltz_headshot.png", use_container_width=True)

studentroute = f'http://api:4000/s/get_student/{sID}'
student = requests.get(studentroute).json()

full_name = str(student[0]['fName']) + " " + str(student[0]['lName'])
role = str(student[0]['role'])
blurb = str(student[0]['blurb'])
email = str(student[0]['email'])
first_name = str(student[0]['fName'])

st.markdown(f"### 📖 About {full_name}")
st.write(f"**Role:** {role}")
st.write(f"**Email:** [Contact {first_name}](mailto:{email})")
st.write(f"**Blurb:** {blurb}")


st.markdown("---")
st.markdown(
    f"""
    🤝 **Want to connect with {first_name}?**  
    📧 Email: {email}
    """,
    unsafe_allow_html=True
)