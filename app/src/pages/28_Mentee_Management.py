import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.session_state['mentee'] = -1
st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Admin Home Page')
st.title('View Current Mentee Students')
st.write('')

# Use request to obtain all mentor data 
mentee_data = requests.get('http://api:4000/s/mentees').json()

buttons = {}
for mentee in mentee_data: 
    sID = mentee['sID']
    last_name = mentee['lName']
    first_name = mentee['fName']
    title = str(last_name) + ", " + str(first_name)
    buttons[title] = sID

# Search bar to filter buttons
search_query = st.text_input("Search program mentees: ")

# Sample list of button titles
button_titles = list(buttons.keys())

# Filter buttons based on search query (case-insensitive)
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered buttons
for title in filtered_titles:
    if st.button(title):
        # If the button is clicked, set the mentor session_state variable to the sID of 
        # that student (found with the get method from the first word of the title)
        # then switch to the generic page that will display relevant info
        st.session_state['mentee'] = buttons[title]
        st.switch_page('pages/31_Display_Mentee_Info.py')

