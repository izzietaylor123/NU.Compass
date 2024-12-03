##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
import requests
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

st.session_state['program'] = -1

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('NU.Connect')
st.write('\n\n')
st.write('### Welcome! Which user would you like to log in as?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 


if st.button('Act as Tim Walz, an abroad alum student looking to be a mentor', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'mentor_student'
    st.session_state['first_name'] = 'Tim'
    st.switch_page('pages/10_Mentor.py')
    
if st.button("Act as Tom Holland, an incoming abroad student looking to be a mentee", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'mentee_student'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'Tom'
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Mentee Student Persona")
    st.switch_page('pages/00_Mentee_Home.py')


if st.button('Act as Andy Samberg, a Northeastern IT Administrator', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'Andy'
    st.switch_page('pages/20_Admin_Home.py')


if st.button('Act as Adam Brody, a Northeastern Global Experience Staff Member and Data Analyst',
             type = 'primary',
             use_container_width = True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'GESM'
    st.session_state['first_name'] = 'Adam'
    st.switch_page('pages/26_GEOAdmin_Home.py');
