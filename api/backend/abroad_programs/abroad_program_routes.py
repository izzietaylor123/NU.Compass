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
abroad_programs = Blueprint('abroad_programs', __name__)


#------------------------------------------------------------
# Get all programs from the system
@abroad_programs.route('/abroad_programs', methods=['GET'])
def get_all_programs():

    cursor = db.get_db().cursor()
    query = '''SELECT programID, programName, prgmDescription, locationID, programType FROM abroadProgram'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get all program names from the system
@abroad_programs.route('/get_all_program_ids', methods=['GET'])
def get_all_program_ids():

    cursor = db.get_db().cursor()
    query = '''SELECT programID FROM abroadProgram'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get location rating from the system
@abroad_programs.route('/location_rating/<programID>', methods=['GET'])
def get_location_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(locRating) 
        FROM Rating
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get professor rating from the system
@abroad_programs.route('/professor_rating/<programID>', methods=['GET'])
def get_professor_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(profRating) 
        FROM Rating
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get atmosphere rating from the system
@abroad_programs.route('/atmosphereRating/<programID>', methods=['GET'])
def get_atmosphere_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(atmosphereRating) 
        FROM Rating
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get city from programID
@abroad_programs.route('/get_city/<programID>', methods=['GET'])
def get_city(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT Location.city 
        FROM abroadProgram
        JOIN Location
        ON Location.locationID = abroadProgram.locationID
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get city from programID
@abroad_programs.route('/get_country/<programID>', methods=['GET'])
def get_country(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT Location.country 
        FROM abroadProgram
        JOIN Location
        ON Location.locationID = abroadProgram.locationID
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get program description from programID
@abroad_programs.route('/program_description/<programID>', methods=['GET'])
def get_program_description(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT prgmDescription 
        FROM abroadProgram
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all questions from programID
@abroad_programs.route('/all_questions/<programID>', methods=['GET'])
def get_program_questions(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT qID, content 
        FROM Question
        WHERE abroadProgram = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get replies from a questionID
@abroad_programs.route('/replies/<qID>', methods=['GET'])
def get_replies(qID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT content 
        FROM Reply
        WHERE qID = {str(qID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response