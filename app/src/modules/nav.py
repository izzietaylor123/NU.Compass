# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About NU.Connect", icon="🧠")


#### ------------------------ Examples for Role of mentee_student ------------------------

def menteeHomeNav():
    st.sidebar.page_link(
        "pages/00_Mentee_Home.py", label="Mentee Student Home", icon="👤"
)


## ------------------------ Examples for Role of mentor_student ------------------------
def mentor_student_home():
    st.sidebar.page_link("pages/12_API_Test.py", label="Mentor Student Home", icon="👤")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ Global Experience Staff Member ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/neulogo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If the user role is a mentee_student
        if st.session_state["role"] == "mentee_student":
            menteeHomeNav()

        # If the user role is mentor student 
        if st.session_state["role"] == "mentor_student":
            mentor_student_home()
            ClassificationNav()

        # If the user is an IT administrator
        if st.session_state["role"] == "administrator":
            AdminPageNav()

        # If the user is a Global Experience Staff Member
        if st.session_state["role"] == "GESM":
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
