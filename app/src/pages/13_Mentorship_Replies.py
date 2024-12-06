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

# Add a new question
def submit_question():
    st.write("question_form:")

    abroad_program = st.text_input('Abroad Program ID', '', key="abroad_program_input")  # New field
    question_content = st.text_area('Question Content', "", key="question_input")

    if st.button("Submit Question"):
        new_question_data = {
            "sID": userID,
            "question_content": question_content,
            "abroadProgram": int(abroad_program)    
        }
        try:
            response = requests.post("http://api:4000/ap/postAQuestion", json=new_question_data)

            if response.status_code == 200:
                st.success("Your question was submitted successfully!")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

st.write("Fill in the details below and submit to add a new question.")
with st.expander("Add Question"):
    submit_question()

# def submit_reply():
#     st.write("Add a New Reply")

#     reply_body = st.text_input("Reply Body", "", key="reply_form")
        
#     if st.button("Submit new reply"):
#         new_reply = {
#             'student_id': userID,
#             'body': reply_body


# # add reply ID
# # add qID as a field

#         }
#         try:
#             response = requests.post(f"http://api:4000/qr/add_reply", json=new_reply)
            
#             if response.status_code == 200:
#                 st.success("Your reply was submitted successfully!")
#             else:
#                 st.error(f"Error: {response.status_code}, {response.text}")
#         except requests.exceptions.RequestException as e:
#             st.error(f"Request failed: {e}")

# st.write("Fill in the details below and submit to add a new reply.")
# with st.expander("Add Reply"):
#     submit_reply()

# st.subheader(f"Questions/Replies")
# for i, question in enumerate(questions, start=1):
#     st.write(f"### Question {i}")
#     for key, value in question.items():
#         st.write(f"**{key.capitalize()}:** {value}")
#         st.subheader(f"Questions/Replies")

# for i, replies in enumerate(replies, start=1):
#     st.write(f"### Reply {i}")
#     for key, value in replies.items():
#         st.write(f"**{key.capitalize()}:** {value}")


        
