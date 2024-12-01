import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

# from backend.customers.location_routes.py import get_locations 

from st_keyup import st_keyup


st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Find a location!')
# get_locations()

# Function for each page
def paris_france_page():
    st.switch_page('pages/051_paris.py')
    
def london_uk_page():
    st.switch_page('pages/location_pages/052_london_uk.py')
    
def nice_france_page():
    st.switch_page('pages/location_pages/053_nice_france.py')
    
def berlin_germany_page():
    st.switch_page('pages/location_pages/054_berlin_germany.py')
    

# Mapping each button to its respective page function
location_functions = {
    "Paris, France": paris_france_page,
    "London, United Kingdom": london_uk_page,
    "Nice, France": nice_france_page,
    "Berlin, Germany": berlin_germany_page
}

# Sample list of button titles
button_titles = list(location_functions.keys())

# Search bar to filter buttons
search_query = st.text_input("Search locations: ")

# Filter buttons based on search query (case-insensitive)
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered buttons
for title in filtered_titles:
    if st.button(title):
        # Call the function associated with the button title
        location_functions[title]()
