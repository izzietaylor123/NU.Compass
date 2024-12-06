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
    mentor_data = requests.get('http://api:4000/s/mentors').json()
    if not mentor_data:
        st.warning("No mentors found.")
except Exception as e:
    st.error("Failed to load mentors data from server.")
    logger.error(f"Error fetching mentors: {e}")
    mentor_data = []

# Build a dictionary for mentor buttons
buttons = {}
for mentor in mentor_data:
    mentor_id = mentor['sID']
    name = f"{mentor['fName']} {mentor['lName']}"
    email = mentor['email']
    blurb = mentor['blurb']
    buttons[name] = {
        "mentor_id": mentor_id,
        "email": email,
        "blurb": blurb
    }

# Search bar for mentors
st.subheader("Search Mentors")
search_query = st.text_input("Type to search mentors:")

# Filter mentor list based on search query (case-insensitive)
button_titles = list(buttons.keys())
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered mentor buttons
st.subheader("View/Edit Mentors")
if filtered_titles:
    for title in filtered_titles:
        if st.button(title, key=f"view_{buttons[title]['mentor_id']}"):
            st.session_state['mentor'] = buttons[title]["mentor_id"]
            st.switch_page('pages/27_Display_Mentor_Info.py')
else:
    st.info("No mentors match your search.")

# Add a new mentor
st.subheader("Add New Mentor")
with st.form("add_mentor_form"):
    f_name = st.text_input("First Name")
    l_name = st.text_input("Last Name")
    email = st.text_input("Email")
    blurb = st.text_area("Blurb (optional)")
    submit = st.form_submit_button("Add Mentor")

    if submit:
        if f_name and l_name and email:
            payload = {
        "Name": f"{f_name} {l_name}",  # Combine first and last name
        "Email": email,
        "Blurb": blurb}
            try:
                response = requests.post('http://api:4000/s/mentors', json=payload)
                if response.status_code == 201:
                    st.success("Mentor added successfully!")
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
    mentor_details = buttons[title]
    mentor_id = mentor_details["mentor_id"]
    with st.expander(f"Manage Mentor: {title}"):
        col1, col2 = st.columns(2)

        # Edit mentor details
        with col1:
            new_f_name = st.text_input(f"Edit First Name (ID: {mentor_id})", value=title.split()[0], key=f"edit_fname_{mentor_id}")
            new_l_name = st.text_input(f"Edit Last Name (ID: {mentor_id})", value=title.split()[1], key=f"edit_lname_{mentor_id}")
            new_email = st.text_input(f"Edit Email (ID: {mentor_id})", value=mentor_details["email"], key=f"edit_email_{mentor_id}")
            new_blurb = st.text_area(f"Edit Blurb (ID: {mentor_id})", value=mentor_details["blurb"], key=f"edit_blurb_{mentor_id}")
            if st.button(f"Save Changes (ID: {mentor_id})", key=f"save_changes_{mentor_id}"):
                payload = {
                    "fName": new_f_name,
                    "lName": new_l_name,
                    "Email": new_email,
                    "Blurb": new_blurb
                }
                try:
                    response = requests.put(f'http://api:4000/s/mentors/{mentor_id}', json=payload)
                    if response.status_code == 200:
                        st.success("Mentor updated successfully!")
                    else:
                        st.error("Failed to update mentor. Please try again.")
                except Exception as e:
                    st.error("Error updating mentor. Please check the logs.")
                    logger.error(f"Error updating mentor: {e}")

        # Delete mentor
        with col2:
            if st.button(f"Delete Mentor (ID: {mentor_id})", key=f"delete_{mentor_id}"):
                try:
                    response = requests.delete(f'http://api:4000/s/mentors/{mentor_id}')
                    if response.status_code == 200:
                        st.success("Mentor deleted successfully!")
                    else:
                        st.error("Failed to delete mentor. Please try again.")
                except Exception as e:
                    st.error("Error deleting mentor. Please check the logs.")
                    logger.error(f"Error deleting mentor: {e}")
