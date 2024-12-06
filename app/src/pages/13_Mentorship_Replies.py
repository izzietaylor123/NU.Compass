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

st.write("### Questions:")
if questions:
    for question in questions:
        st.write(f"- {question['content']}")
else:
    st.warning("No questions available for this user.")


if st.session_state['role'] == 'mentor_student':
    st.write("### Replies:")
    if replies:
        for reply in replies:
            st.write(f"- {reply['content']}")
    else:
        st.warning("No replies available for this user.")


with st.expander("Add a New Question"):
    with st.form(key="question_form"):
        question_body = st.text_area("Question")
        
        submit_question = st.form_submit_button("Submit Question")
        
        if submit_question:
            new_question = {
                "sID": userID,
                "body": question_body
            }
            
            response = requests.post("http://api:4000/qr/add_question", json=new_question)
            
            if response.status_code == 200:
                st.success("Your question was submitted successfully!")

            else:
                st.error("There was an error submitting your question.")

if st.session_state['role'] == 'mentor_student':

    mentees_route = f"http://api:4000/m/get_mentees/{userID}"
    mentees = requests.get(mentees_route).json()
    if mentees:
        for mentee in mentees:
            m = mentee['sID']
            questions_route = f"http://api:4000/qr/get_questions/{mentee['sID']}"
            questions = requests.get(questions_route).json()
            with st.expander(f"Add a New Reply For Mentee {m}"):
                with st.form(key=f"reply_form_for_{m}"):
                    reply_body = st.text_area("Reply Body")
                    question_id = st.selectbox("Select Question to Reply To", [q['content'] for q in questions])
                    
                    submit_reply = st.form_submit_button("Submit Reply")
                    
                    if submit_reply:
                        question_id_selected = next(q['qID'] for q in questions if q['content'] == question_id) 
                        new_reply = {
                            "student_id": userID,
                            "body": reply_body,
                            "qID" : question_id_selected
                        }

                        response = requests.post(f"http://api:4000/qr/add_reply", json=new_reply)
                        
                        if response.status_code == 200:
                            st.success("Your reply was submitted successfully!")
                        else:
                            st.error("There was an error submitting your reply.")


        
