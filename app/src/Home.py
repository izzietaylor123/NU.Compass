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

# streamlit supports regular and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout='wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

st.session_state['program'] = -1

st.session_state['userID'] = -1

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# for aesthetics
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom, #f7f8fa, #e9ecef);
        }
        .main-title {
            font-size: 2.8em;
            color: #c0392b;
            font-weight: bold;
            text-align: center;
            margin-bottom: 1.5em;
        }
        .subtitle {
            font-size: 1.6em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 2em;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }
        .button {
            background-color: #c0392b;
            color: white;
            border: none;
            padding: 15px 30px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 10px;
            cursor: pointer;
            width: 400px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")

left_col, center_col, right_col = st.columns([2, 3, 2])
with center_col:
    st.title(" :red[NU.Compass]")
    st.write("#### *The Pack Goes Global*")

st.write('')
st.write('')

st.write('')


st.markdown("#### Welcome! Which user would you like to log in as?")

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

# Button container
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

if st.button('Act as Tim Walz, an abroad alum student looking to be a mentor', 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'mentor_student'
    st.session_state['first_name'] = 'Tim'
    st.session_state['full_name'] = 'Tim Walz'
    st.session_state['userID'] = 31
    st.switch_page('pages/10_Mentor.py')
    
if st.button("Act as Tom Holland, an incoming abroad student looking to be a mentee", 
            type='primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'mentee_student'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'Tom'
    st.session_state['full_name'] = 'Tom Holland'
    st.session_state['userID'] = 32
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Mentee Student Persona")
    st.switch_page('pages/00_Mentee_Home.py')

if st.button('Act as Andy Samberg, a Northeastern IT Administrator', 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'Andy'
    st.session_state['full_name'] = 'Andy Samberg'
    st.switch_page('pages/20_IT_Admin_Home.py')

if st.button('Act as Adam Brody, a Northeastern Global Experience Staff Member and Data Analyst',
             type='primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'GESM'
    st.session_state['first_name'] = 'Adam'
    st.session_state['full_name'] = 'Adam Brody'
    st.switch_page('pages/26_GEOAdmin_Home.py')

# # image for home
# st.markdown("</div>", unsafe_allow_html=True)
# st.image("assets/home.png", width=500)