import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

if 'mentee' not in st.session_state:
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
    mentee_id = mentee['sID']
    last_name = mentee['lName']
    first_name = mentee['fName']
    title = str(last_name) + ", " + str(first_name)
    email = mentee['email']
    blurb = mentee['blurb']
    buttons[title] = {
        "mentee_id": mentee_id,
        "email": email,
        "blurb": blurb
    }

# Search bar to filter buttons
search_query = st.text_input("Search program mentees: ")

# Sample list of button titles
button_titles = list(buttons.keys())

# Filter buttons based on search query (case-insensitive)
filtered_titles = [title for title in button_titles if search_query.lower() in title.lower()]

# Display filtered buttons
st.subheader("View Mentees")
if filtered_titles:
    for title in filtered_titles:
        if st.button(title):
            # set the mentee session state and navigate to the details page
            st.session_state['mentee'] = buttons[title]["mentee_id"]
            st.switch_page('pages/31_Display_Mentee_Info.py')
else:
    st.info("No mentees match your search.")

st.subheader("Add New Mentee")
with st.form("add_mentee_form"):
    f_name = st.text_input("First Name")
    l_name = st.text_input("Last Name")
    email = st.text_input("Email")
    blurb = st.text_area("Blurb (optional)")
    submit = st.form_submit_button("Add Mentee")

    if submit:
        if f_name and l_name and email:
            payload = {
                "Name": f"{f_name} {l_name}",
                "Email": email,
                "Blurb": blurb
            }
            try:
                response = requests.post('http://api:4000/s/mentees', json=payload)
                if response.status_code == 201:
                    st.success("Mentee added successfully!")
                    #st.experimental_rerun()
                else:
                    st.error("Failed to add mentee. Please try again.")
            except Exception as e:
                st.error("Error adding mentee. Please check the logs.")
                logger.error(f"Error adding mentee: {e}")
        else:
            st.error("All fields are required to add a mentee.")

# Edit or Delete Mentees
st.subheader("Edit or Delete Mentees")
for title in filtered_titles:
    mentee_details = buttons[title]
    mentee_id = mentee_details["mentee_id"]
    with st.expander(f"Manage Mentee: {title}"):
        col1, col2 = st.columns(2)

        # Edit mentor details
        with col1:
            new_f_name = st.text_input(f"Edit First Name (ID: {mentee_id})", value=title.split()[0])
            new_l_name = st.text_input(f"Edit Last Name (ID: {mentee_id})", value=title.split()[1])
            new_email = st.text_input(f"Edit Email (ID: {mentee_id})", value=mentee_details["email"])
            new_blurb = st.text_area(f"Edit Blurb (ID: {mentee_id})", value=mentee_details["blurb"])
            if st.button(f"Save Changes (ID: {mentee_id})"):
                payload = {
                    "Name": f"{new_f_name} {new_l_name}",
                    "Email": new_email,
                    "Blurb": new_blurb
                }
                try:
                    response = requests.put(f'http://api:4000/s/mentors/{mentee_id}', json=payload)
                    if response.status_code == 200:
                        st.success("Mentee updated successfully!")
                        # st.experimental_rerun()
                    else:
                        st.error("Failed to update mentee. Please try again.")
                except Exception as e:
                    st.error("Error updating mentee. Please check the logs.")
                    logger.error(f"Error updating mentee: {e}")

        # Delete mentor
        with col2:
            if st.button(f"Delete Mentee (ID: {mentee_id})"):
                try:
                    response = requests.delete(f'http://api:4000/s/mentees/{mentee_id}')
                    if response.status_code == 200:
                        st.success("Mentee deleted successfully!")
                        # st.experimental_rerun()
                    else:
                        st.error("Failed to delete mentee. Please try again.")
                except Exception as e:
                    st.error("Error deleting mentee. Please check the logs.")
                    logger.error(f"Error deleting mentee: {e}")


