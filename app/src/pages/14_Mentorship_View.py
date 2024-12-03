import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import json

SideBarLinks()
# Page title
st.title("Tim's mentor view where he can see all other mentors")

mentorRoute = f'http://api:4000/s/mentors'
mentors = requests.get(mentorRoute).json()

st.write('')
st.dataframe(mentors)
