import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import json

SideBarLinks()

# Page title
st.title("My Replies to Mentee Questions, from Mentee Tom")
# Check if userID exists in session state
if 'userID' not in st.session_state:
    st.error("User not logged in. Please log in to continue.")
    st.stop()

# Get userID from session state
userID = st.session_state['userID']

# Define API endpoints
questions_route = f"http://api:4000/qr/get_questions/{userID}"
questions = requests.get(questions_route).json()

replies_route = f"http://api:4000/qr/get_replies/{userID}"
replies = requests.get(replies_route).json()

# Fetch data from APIs
def fetch_data(route):
    try:
        response = requests.get(route)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Parse JSON response
        if not isinstance(data, list):
            raise ValueError("Invalid data format received from API.")
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch data from {route}. Please try again later.")
        st.stop()
    except ValueError as e:
        st.error(f"Unexpected data format from API: {e}")
        st.stop()

# Filter and display questions
if len(questions) == 0:
    st.warning("No questions available for this user.")

if len(replies) == 0:
    st.warning("No replies available for this user.")
    st.stop()

# Display questions
st.subheader(f"Questions for User ID: {userID}")
for i, question in enumerate(questions, start=1):
    st.write(f"### Question {i}")
    for key, value in question.items():
        st.write(f"**{key.capitalize()}:** {value}")

# Expandable section for all data
with st.expander("View All Questions and Replies"):
    st.subheader("All Questions")
    st.dataframe(pd.DataFrame(questions))

    st.subheader("All Replies")
    st.dataframe(pd.DataFrame(replies))