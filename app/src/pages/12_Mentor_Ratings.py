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

st.write('')
st.write('')


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

        st.write(f"### Rating for program in {city}, {country}:")

        atmosphereRating = float(rating['atmosphereRating'])
        locationRating = float(rating['locRating'])
        professorRating = float(rating['profRating'])


        location_stars = "⭐️" * int(locationRating)

        location_text = f"##### 📍 Location rating: {round(locationRating, 2)} {location_stars}" 
        st.markdown(location_text)



        professor_stars = "⭐️" * int(professorRating)

        professor_text = f"##### 👨‍🏫 Professor rating: {round(professorRating, 2)} {professor_stars}"
        st.markdown(professor_text)


        atmosphere_stars = "⭐️" * int(atmosphereRating)
        atmosphere_text = f"##### 🌤️ Atmosphere rating: {round(atmosphereRating, 2)} {atmosphere_stars}"
        st.markdown(atmosphere_text)

        st.markdown("---")

else:
    st.write('No ratings written yet!')


