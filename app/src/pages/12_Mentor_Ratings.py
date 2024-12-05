import logging
import requests # type: ignore
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

sID = st.session_state['userID']

studentroute = f'http://api:4000/s/get_student/{sID}'
student = requests.get(studentroute).json()

title = "Mentor " + str(student[0]['fName']) + " " + str(student[0]['lName']) + "\'s Ratings:"

st.title(title)

ratings_route = f'http://api:4000/s/get_ratings/{sID}'
ratings_list = requests.get(ratings_route).json()


if ratings_list:
    for rating in ratings_list:
        programID = rating['programID']
        cityroute = f'http://api:4000/ap/get_city/{programID}'
        city = requests.get(cityroute).json()
        city = city[0]['city']
        countryroute = f'http://api:4000/ap/get_country/{programID}'
        country = requests.get(countryroute).json()
        country = country[0]['country']

        st.write("Rating for program in ", str(city), ", ", str(country), ":")

        atmosphereRating = float(rating['atmosphereRating'])
        locationRating = float(rating['locRating'])
        professorRating = float(rating['profRating'])


        st.subheader("📍 Location Rating")
        location_text = f"**Location rating:** {round(locationRating, 2)}"
        st.markdown(location_text)

        location_stars = "⭐️" * int(locationRating)
        st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{location_stars}</span>", unsafe_allow_html=True)


        st.subheader("👨‍🏫 Professor Rating")
        professor_text = f"**Professor rating:** {round(professorRating, 2)}"
        st.markdown(professor_text)


        professor_stars = "⭐️" * int(professorRating)
        st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{professor_stars}</span>", unsafe_allow_html=True)

        st.subheader("🌤️ Atmosphere Rating")
        atmosphere_text = f"**Atmosphere rating:** {round(atmosphereRating, 2)}"
        st.markdown(atmosphere_text)

        atmosphere_stars = "⭐️" * int(atmosphereRating)
        st.markdown(f"<span style='font-size: 24px; color: #FFD700;'>{atmosphere_stars}</span>", unsafe_allow_html=True)
        st.markdown("---")

else:
    st.write('No ratings written yet!')


