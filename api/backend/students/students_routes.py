from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
students = Blueprint('students', __name__)

#------------------------------------------------------------
# Get all students from the system
@students.route('/students', methods=['GET'])
def get_all_students():

    cursor = db.get_db().cursor()
    query = '''
        SELECT sID, fName, lName, email, blurb, role 
        FROM Student'''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all student mentors from the system
@students.route('/mentors', methods=['GET'])
def get_all_mentors():

    cursor = db.get_db().cursor()
    query = '''
        SELECT sID, fName, lName, email, blurb, role
        FROM Student
        WHERE role = 'mentor' '''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all student mentees from the system
@students.route('/mentees', methods=['GET'])
def get_all_mentees():

    cursor = db.get_db().cursor()
    query = '''
        SELECT sID, fName, lName, email, blurb, role
        FROM Student
        WHERE role = 'mentee' '''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get a student from the system
@students.route('/get_student/<sID>', methods=['GET'])
def get_student(sID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT fName, lName, email, role, blurb
        FROM Student
        WHERE sID = {str(sID)} '''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Get mentor-mentee match data 
@students.route('/mmMatch', methods=['GET'])
def mentor_mentee_match():

    cursor = db.get_db().cursor()
    query = '''SELECT matchID, menteeID, mentorID, dateMatched
    FROM mentorshipMatch'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Get all of of a mentor's mentees from the system
@students.route('/mentors/mentees/<sID>', methods=['GET'])
def get_mentors_mentees(sID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT email, fName, lName, blurb, role
        FROM mentorshipMatch JOIN Student
        WHERE role = 'mentee' AND matchID = {str(sID)}
        '''
    cursor.execute(query)
    
    mentors = cursor.fetchall()
    
    the_response = make_response(jsonify(mentors))
    the_response.status_code = 200    
    return the_response

# #------------------------------------------------------------
# Get student blurb data 
@students.route('/get_blurb/<sID>', methods=['GET'])
def get_student_blurb(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT blurb
    FROM Student
    WHERE sID = {str(sID)}'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Get student email data 
@students.route('/get_email/<sID>', methods=['GET'])
def get_student_email(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT email
    FROM Student
    WHERE sID = {str(sID)}'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Get student ratings data 
@students.route('/get_ratings/<sID>', methods=['GET'])
def get_student_ratings(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT programID, locRating, profRating, atmosphereRating, comment
    FROM Rating
    WHERE sID = {str(sID)}'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# #------------------------------------------------------------
# Get a mentee's mentor
@students.route('/get_mentor_id/<sID>', methods=['GET'])
def get_mentor_id(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT mentorID
    FROM mentorshipMatch
    WHERE menteeID = {str(sID)}'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get pic from student PFP
@students.route('/get_student_pfp/<sID>', methods=['GET'])
def get_student_pic(sID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT pfpPath 
        FROM Student
        WHERE sID = {str(sID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response



