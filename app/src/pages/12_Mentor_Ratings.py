import logging
import requests # type: ignore
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Mentor Tim Ratings")

locRatRoute = f'http://api:4000/ap/location_rating/{programID}'
locationRating = requests.get(locRatRoute).json()
locationRating = locationRating[0]['AVG(locRating)']

profRatRoute = f'http://api:4000/ap/professor_rating/{programID}'
professorRating = requests.get(profRatRoute).json()
professorRating = professorRating[0]['AVG(profRating)']

atmRatRoute = f'http://api:4000/ap/atmosphereRating/{programID}'
atmosphereRating = requests.get(atmRatRoute).json()
atmosphereRating = atmosphereRating[0]['AVG(atmosphereRating)']


try:
    st.dataframe(response)
except:
    st.write("Could not connect to database to retrive abroad programs")