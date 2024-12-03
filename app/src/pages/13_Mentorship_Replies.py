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
st.title("My Replies to Mentee Questions, from Mentee Tom")

repliesRoute = "http://api:4000/qr/tim/replies"
replies = requests.get(repliesRoute).json()

questionsRoute = "http://api:4000/qr/tom/questions"
questions = requests.get(questionsRoute).json()

flask_api_url_tom = "http://api:4000/qr/tom"
tom_name = requests.get(flask_api_url_tom)

# # Iterate through the questions and replies
# for idx, qa in enumerate(questions):
#     st.subheader(f"Question {idx + 1}")
#     st.markdown(f"**Question:** {qa['question']}")
#     st.markdown(
#         f"<div style='font-size: 1.2em; font-weight: bold; color: #333;'>Reply: {qa['reply']}</div>",
#         unsafe_allow_html=True
#     )
#     st.markdown("---")  # Separator for clarity

# for idx, qa in enumerate(replies):
#     st.subheader(f"Question {idx + 1}")
#     st.markdown(f"**Question:** {qa['question']}")
#     st.markdown(
#         f"<div style='font-size: 1.2em; font-weight: bold; color: #333;'>Reply: {qa['reply']}</div>",
#         unsafe_allow_html=True
#     )
#     st.markdown("---")  # Separator for clarity
