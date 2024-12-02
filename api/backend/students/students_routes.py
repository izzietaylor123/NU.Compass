from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
students = Blueprint('students', __name__)

#------------------------------------------------------------
# Get all students from the system
@students.route('/students', methods=['GET'])
def get_all_students():

    cursor = db.get_db().cursor()
    query = '''SELECT sID, fName, lName, email, blurb, role FROM Student'''
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

