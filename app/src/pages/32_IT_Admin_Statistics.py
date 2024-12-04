import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import matplotlib.pyplot as plt

from st_keyup import st_keyup

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title('User Statistics')
st.write('')

# Importing the data
mentor_data = requests.get('http://api:4000/s/mentors').json()
mentee_data = requests.get('http://api:4000/s/mentees').json()

abroad_programs_data = requests.get('http://api:4000/ap/abroad_programs').json()
locations = requests.get('http://api:4000/l/locations').json()

# Make a bar chart comparing the number of mentors to mentees
user_counts = {}
user_counts["Mentor"] = 0
user_counts["Mentee"] = 0

for mentor in mentor_data:
    user_counts["Mentor"] += 1
for mentee in mentee_data:
     user_counts["Mentee"] += 1

st.write(f"Number of Mentees: {user_counts['Mentee']}, Number of Mentors: {user_counts['Mentor']}")
plt.bar(user_counts.keys(), user_counts.values(), color=['blue', 'red'])
plt.title('Mentor vs Mentee')
plt.xlabel('Category')
plt.ylabel('Count')
st.pyplot(plt)

# Make a pie chart of abroad programs separated by country
location_counts = {}
for location in locations:
     country = location["country"]
     if country: 
            location_counts[country] = location_counts.get(country, 0) + 1

st.write(f"{location_counts}")
labels = location_counts.keys()
sizes = location_counts.values()
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=.85, labeldistance=1.4)
st.pyplot(plt)
