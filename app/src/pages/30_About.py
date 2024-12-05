import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks(show_home=True)

st.write("# About this App")

st.markdown (
    """
    This is a demo app for a CS 3200 Course Project by Isabel Taylor, Ashna Shah, Sarah Wang, Ava Toren and Lara Goyal.  

    The goal of this demo is to mock an app that can create bridges between students on abroad programs, giving them resources to 
    learn more about programs and connect with one another. 

    We hope that it can help students preparing to go abroad make informed decisions and feel more confident in the adventure that 
    awaits them, and that students returing from being abroad can give back to and maintain their abroad community!

    Stay tuned for more information and features to come!
    """
        )
