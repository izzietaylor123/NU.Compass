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
st.title("Tim's mentor view where he can see all of his mentees")

mentorRoute = f'http://api:4000/s/tim/matches'
mentees = requests.get(mentorRoute).json()

if mentees:
    mentees_df = pd.DataFrame(mentees)

    for index, row in mentees_df.iterrows():
        st.markdown(f"### Mentee {index + 1}: {row['fName']} {row['lName']}")

        st.write(f"**Student ID (sID):** {row['sID']}")
        st.write(f"**First Name:** {row['fName']}")
        st.write(f"**Last Name:** {row['lName']}")
        st.write(f"**Blurb:** {row['blurb']}")

        st.markdown("---")
else:
    st.error("No mentee data available at the moment.")