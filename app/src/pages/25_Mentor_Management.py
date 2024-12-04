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
    mentor_data = requests.get('http://api:4000/s/mentors').json()  # Adjust URL to match your API
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
    name = mentor['fName']
    email = mentor['email']
    # Expertise and Availability are placeholders unless implemented in the backend
    expertise = mentor.get('Expertise', 'N/A')
    availability = mentor.get('Availability', 'N/A')
    buttons[name] = {
        "mentor_id": mentor_id,
        "email": email,
        "expertise": expertise,
        "availability": availability
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
        if st.button(title):
            # Set the mentor session state and navigate to the details page
            mentor_id = buttons[title]["mentor_id"]
            st.session_state['mentor'] = mentor_id
            st.switch_page('pages/27_Display_Mentor_Info.py')
else:
    st.info("No mentors match your search.")

# Add a new mentor
st.subheader("Add New Mentor")
with st.form("add_mentor_form"):
    name = st.text_input("Mentor Name")
    email = st.text_input("Mentor Email")
    blurb = st.text_area("Blurb (optional)")
    submit = st.form_submit_button("Add Mentor")

    if submit:
        if name and email:
            payload = {
                "Name": name,
                "Email": email,
                "Blurb": blurb
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
            st.error("Name and Email are required to add a mentor.")

# Edit or Delete Mentors
st.subheader("Edit or Delete Mentors")
for title in filtered_titles:
    mentor_details = buttons[title]
    mentor_id = mentor_details["mentor_id"]
    with st.expander(f"Manage Mentor: {title}"):
        col1, col2 = st.columns(2)

        # Edit mentor details
        with col1:
            new_name = st.text_input(f"Edit Name (ID: {mentor_id})", value=title)
            new_email = st.text_input(f"Edit Email (ID: {mentor_id})", value=mentor_details["email"])
            new_blurb = st.text_area(f"Edit Blurb (ID: {mentor_id})", value="Update mentor details here.")
            if st.button(f"Save Changes (ID: {mentor_id})"):
                payload = {
                    "Name": new_name,
                    "Email": new_email,
                    "Blurb": new_blurb
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
