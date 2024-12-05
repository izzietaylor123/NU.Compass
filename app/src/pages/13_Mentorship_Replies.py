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

st.title("My Questions and/or Replies")
if 'userID' not in st.session_state:
    st.error("User not logged in. Please log in to continue.")
    st.stop()

userID = st.session_state['userID']

questions_route = f"http://api:4000/qr/get_questions/{userID}"
questions = requests.get(questions_route).json()

replies_route = f"http://api:4000/qr/get_replies/{userID}"
replies = requests.get(replies_route).json()


if len(questions) == 0:
    st.warning("No questions available for this user.")

if len(replies) == 0:
    st.warning("No replies available for this user.")

st.subheader(f"Questions/Replies")
for i, question in enumerate(questions, start=1):
    st.write(f"### Question {i}")
    for key, value in question.items():
        st.write(f"**{key.capitalize()}:** {value}")
        st.subheader(f"Questions/Replies")

for i, replies in enumerate(replies, start=1):
    st.write(f"### Reply {i}")
    for key, value in replies.items():
        st.write(f"**{key.capitalize()}:** {value}")
