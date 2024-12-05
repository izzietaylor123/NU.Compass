import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

from st_keyup import st_keyup

user_role = st.session_state.get("role", "guest")
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

programID = st.session_state.program


cityroute = f'http://api:4000/ap/get_city/{programID}'
city = requests.get(cityroute).json()
city = city[0]['city']
countryroute = f'http://api:4000/ap/get_country/{programID}'
country = requests.get(countryroute).json()
country = country[0]['country']



title = "Welcome to " + str(city) +  ", " + str(country) + "!"

st.title(title)
st.write('')

left_co, cent_co = st.columns((1, 2))
with left_co:
    st.image("assets/eiffel_tower.png")

with cent_co:

    st.write(' ')
    st.write(' ')
    st.write(' ')

    locRatRoute = f'http://api:4000/ap/location_rating/{programID}'
    locationRating = requests.get(locRatRoute).json()
    locationRating = locationRating[0]['AVG(locRating)']

    profRatRoute = f'http://api:4000/ap/professor_rating/{programID}'
    professorRating = requests.get(profRatRoute).json()
    professorRating = professorRating[0]['AVG(profRating)']

    atmRatRoute = f'http://api:4000/ap/atmosphereRating/{programID}'
    atmosphereRating = requests.get(atmRatRoute).json()
    atmosphereRating = atmosphereRating[0]['AVG(atmosphereRating)']


    if locationRating and professorRating and atmosphereRating:
        averageRating = round(((float(locationRating) + float(professorRating) + float(atmosphereRating)) / 3), 2)
        atmosphereRating = float(atmosphereRating)
        locationRating = float(locationRating)
        professorRating = float(professorRating)

        st.write('')
        avgR = 'Average rating: ' + str(averageRating) + ' '
        for i in range (int(averageRating)):
            avgR = avgR + '⭐️'
        st.write('###', avgR)

        st.write('')
        lr = 'Location rating: ' + str(round((locationRating), 2)) + ' '
        for i in range (int(locationRating)):
            lr = lr + '⭐️'
        st.write(lr)

        st.write('')

        pr = 'Professor rating: ' + str(round((professorRating), 2)) + ' '
        for i in range (int(professorRating)):
            pr = pr + '⭐️'
        st.write(pr)

        st.write('')
        ar = 'Atmosphere rating: ' + str(round((atmosphereRating), 2)) + ' '
        for i in range (int(atmosphereRating)):
            ar = ar + '⭐️'
        st.write(ar)
    else:
        st.write("This program hasn't been rated yet!")
    
    if st.button('View Alerts for this Program', 
                    type='secondary',
                    use_container_width=True):
            st.switch_page('pages/08_Display_Alerts.py')

# Accesses and writes the program description based on the programID of the session_state
descriptionRoute = f'http://api:4000/ap/program_description/{programID}'
description = requests.get(descriptionRoute).json()
description = description[0]['prgmDescription']
st.write(description)

st.subheader("Program FAQs")

# get all questions
questionsroute = f'http://api:4000/ap/all_questions/{programID}'

question_list = requests.get(questionsroute).json()

if question_list: 
    for question in question_list: 
        question_content = "Q: " + str(question['content'])
        st.write(question_content)
        qID = question['qID']
        replies_route = f'http://api:4000/ap/replies/{qID}'
        replies_list = requests.get(replies_route).json()
        if replies_list:
            for replies in replies_list:
                reply = ">>>   A: " + str(replies['content'])
                st.write(reply)
        else:
            st.write("No replies yet.")        
else:
    st.write("No questions asked yet.")        


st.subheader("Ask a question!")


# Create a Streamlit form widget
with st.form("add_question_form"):
    
    # Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    question_content = st.text_input("Question Content")
    sID = st.session_state['userID']
    isAproved = False
    abroadProgram = programID
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Ask Question")
    
    if submit_button:
        
        # Package the data up that the user entered into 
        # a dictionary (which is just like JSON in this case)
        question_data = {
            "question_content": question_content,
            "sID": sID,
            "abroadProgram": abroadProgram
        }
        
        # printing out the data - will show up in the Docker Desktop logs tab
        # for the web-app container 
        logger.info(f"Question form submitted with data: {question_data}")
        
        # Now, we try to make a POST request to the proper end point
        try:
            # using the requests library to POST to /p/product.  Passing
            # product_data to the endpoint through the json parameter.
            # This particular end point is located in the products_routes.py
            # file found in api/backend/products folder. 
            response = requests.post('http://api:4000/ap/postAQuestion', json=question_data)
            if response.status_code == 200:
                st.success("Question added successfully!")
            else:
                st.error(f"Error adding product: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")

# Delete abroad program (only if administrator)
def delete_program():
    response = requests.delete('http://api:4000/abroad_programs/{programID}') 
    if response.status_code == 200:
        st.write("Program has been deleted.")

if user_role == 'administrator':
    # Delete location once button is pressed
    if st.button('Delete Location', 
            type='primary',
            use_container_width=True):
        delete_program()
       
def update_program():
    with st.form("update_program_form"):
        program_name = st.text_input("Program Name")
        prog_desc = st.text_area("Program Description")
        loc_id = st.text_input("Location ID")
        prog_type = st.text_input("Program Type")
        emp_id = st.text_input("Employee ID")
        if st.form_submit_button("Update Abroad Program"):
            updated_program_data = {"programName": program_name, 
            "prgm Description": prog_desc, "locationID": loc_id, 
            "empID": emp_id
            }
            response = requests.put(f'http://api:4000/abroad_programs/{programID}', json=updated_program_data)
    
# Update abroad program (only if administrator)
if user_role == 'administrator':
    # Delete location once button is pressed
    if st.button('Update Location', 
            type='primary',
            use_container_width=True):
        update_program()