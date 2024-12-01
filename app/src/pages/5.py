import logging
logger = logging.getLogger(__name__)
import lisaa_sql as lisaa
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome to Paris, France!")

st.write("The Northeastern Paris N.U.in Program offers first-year students\
         the chance to study abroad in one of the world’s most iconic cities. \
         In Paris, students immerse themselves in the city’s rich history, culture, and art \
         while taking courses that blend global perspectives with their academic focus. \
         Beyond the classroom, students explore landmarks like the Eiffel Tower, the Louvre, and Montmartre, \
         gaining firsthand experience of Parisian life. The program also integrates opportunities for professional development, \
         including the potential for co-op placements in international companies or organizations based in Paris. \
         Through this experience, students develop not only academic knowledge but also a deep appreciation for French culture\
        and the global context in which they are studying.")

# locationRating = lisaa.get_location_rating(lisaa.get_program_id('Paris'))
# professorRating = lisaa.get_professor_rating(lisaa.get_program_id('Paris'))
# atmosphereRating = lisaa.get_atmosphere_rating(lisaa.get_program_id('Paris'))

locationRating = 4.6
professorRating = 2.5
atmosphereRating = 3.0

averageRating = (locationRating + professorRating + atmosphereRating) / 3

st.write('')
st.write('Location rating: ')
st.write(locationRating)
for i in range (int(locationRating)):
    st.write('⭐️')

st.write('')
st.write('Professor rating: ')
st.write(professorRating)
for i in range (int(professorRating)):
    st.write('⭐️')

st.write('')
st.write('Atmosphere rating: ')
st.write(atmosphereRating)
for i in range (int(atmosphereRating)):
    st.write('⭐️')
