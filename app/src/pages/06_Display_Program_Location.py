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


cityroute = f'http://api:4000/ap/get_city/{programID}'
city = requests.get(cityroute).json()
city = city[0]['city']
countryroute = f'http://api:4000/ap/get_country/{programID}'
country = requests.get(countryroute).json()
country = country[0]['country']



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

    locRatRoute = f'http://api:4000/ap/location_rating/{programID}'
    locationRating = requests.get(locRatRoute).json()
    locationRating = locationRating[0]['AVG(locRating)']

    profRatRoute = f'http://api:4000/ap/professor_rating/{programID}'
    professorRating = requests.get(profRatRoute).json()
    professorRating = professorRating[0]['AVG(profRating)']

    atmRatRoute = f'http://api:4000/ap/atmosphereRating/{programID}'
    atmosphereRating = requests.get(atmRatRoute).json()
    atmosphereRating = atmosphereRating[0]['AVG(atmosphereRating)']



    averageRating = round(((float(locationRating) + float(professorRating) + float(atmosphereRating)) / 3), 2)

    atmosphereRating = float(atmosphereRating)
    locationRating = float(locationRating)
    professorRating = float(professorRating)

    st.write('')
    avgR = 'Average rating: ' + str(averageRating) + ' '
    for i in range (int(averageRating)):
        avgR = avgR + '⭐️'
    st.write('###', avgR)

    st.write('')
    lr = 'Location rating: ' + str(round((locationRating), 2)) + ' '
    for i in range (int(locationRating)):
        lr = lr + '⭐️'
    st.write(lr)

    st.write('')

    pr = 'Professor rating: ' + str(round((professorRating), 2)) + ' '
    for i in range (int(professorRating)):
        pr = pr + '⭐️'
    st.write(pr)

    st.write('')
    ar = 'Atmosphere rating: ' + str(round((atmosphereRating), 2)) + ' '
    for i in range (int(atmosphereRating)):
        ar = ar + '⭐️'
    st.write(ar)

# Accesses and writes the program description based on the programID of the session_state
descriptionRoute = f'http://api:4000/ap/program_description/{programID}'
description = requests.get(descriptionRoute).json()
description = description[0]['prgmDescription']
st.write(description)

