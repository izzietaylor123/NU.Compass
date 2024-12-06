import logging
import json
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

user_role = st.session_state.get("role", "guest")

from st_keyup import st_keyup

st.session_state['program'] = -1

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Find a location!')

# get all locations

location_list = requests.get('http://api:4000/ap/get_all_program_ids').json()

# Add button to switch to page in order to add new location if the role is an admin
if st.session_state['role'] == 'administrator':
    with st.container(): 
        if st.button('Add New Location/Program', 
                    type='primary',
                    use_container_width=True):
            st.switch_page('pages/07_Add_Program_Location.py')

# get all locations
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

# Delete a location, given a locationID
def delete_location(locationID):
    delete_route = f'http://api:4000/l/location/{locationID}'
    response = requests.delete(delete_route)
    if response.status_code == 200:
        st.write(f"Location with ID {locationID} has been deleted.")

if user_role == 'administrator':
    st.subheader("Delete a Location")
    locationID = st.text_input("Enter Location ID to delete:")

    # Delete location once button is pressed
    if st.button("Delete Location"):
        if locationID:
            delete_location(locationID)
        else:
            st.write("Please provide a valid Location ID")