
import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

user_role = st.session_state.get("role", "guest")
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



title = f"View comments for *{str(city)}, {str(country)}*:"
st.title(title)

st.write('')


commentsroute = f'http://api:4000/ap//get_comments/{programID}'
comments = requests.get(commentsroute).json()

if comments:
    for comment in comments:
        comment_content = str(comment['comment'])
        sID = str(comment['sID'])
        studentroute = f'http://api:4000/s/get_student/{sID}'
        student = requests.get(studentroute).json()
        first_name = str(student[0]['fName'])
        st.write(f"- \"**{comment_content}\"** -{first_name}")

