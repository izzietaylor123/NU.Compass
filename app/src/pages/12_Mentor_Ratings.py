import logging
import requests # type: ignore
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Mentor Tim Ratings")

response = requests.get("http://api:4000/ap/abroad_programs").json()

try:
    st.dataframe(response)
except:
    st.write("Could not connect to database to retrive abroad programs")

            
    #         if response.status_code == 200:
    #             ratings = response.json()
    #             if not ratings:
    #                 st.write(f"Sorry! I don't have any ratings for: {location}.")
    #             else:
    #                 st.write(f"Mentor Ratings for {location}:")
    #                 for rating in ratings:
    #                     st.write(f"""
    #                     **Location Rating**: {rating['mentor']}  
    #                     **Atmosphere Rating**: {rating['rating']}  
    #                     **Professor Rating**: {rating['comment']}  
    #                     """)
    #         else:
    #             st.error(f"Failed to fetch ratings: {response.status_code}")
    #     except requests.ConnectionError:
    #         st.error("Unable to connect to the Flask API. Make sure it's running.")
    # else:
    #     st.error("Sorry! I don't have any ratings for this location.")