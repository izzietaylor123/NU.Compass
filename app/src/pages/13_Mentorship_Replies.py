import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

# Page title
st.title("My Replies to Mentee Questions")

# Sample data (you can replace this with dynamic data or a database query)
mentee_name = "Jane Doe"
questions_and_replies = [
    {
        "question": "What is the best way to prepare for exams?",
        "reply": "Creating a study schedule and practicing past questions are great ways to prepare effectively. Make sure to also take regular breaks!"
    },
    {
        "question": "How do I stay motivated during difficult projects?",
        "reply": "Break the project into smaller tasks and focus on achieving one at a time. Reward yourself for completing milestones to stay motivated."
    },
    {
        "question": "What books would you recommend for personal growth?",
        "reply": "Some great options are 'Atomic Habits' by James Clear, 'Mindset' by Carol Dweck, and 'The Power of Now' by Eckhart Tolle."
    },
]

# Display mentee name prominently
st.header(f"Replies for: {mentee_name}")

# Iterate through the questions and replies
for idx, qa in enumerate(questions_and_replies):
    st.subheader(f"Question {idx + 1}")
    st.markdown(f"**Question:** {qa['question']}")
    st.markdown(
        f"<div style='font-size: 1.2em; font-weight: bold; color: #333;'>Reply: {qa['reply']}</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")  # Separator for clarity

