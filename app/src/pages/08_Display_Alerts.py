import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

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


title = "View Alerts for " + str(city) +  ", " + str(country) + ":"

st.title(title)
st.write('')

alertsroute = f'http://api:4000/ap/get_alerts/{programID}'
alerts_list = requests.get(alertsroute).json()

if alerts_list:
    for alert in alerts_list:
        st.write("- (", alert['datePosted'], ")", alert['message'])