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
# Get tim mentor from the system
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

#------------------------------------------------------------
# Get tom mentee from the system
@students.route('/tom', methods=['GET'])
def tom():

    cursor = db.get_db().cursor()
    query = '''
        SELECT fName, lName, email, blurb
        FROM Student
        WHERE sID = 32 '''
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
# # Get all of tim's mentees from the system
# @students.route('/tim/matches', methods=['GET'])
# def get_tim_matches():

#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT menteeID
#         FROM mentorshipMatch
#         WHERE mentorID = 31 '''
#     cursor.execute(query)
    
#     mentors = cursor.fetchall()
    
#     the_response = make_response(jsonify(mentors))
#     the_response.status_code = 200
#     return the_response

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
# Get student ratings data 
@students.route('/get_mentor_id/<menteeID>', methods=['GET'])
def get_mentor_id(menteeID):

    cursor = db.get_db().cursor()
    query = f'''SELECT mentorID
    FROM mentorshipMatch
    WHERE menteeID = {str(menteeID)}'''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response