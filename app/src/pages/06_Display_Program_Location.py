import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

# from backend.customers.location_routes.py import get_locations 

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

programID = st.session_state.program

city = requests.get('http://api:4000/ap/get_city/<programID>').json()
country = requests.get('http://api:4000/ap/get_country/<programID>').json()

title = "Welcome to " + str(city) +  ", " + str(country) + "!"

st.title(title)
st.write('')

left_co, cent_co = st.columns((1, 2))
with left_co:
    st.image("assets/eiffel_tower.png")

with cent_co:

    st.write(' ')
    st.write(' ')
    st.write(' ')

    locationRating = lisaa.get_location_rating(programID)
    professorRating = lisaa.get_professor_rating(programID)
    atmosphereRating = lisaa.get_atmosphere_rating(programID)

    averageRating = round(((locationRating + professorRating + atmosphereRating) / 3), 2)

    st.write('')
    avgR = 'Average rating: ' + str(averageRating) + ' '
    for i in range (int(averageRating)):
        avgR = avgR + '⭐️'
    st.write('###', avgR)

    st.write('')
    lr = 'Location rating: ' + str(round(locationRating, 2)) + ' '
    for i in range (int(locationRating)):
        lr = lr + '⭐️'
    st.write(lr)

    st.write('')

    pr = 'Professor rating: ' + str(round(professorRating, 2)) + ' '
    for i in range (int(professorRating)):
        pr = pr + '⭐️'
    st.write(pr)

    st.write('')
    ar = 'Atmosphere rating: ' + str(round(atmosphereRating, 2)) + ' '
    for i in range (int(atmosphereRating)):
        ar = ar + '⭐️'
    st.write(ar)

# Accesses and writes the program description based on the programID of the session_state
st.write(lisaa.get_program_description(programID))

