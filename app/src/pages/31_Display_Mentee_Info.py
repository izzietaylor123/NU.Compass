import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

sID = st.session_state.mentee

mentee_data = requests.get('http://api:4000/s/mentees').json()

# Ensure only specific mentor's profile is being accessed
for mentee in mentee_data:
    if mentee['sID'] == sID:
        selected_mentee = mentee
        break

# Provide personal information for the specified mentor
if selected_mentee:
    last_name = selected_mentee['lName']
    first_name = selected_mentee['fName']
    email = selected_mentee['email']
    blurb = selected_mentee['blurb']
    title = str(last_name) + ", " + str(first_name)

    pg_title = f"Welcome to {last_name}, {first_name}'s Profile:"

    st.title(pg_title)
    st.write(f"**Student ID**: {selected_mentee['sID']}")
    st.write(f"**Full Name**: {first_name} {last_name}")
    st.write(f"**Email**: {email}")
    st.write(f"**Here is {first_name}'s blurb**: {blurb}")
        
# Find replies associated with this mentor
mentee_replies = requests.get('http://api:4000/qr//questions_and_replies/replies')
mentee_replies = mentee_replies.json()

selected_replies = [reply for reply in mentee_replies if reply.get('sID') == sID]
if selected_replies:
    st.write(f"Here are {first_name}'s replies:")
    for reply in selected_replies:
        st.write(f"- {reply['replyID']}: {reply['content']}")
else:
    st.write(f"{first_name} has not written any replies yet.")

# Find questions associated with this mentor
mentee_questions = requests.get('http://api:4000/qr//questions_and_replies/questions')
mentee_questions = mentee_questions.json()

selected_questions = [question for question in mentee_questions if question.get('sID') == sID]
if selected_questions:
    st.write(f"Here are {first_name}'s questions:")
    for question in selected_questions:
        st.write(f"- {question['qID']}: {question['content']}")
else:
    st.write(f"{first_name} has not written any questions yet.")
