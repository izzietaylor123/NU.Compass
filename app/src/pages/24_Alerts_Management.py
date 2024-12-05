import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Alert Management')

# Fetch alert data from the backend
try:
    alerts_data = requests.get('http://api:4000/am/alerts').json()
    if not alerts_data:
        st.warning("No alerts found.")
except Exception as e:
    st.error("Failed to load alerts data from server.")
    logger.error(f"Error fetching alerts: {e}")
    alerts_data = []

# Build a dictionary for alert buttons
buttons = {}
for alert in alerts_data:
    alert_id = alert['alertID']
    location_id = alert['locationID']
    message = alert['message']
    date_posted = alert['datePosted']
    buttons[f"Alert {alert_id} (Location {location_id})"] = {
        "alert_id": alert_id,
        "location_id": location_id,
        "message": message,
        "date_posted": date_posted
    }

# Search bar for alerts
st.subheader("Search Alerts")
search_query = st.text_input("Type to search alerts by message:")

# Filter alerts based on search query (case-insensitive)
button_titles = list(buttons.keys())
filtered_titles = [title for title in button_titles if search_query.lower() in buttons[title]["message"].lower()]

# Display filtered alerts
st.subheader("View/Edit Alerts")
if filtered_titles:
    for title in filtered_titles:
        alert_details = buttons[title]
        alert_id = alert_details["alert_id"]
        with st.expander(f"Manage Alert: {title}"):
            col1, col2 = st.columns(2)

            # Edit alert details
            with col1:
                new_message = st.text_area(f"Edit Message (ID: {alert_id})", value=alert_details["message"])
                if st.button(f"Save Changes (ID: {alert_id})"):
                    payload = {
                        "message": new_message
                    }
                    try:
                        response = requests.put(f'http://api:4000/am/alerts/{alert_id}', json=payload)
                        if response.status_code == 200:
                            st.success("Alert updated successfully!")
                            #st.experimental_rerun()
                        else:
                            st.error("Failed to update alert. Please try again.")
                    except Exception as e:
                        st.error("Error updating alert. Please check the logs.")
                        logger.error(f"Error updating alert: {e}")

            # Delete alert
            with col2:
                if st.button(f"Delete Alert (ID: {alert_id})"):
                    try:
                        response = requests.delete(f'http://api:4000/am/alerts/{alert_id}')
                        if response.status_code == 200:
                            st.success("Alert deleted successfully!")
                            #st.experimental_rerun()
                        else:
                            st.error("Failed to delete alert. Please try again.")
                    except Exception as e:
                        st.error("Error deleting alert. Please check the logs.")
                        logger.error(f"Error deleting alert: {e}")
else:
    st.info("No alerts match your search.")

# Add a new alert
st.subheader("Add New Alert")
with st.form("add_alert_form"):
    location_id = st.number_input("Location ID", min_value=1, step=1)
    new_message = st.text_area("Alert Message")
    submit = st.form_submit_button("Add Alert")

    if submit:
        if location_id and new_message:
            payload = {
                "locationID": location_id,
                "message": new_message
            }
            try:
                response = requests.post('http://api:4000/am/alerts', json=payload)
                if response.status_code == 201:
                    st.success("Alert added successfully!")
                    #st.experimental_rerun()  # Refresh the page to show the new alert
                else:
                    st.error("Failed to add alert. Please try again.")
            except Exception as e:
                st.error("Error adding alert. Please check the logs.")
                logger.error(f"Error adding alert: {e}")
        else:
            st.error("Location ID and Message are required to add an alert.")
