import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

programID = st.session_state['program']


# Add a section to add a new location to the database

cityroute = f'http://api:4000/ap/get_city/{programID}'
city = requests.get(cityroute).json()
city = city[0]['city']
countryroute = f'http://api:4000/ap/get_country/{programID}'
country = requests.get(countryroute).json()
country = country[0]['country']

st.write(f"## Enter ratings for *{city}, {country}* below:")



with st.form("add_rating_form"):

    # Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    location_rating = st.slider("Location Rating", 1, 5)
    professor_rating = st.slider("Professor Rating", 1, 5)
    atmosphere_rating = st.slider("Atmosphere Rating", 1, 5)
    comment = st.text_input("Comments:")
    abroadProgram = programID
    sID = st.session_state['userID']

    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Post Rating")

    if submit_button:
        
        # Package the data up that the user entered into 
        # a dictionary (which is just like JSON in this case)
        rating_data = {
            "location_rating": location_rating,
            "professor_rating": professor_rating,
            "atmosphere_rating": atmosphere_rating,
            "comment": comment,
            "sID": sID,
            "abroadProgram": abroadProgram
        }
        
        # printing out the data - will show up in the Docker Desktop logs tab
        # for the web-app container 
        logger.info(f"Rating form submitted with data: {rating_data}")
        
        # Now, we try to make a POST request to the proper end point
        try:
            # using the requests library to POST to /p/product.  Passing
            # product_data to the endpoint through the json parameter.
            # This particular end point is located in the products_routes.py
            # file found in api/backend/products folder. 
            response = requests.post('http://api:4000/ap/add_rating', json=rating_data)
            if response.status_code == 200:
                st.success("Rating added successfully!")
            else:
                st.error(f"Error adding product: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
