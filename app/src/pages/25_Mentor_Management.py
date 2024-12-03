import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.session_state['mentor'] = -1
st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('View Current Abroad Mentors')
st.write('')

# Use request to obtain all mentor data 
mentor_data = requests.get('http://api:4000/s/mentors').json()

buttons = {}
for mentor in mentor_data: 
    sID = mentor['sID']
    last_name = mentor['lName']
    first_name = mentor['fName']
    title = str(last_name) + "," + str(first_name)
    buttons[title] = sID

# Search bar to filter buttons
search_query = st.text_input("Search program mentors: ")

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
        st.session_state['mentor'] = buttons[title]
        st.switch_page('pages/27_Display_Mentor_Info.py')
