import logging
import json
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

# Dynamic Method

# get all locations
location_list = requests.get('http://api:4000/ap/get_all_program_ids').json()


buttons = {}
for programID in location_list: 
    programID = programID['programID']
    cityroute = f'http://api:4000/ap/get_city/{programID}'
    city = requests.get(cityroute).json()
    city = city[0]['city']
    countryroute = f'http://api:4000/ap/get_country/{programID}'
    country = requests.get(countryroute).json()
    country = country[0]['country']
    title = str(city) + ', ' + str(country)
    buttons[title] = programID

# Search bar to filter buttons
search_query = st.text_input("Search programs: ")

# Sample list of button titles
button_titles = list(buttons.keys())

# Filter buttons based on search query (case-insensitive)
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]


# Display filtered buttons
for title in filtered_titles:
    if st.button(title):
        # If the button is clicked, set the program session_state variable to the programID of 
        # that program (found with the get method from the first word of the title)
        # then switch to the generic page that will display relevant info
        st.session_state['program'] = buttons[title]
        st.switch_page('pages/06_Display_Program_Location.py')

# # Making manual pages for each location     
# def paris_france_page():
#     st.switch_page('pages/051_paris.py')  

# def london_uk_page():
#     st.switch_page('pages/location_pages/052_london_uk.py')
    
# def nice_france_page():
#     st.switch_page('pages/location_pages/053_nice_france.py')
    
# def berlin_germany_page():
#     st.switch_page('pages/location_pages/054_berlin_germany.py')
    

# # Mapping each button to its respective page function
# location_functions = {
#     "Paris, France": paris_france_page,
#     "London, United Kingdom": london_uk_page,
#     "Nice, France": nice_france_page,
#     "Berlin, Germany": berlin_germany_page
# }

# # Sample list of button titles
# button_titles = list(location_functions.keys())

# # Search bar to filter buttons
# search_query = st.text_input("Search programs: ")

# # Filter buttons based on search query (case-insensitive)
# filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# # Display filtered buttons
# for title in filtered_titles:
#     if st.button(title):
#         # Call the function associated with the button title
#         location_functions[title]()
