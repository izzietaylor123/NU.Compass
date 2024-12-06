from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

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
@abroad_programs.route('/abroad_programs/<programID>', methods=['PUT'])
def update_program(program_id):
    
    program_data = request.json 

    # extract variables
    prog_ID = program_data['programID']
    name = program_data['programName']
    description = program_data['prgmDescription']
    loc_ID = program_data['locationID']
    ptype = program_data['programType']
    emp_ID = program_data['empID']

    query = '''UPDATE abroadProgram SET programName = %s, prgmDescription = %s, 
    locationID = %s, programType = %s WHERE programID = %s'''

    cursor = db.get_db().cursor()
    cursor.execute(query, (prog_ID, name, description, loc_ID, ptype, emp_ID))
    db.get_db().commit()
    
    response = make_response("Successfully updated abroad program")
    response.status_code = 200
    
    return 'abroad program created!'

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
# Add a new abroad program to the database

@abroad_programs.route('/add_abroad_programs', methods=['POST'])
def add_programs():

    program_data = request.json

    # extract variables
    prog_ID = program_data['programID']
    name = program_data['programName']
    description = program_data['prgmDescription']
    loc_ID = program_data['locationID']
    ptype = program_data['programType']
    emp_ID = program_data['empID']

    query = f'''INSERT INTO abroadProgram (programID, programName, prgmDescription, locationID, programType, empID, prgmPhotoPath)
    VALUES ({prog_ID}, "{name}", "{description}", {loc_ID}, "{ptype}", {emp_ID}, 'generic_loc_image.png')'''

    current_app.logger.info(query)
    

    cursor = db.get_db().cursor()
    cursor.execute(query) #(prog_ID, name, description, loc_ID, ptype, emp_ID, 'generic_loc_image.png'))
    db.get_db().commit()

    response = make_response("Successfully added new abroad program")
    response.status_code = 200
    return 'abroad program created!'

#------------------------------------------------------------
# Add a new rating for an abroad program to the database

@abroad_programs.route('/add_rating', methods=['POST'])
def add_rating():

    rating_data = request.json

    # extract variables
    locR = rating_data['location_rating']
    profR = rating_data['professor_rating']
    atmR = rating_data['atmosphere_rating']
    comment = rating_data['comment']
    sID = rating_data['sID']
    program = rating_data['abroadProgram']

    query = f'''INSERT INTO Rating (programID, sID, locRating, profRating, atmosphereRating, comment)
    VALUES ({program}, {sID}, {locR}, {profR}, {atmR}, "{comment}")'''

    current_app.logger.info('Inserting location with ID: %s', program)

    cursor = db.get_db().cursor()
    cursor.execute(query) #, (prog_ID, name, description, loc_ID, ptype, emp_ID, image))
    db.get_db().commit()

    response = make_response("Successfully added new abroad program")
    response.status_code = 200
    return 'abroad program created!'


#------------------------------------------------------------
# Delete a location from the database

@abroad_programs.route('/abroad_programs/<programID>', methods=['DELETE'])
def delete_abroad_program(programID):

    query = '''DELETE FROM abroadProgram WHERE programID = %s'''

    current_app.logger.info('Attempting to delete program with ID: %s', programID)

    cursor = db.get_db().cursor()
    cursor.execute(query, (programID))
    db.get_db().commit()

    # handle cases where no program is found
    if cursor.rowcount == 0:
        return make_response(f"Program not found", 404)

    response = make_response(f"Program with ID {programID} deleted successfully")
    response.status_code = 200
    return 'program deleted!'


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
# Get country from programID
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
        WHERE abroadProgram = {str(programID)} AND isApproved = True'''
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
        WHERE qID = {str(qID)} AND isApproved = True'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Post a question
@abroad_programs.route('/postAQuestion', methods=['POST'])
def add_question():

    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    sID = the_data['sID']
    content = the_data['question_content']
    abroad_program = the_data['abroadProgram']

    cursor = db.get_db().cursor()
    query = f'''
        INSERT INTO Question(sID, content, abroadProgram, isApproved)
        VALUES({sID}, "{content}", {abroad_program}, 0)'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get Alerts from a programID
@abroad_programs.route('/get_alerts/<programID>', methods=['GET'])
def get_alerts(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT Alerts.message, Alerts.datePosted 
        FROM Alerts
        JOIN Location ON Location.locationID = Alerts.locationID
        JOIN abroadProgram ON abroadProgram.locationID = Location.locationID
        WHERE abroadProgram.programID = {str(programID)}
        ORDER BY datePosted DESC'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get pic from programID
@abroad_programs.route('/get_program_pic/<programID>', methods=['GET'])
def get_program_pic(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT prgmPhotoPath 
        FROM abroadProgram
        WHERE programID = {programID}'''
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    the_response = make_response(jsonify(data))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get comments from programID
@abroad_programs.route('/get_comments/<programID>', methods=['GET'])
def get_comments(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT comment, sID
        FROM Rating
        WHERE programID = {str(programID)}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response