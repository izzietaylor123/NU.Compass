import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome to Paris, France!")

st.write("The Northeastern Paris N.U.in Program offers first-year students\
         the chance to study abroad in one of the world’s most iconic cities. \
         In Paris, students immerse themselves in the city’s rich history, culture, and art \
         while taking courses that blend global perspectives with their academic focus. \
         Beyond the classroom, students explore landmarks like the Eiffel Tower, the Louvre, and Montmartre, \
         gaining firsthand experience of Parisian life. The program also integrates opportunities for professional development, \
         including the potential for co-op placements in international companies or organizations based in Paris. \
         Through this experience, students develop not only academic knowledge but also a deep appreciation for French culture\
        and the global context in which they are studying.")