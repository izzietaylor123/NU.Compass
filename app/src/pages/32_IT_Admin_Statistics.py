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
st.write('')
st.write('### Welcome to the hub for usage and data statistics. Click below to view current app data.')

# Importing the data
mentor_data = requests.get('http://api:4000/s/mentors').json()
mentee_data = requests.get('http://api:4000/s/mentees').json()

abroad_programs_data = requests.get('http://api:4000/ap/abroad_programs').json()
locations = requests.get('http://api:4000/l/locations').json()

# Make a bar chart comparing the number of mentors to mentees
with st.expander("View Data on User Counts"):
     st.subheader("Mentor vs. Mentee Usage")
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
     plt.close()


# Make a pie chart of abroad programs separated by country
col1, col2 = st.columns(2)

with col1: 
     with st.expander("View Locations Data"):
          location_counts = {}
          for location in locations:
               country = location["country"]
               if country: 
                    location_counts[country] = location_counts.get(country, 0) + 1

          labels = location_counts.keys()
          sizes = location_counts.values()
          fig, ax = plt.subplots()
          wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.25, rotatelabels=True)

          # making the percentages angled to avoid overlap
          for i, autotext in enumerate(autotexts):
               angle = (i * 360) / len(autotexts)
               autotext.set_rotation(angle)
          
          ax.set(aspect="equal")
          st.pyplot(fig)
          plt.close(fig)

# Make a bar chart comparing the number of different types of abroad programs
with col2: 
     with st.expander("View Abroad Program Data"):
          program_type_counts = {}
          for program in abroad_programs_data:
               type = program["programType"]
               if type:
                    program_type_counts[type] = program_type_counts.get(type, 0) + 1


          plt.bar(program_type_counts.keys(), program_type_counts.values(), color=["green", "purple", "yellow", "orange"])
          plt.title('Count per Abroad Program Type')
          plt.xticks(rotation=45)
          plt.xlabel('Program Type')
          plt.ylabel('Count')
          st.pyplot(plt)

