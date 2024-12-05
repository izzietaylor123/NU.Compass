import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import json

SideBarLinks()
# Page title
st.title("Tim's mentor view")

userID = st.session_state['userID']

menteeRoute = f'http://api:4000/s/mentors/mentees/{userID}'
mentees = requests.get(menteeRoute).json()

mentorRoute = f'http://api:4000/s/mentors'
mentors = requests.get(mentorRoute).json()

with st.expander("Mentees"):
    if mentees:
        mentees_df = pd.DataFrame(mentees)
        for index, row in mentees_df.iterrows():
            st.markdown(f"### Mentee {index + 1}: {row['fName']} {row['lName']}")
            st.write(f"**First Name:** {row['fName']}")
            st.write(f"**Last Name:** {row['lName']}")
            st.write(f"**Blurb:** {row['blurb']}")
            st.markdown("---")
    else:
        st.error("No mentee data available at the moment.")

with st.expander("Mentors"):
    if mentors:
        mentors_df = pd.DataFrame(mentors)
        for index, row in mentors_df.iterrows():
            st.markdown(f"### Mentor {index + 1}: {row['fName']} {row['lName']}")
            st.write(f"**First Name:** {row['fName']}")
            st.write(f"**Last Name:** {row['lName']}")
            st.write(f"**Blurb:** {row['blurb']}")
            st.markdown("---")
    else:
        st.error("No mentor data available at the moment.")