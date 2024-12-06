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

    location_id = st.text_input("Location ID", "", key="location_id_input")
    city = st.text_input("City", "")
    country = st.text_input("Country", "")
    description = st.text_area("Description", "", key="description_input")

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
with st.expander("Add Location"):
    submit_location()


# Add a section to add a new program to the database
def submit_abroad_program():
    st.write("Enter new program information below:")

    prog_ID = st.text_input("Program ID", "")
    name = st.text_input("Program Name", "")
    description = st.text_input("Program Description", "")
    loc_ID = st.text_input("Location ID", "", key="location_id_program_input")
    ptype = st.text_input("Program Type", "")
    emp_ID = st.text_input("Employee ID", "")
    
    if st.button("Submit Abroad Program"):
        program_data = {
            "programID": prog_ID, "programName": name, "prgmDescription": description, 
            "locationID": loc_ID, "programType": ptype, "empID": emp_ID
        }
        try:
            response = requests.post("http://api:4000/ap/add_abroad_programs", json=program_data)
            
            if response.status_code == 200:
                st.success("Program added successfully!")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

st.title("Abroad Program Form")
st.write("Fill in the details below and submit to add a new program.")
with st.expander("Add Program"):
    submit_abroad_program()