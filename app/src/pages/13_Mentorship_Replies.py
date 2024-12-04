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

if not isinstance(questions, list) or not isinstance(replies, list):
    st.error("Unexpected API response. Please check the data structure.")
    st.stop()

if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

def next_question():
    if st.session_state.current_question_index < len(questions) - 1:
        st.session_state.current_question_index += 1

def previous_question():
    if st.session_state.current_question_index > 0:
        st.session_state.current_question_index -= 1

current_index = st.session_state.current_question_index
current_question = questions[current_index]
current_reply = (
    replies[current_index]
    if current_index < len(replies)
    else {"reply_text": "No reply available"}
)

st.title("Question and Reply Viewer")

st.subheader(f"Question {current_index + 1} of {len(questions)}")
st.write("### Question Details:")
for key, value in current_question.items():
    st.write(f"**{key.capitalize()}:** {value}")

st.write("### Reply Details:")
for key, value in current_reply.items():
    st.write(f"**{key.capitalize()}:** {value}")

col1, col2 = st.columns([1, 1])
with col1:
    st.button("Previous", on_click=previous_question, disabled=current_index == 0)
with col2:
    st.button("Next", on_click=next_question, disabled=current_index == len(questions) - 1)

with st.expander("View All Questions and Replies"):
    st.subheader("Questions")
    st.dataframe(questions)
    st.subheader("Replies")
    st.dataframe(replies)
