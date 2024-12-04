import logging
import requests # type: ignore
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Mentor Tim Ratings for Rome Dialoge of Civilations")

programID = 9

locRatRoute = f'http://api:4000/ap/location_rating/{programID}'
locationRating = requests.get(locRatRoute).json()
locationRating = locationRating[0]['AVG(locRating)']


profRatRoute = f'http://api:4000/ap/professor_rating/{programID}'
professorRating = requests.get(profRatRoute).json()
professorRating = professorRating[0]['AVG(profRating)']


atmRatRoute = f'http://api:4000/ap/atmosphereRating/{programID}'
atmosphereRating = requests.get(atmRatRoute).json()
atmosphereRating = atmosphereRating[0]['AVG(atmosphereRating)']

atmosphereRating = float(atmosphereRating)
locationRating = float(locationRating)
professorRating = float(professorRating)

st.header("Program Ratings")

st.markdown("---")

st.subheader("📍 Location Rating")
location_text = f"**Location rating:** {round(locationRating, 2)}"
st.markdown(location_text)

location_stars = "⭐️" * int(locationRating)
st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{location_stars}</span>", unsafe_allow_html=True)

st.markdown("---")

st.subheader("👨‍🏫 Professor Rating")
professor_text = f"**Professor rating:** {round(professorRating, 2)}"
st.markdown(professor_text)


professor_stars = "⭐️" * int(professorRating)
st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{professor_stars}</span>", unsafe_allow_html=True)

st.markdown("---")

st.subheader("🌤️ Atmosphere Rating")
atmosphere_text = f"**Atmosphere rating:** {round(atmosphereRating, 2)}"
st.markdown(atmosphere_text)

atmosphere_stars = "⭐️" * int(atmosphereRating)
st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{atmosphere_stars}</span>", unsafe_allow_html=True)

