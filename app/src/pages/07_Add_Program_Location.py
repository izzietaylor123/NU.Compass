import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()


# Add a section to add a new location to the database
def submit_location():
    st.write("Enter new location information below:")

    location_id = st.text_input("Location ID", "")
    city = st.text_input("City", "")
    country = st.text_input("Country", "")
    description = st.text_area("Description", "")

    if st.button("Submit Location"):
        location_data = {
            "locationID": location_id, "city": city, 
            "country": country, "description": description       
        }
        try:
            response = requests.post("http://api:4000/l/locations", json=location_data)
            
            if response.status_code == 200:
                st.success("Location added successfully!")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

st.title("Location Form")
st.write("Fill in the details below and submit to add a new location.")
submit_location()


def submit_abroad_program():
    st.write("Enter new program information below:")
    