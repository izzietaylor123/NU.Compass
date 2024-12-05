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
    
# Show replies with delete functionality
st.subheader("My Replies")
for reply in replies:
    st.write(f"**Reply ID:** {reply['replyID']}")
    st.write(f"**Content:** {reply['content']}")

    if st.button(f"Delete Reply {reply['replyID']}"):
        delete_url = f"http://api:4000/qr/delete_reply/{reply['replyID']}/{userID}"
        response = requests.delete(delete_url)

        if response.status_code == 200:
            st.success("Reply deleted successfully!")
            st.experimental_rerun()  # Refresh the page to reflect the changes
        else:
            st.error("Failed to delete reply. Please try again.")

with st.expander("Add a New Question"):
    with st.form(key="question_form"):
        question_title = st.text_input("Question Title")
        question_body = st.text_area("Question Body")
        
        submit_question = st.form_submit_button("Submit Question")
        
        if submit_question:
            new_question = {
                "student_id": userID,
                "body": question_body
            }
            
            response = requests.post(f"http://api:4000/qr/add_question", json=new_question)
            
            if response.status_code == 200:
                st.success("Your question was submitted successfully!")

            else:
                st.error("There was an error submitting your question.")

with st.expander("Add a New Reply"):
    with st.form(key="reply_form"):
        reply_body = st.text_area("Reply Body")
        question_id = st.selectbox("Select Question to Reply To", [q['title'] for q in questions])
        
        submit_reply = st.form_submit_button("Submit Reply")
        
        if submit_reply:
            question_id_selected = next(q['id'] for q in questions if q['title'] == question_id) 
            new_reply = {
                "student_id": userID,
                "body": reply_body
            }

            response = requests.post(f"http://api:4000/qr/add_reply", json=new_reply)
            
            if response.status_code == 200:
                st.success("Your reply was submitted successfully!")
            else:
                st.error("There was an error submitting your reply.")

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


        