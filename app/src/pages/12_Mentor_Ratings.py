import logging
import requests # type: ignore
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Mentor Tim Ratings")

# user input
location = st.text_input("Location:", "")

if st.button("Get Ratings"):
    if location.strip():
        try:
            response = requests.get(f"http://api:4000/abroad_programs")
            
            if response.status_code == 200:
                ratings = response.json()
                if not ratings:
                    st.write(f"No ratings found for location: {location}.")
                else:
                    st.write(f"Mentor Ratings for {location}:")
                    for rating in ratings:
                        st.write(f"""
                        **Mentor**: {rating['mentor']}  
                        **Rating**: {rating['rating']}  
                        **Comment**: {rating['comment']}  
                        """)
            else:
                st.error(f"Failed to fetch ratings: {response.status_code}")
        except requests.ConnectionError:
            st.error("Unable to connect to the Flask API. Make sure it's running.")
    else:
        st.error("Please enter a valid location.")