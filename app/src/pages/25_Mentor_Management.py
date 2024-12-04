import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Initialize session state for mentor if not already set
if 'mentor' not in st.session_state:
    st.session_state['mentor'] = -1

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Mentor Management')

# Fetch mentor data from the backend
try:
    mentor_data = requests.get('http://localhost:4000/mentors').json()  # Adjust URL to match your API
except Exception as e:
    st.error("Failed to load mentors data from server.")
    logger.error(f"Error fetching mentors: {e}")
    mentor_data = []

# Build a dictionary for mentor buttons
buttons = {}
for mentor in mentor_data:
    mentor_id = mentor['MentorID']
    name = mentor['Name']
    title = f"{name} (ID: {mentor_id})"
    buttons[title] = mentor_id

# Search bar for mentors
search_query = st.text_input("Search mentors: ")

# Filter mentor list based on search query (case-insensitive)
button_titles = list(buttons.keys())
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered mentor buttons
st.subheader("View/Edit Mentors")
for title in filtered_titles:
    if st.button(title):
        # Set the mentor session state and navigate to the details page
        st.session_state['mentor'] = buttons[title]
        st.switch_page('pages/27_Display_Mentor_Info.py')

# Add a new mentor
st.subheader("Add New Mentor")
with st.form("add_mentor_form"):
    name = st.text_input("Mentor Name")
    email = st.text_input("Mentor Email")
    expertise = st.text_input("Expertise (e.g., Programming, Business)")
    availability = st.text_input("Availability (e.g., Full-Time, Part-Time)")
    submit = st.form_submit_button("Add Mentor")

    if submit:
        if name and email and expertise and availability:
            payload = {
                "Name": name,
                "Email": email,
                "Expertise": expertise,
                "Availability": availability
            }
            try:
                response = requests.post('http://localhost:4000/mentors', json=payload)
                if response.status_code == 201:
                    st.success("Mentor added successfully!")
                    st.experimental_rerun()  # Refresh the page to show the new mentor
                else:
                    st.error("Failed to add mentor. Please try again.")
            except Exception as e:
                st.error("Error adding mentor. Please check the logs.")
                logger.error(f"Error adding mentor: {e}")
        else:
            st.error("All fields are required to add a mentor.")

# Edit or Delete Mentors
st.subheader("Edit or Delete Mentors")
for title in filtered_titles:
    mentor_id = buttons[title]
    with st.expander(f"Manage Mentor: {title}"):
        col1, col2 = st.columns(2)

        # Edit mentor details
        with col1:
            new_name = st.text_input(f"Edit Name (ID: {mentor_id})", value=mentor['Name'])
            new_email = st.text_input(f"Edit Email (ID: {mentor_id})", value=mentor['Email'])
            new_expertise = st.text_input(f"Edit Expertise (ID: {mentor_id})", value=mentor['Expertise'])
            new_availability = st.text_input(f"Edit Availability (ID: {mentor_id})", value=mentor['Availability'])

            if st.button(f"Save Changes (ID: {mentor_id})"):
                payload = {
                    "Name": new_name,
                    "Email": new_email,
                    "Expertise": new_expertise,
                    "Availability": new_availability
                }
                try:
                    response = requests.put(f'http://localhost:4000/mentors/{mentor_id}', json=payload)
                    if response.status_code == 200:
                        st.success("Mentor updated successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to update mentor. Please try again.")
                except Exception as e:
                    st.error("Error updating mentor. Please check the logs.")
                    logger.error(f"Error updating mentor: {e}")

        # Delete mentor
        with col2:
            if st.button(f"Delete Mentor (ID: {mentor_id})"):
                try:
                    response = requests.delete(f'http://localhost:4000/mentors/{mentor_id}')
                    if response.status_code == 200:
                        st.success("Mentor deleted successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to delete mentor. Please try again.")
                except Exception as e:
                    st.error("Error deleting mentor. Please check the logs.")
                    logger.error(f"Error deleting mentor: {e}")


import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Initialize session state for mentor if not already set
if 'mentor' not in st.session_state:
    st.session_state['mentor'] = -1

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Mentor Management')

# Fetch mentor data from the backend
try:
    mentor_data = requests.get('http://localhost:4000/mentors').json()  # Adjust URL to match your API
except Exception as e:
    st.error("Failed to load mentors data from server.")
    logger.error(f"Error fetching mentors: {e}")
    mentor_data = []

# Build a dictionary for mentor buttons
buttons = {}
for mentor in mentor_data:
    mentor_id = mentor['MentorID']
    name = mentor['Name']
    title = f"{name} (ID: {mentor_id})"
    buttons[title] = mentor_id

# Search bar for mentors
search_query = st.text_input("Search mentors: ")

# Filter mentor list based on search query (case-insensitive)
button_titles = list(buttons.keys())
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered mentor buttons
st.subheader("View/Edit Mentors")
for title in filtered_titles:
    if st.button(title):
        # Set the mentor session state and navigate to the details page
        st.session_state['mentor'] = buttons[title]
        st.switch_page('pages/27_Display_Mentor_Info.py')

# Add a new mentor
st.subheader("Add New Mentor")
with st.form("add_mentor_form"):
    name = st.text_input("Mentor Name")
    email = st.text_input("Mentor Email")
    expertise = st.text_input("Expertise (e.g., Programming, Business)")
    availability = st.text_input("Availability (e.g., Full-Time, Part-Time)")
    submit = st.form_submit_button("Add Mentor")

    if submit:
        if name and email and expertise and availability:
            payload = {
                "Name": name,
                "Email": email,
                "Expertise": expertise,
                "Availability": availability
            }
            try:
                response = requests.post('http://localhost:4000/mentors', json=payload)
                if response.status_code == 201:
                    st.success("Mentor added successfully!")
                    st.experimental_rerun()  # Refresh the page to show the new mentor
                else:
                    st.error("Failed to add mentor. Please try again.")
            except Exception as e:
                st.error("Error adding mentor. Please check the logs.")
                logger.error(f"Error adding mentor: {e}")
        else:
            st.error("All fields are required to add a mentor.")

# Edit or Delete Mentors
st.subheader("Edit or Delete Mentors")
for title in filtered_titles:
    mentor_id = buttons[title]
    with st.expander(f"Manage Mentor: {title}"):
        col1, col2 = st.columns(2)

        # Edit mentor details
        with col1:
            new_name = st.text_input(f"Edit Name (ID: {mentor_id})", value=mentor['Name'])
            new_email = st.text_input(f"Edit Email (ID: {mentor_id})", value=mentor['Email'])
            new_expertise = st.text_input(f"Edit Expertise (ID: {mentor_id})", value=mentor['Expertise'])
            new_availability = st.text_input(f"Edit Availability (ID: {mentor_id})", value=mentor['Availability'])

            if st.button(f"Save Changes (ID: {mentor_id})"):
                payload = {
                    "Name": new_name,
                    "Email": new_email,
                    "Expertise": new_expertise,
                    "Availability": new_availability
                }
                try:
                    response = requests.put(f'http://localhost:4000/mentors/{mentor_id}', json=payload)
                    if response.status_code == 200:
                        st.success("Mentor updated successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to update mentor. Please try again.")
                except Exception as e:
                    st.error("Error updating mentor. Please check the logs.")
                    logger.error(f"Error updating mentor: {e}")

        # Delete mentor
        with col2:
            if st.button(f"Delete Mentor (ID: {mentor_id})"):
                try:
                    response = requests.delete(f'http://localhost:4000/mentors/{mentor_id}')
                    if response.status_code == 200:
                        st.success("Mentor deleted successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to delete mentor. Please try again.")
                except Exception as e:
                    st.error("Error deleting mentor. Please check the logs.")
                    logger.error(f"Error deleting mentor: {e}")


