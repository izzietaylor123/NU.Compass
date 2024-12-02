from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict
# # commented out stuff was attempt to refactor. 
# refactoring made worse, so commented out.
# #------------------------------------------------------------
# # Create a new Blueprint object, which is a collection of 
# # routes.
# abroad_programs = Blueprint('abroad_programs', __name__)


# #------------------------------------------------------------
# # Get all locations from the system
# @abroad_programs.route('/abroad_programs', methods=['GET'])
# def get_all_programs():

#     cursor = db.get_db().cursor()
#     query = '''SELECT programID, programName, prgmDescription, locationID, programType FROM abroadProgram'''
#     cursor.execute(query)
    
#     locations = cursor.fetchall()
    
#     the_response = make_response(jsonify(locations))
#     the_response.status_code = 200
#     return the_response

# # Helper function to calculate the average rating
# def get_average_rating(program_id, rating_type):
#     cursor = db.get_db().cursor()
#     query = f'''
#         SELECT AVG({rating_type}) 
#         FROM Rating
#         WHERE programID = %s
#     '''
#     cursor.execute(query, (program_id,))
#     result = cursor.fetchone()
#     return result[0] if result else None

# #------------------------------------------------------------
# # Get programID from city name
# @abroad_programs.route('/abroad_programs/city/<cityname>', methods=['GET'])
# def get_program_id(cityname):
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT programID
#         FROM abroadProgram
#         JOIN location ON location.locationID = abroadProgram.locationID
#         WHERE location.city = %s
#     '''
#     cursor.execute(query, (cityname,))
#     locations = cursor.fetchall()
#     the_response = make_response(jsonify(locations))
#     the_response.status_code = 200
#     return the_response

# #------------------------------------------------------------
# # Get location rating from the system
# @abroad_programs.route('/abroad_programs/location_rating/<int:programID>', methods=['GET'])
# def get_location_rating(programID):
#     avg_rating = get_average_rating(programID, 'locRating')
#     if avg_rating is not None:
#         return jsonify({"location_rating": avg_rating}), 200
#     else:
#         return jsonify({"error": "Program not found or no ratings available"}), 404


# #------------------------------------------------------------
# # Get professor rating from the system
# @abroad_programs.route('/abroad_programs/professor_rating/<int:programID>', methods=['GET'])
# def get_professor_rating(programID):
#     avg_rating = get_average_rating(programID, 'profRating')
#     if avg_rating is not None:
#         return jsonify({"professor_rating": avg_rating}), 200
#     else:
#         return jsonify({"error": "Program not found or no ratings available"}), 404


# #------------------------------------------------------------
# # Get atmosphere rating from the system
# @@abroad_programs.route('/abroad_programs/atmosphere_rating/<int:programID>', methods=['GET'])
# def get_atmosphere_rating(programID):
#     avg_rating = get_average_rating(programID, 'atmosphereRating')
#     if avg_rating is not None:
#         return jsonify({"atmosphere_rating": avg_rating}), 200
#     else:
#         return jsonify({"error": "Program not found or no ratings available"}), 404
# #

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
abroad_programs = Blueprint('abroad_programs', __name__)


#------------------------------------------------------------
# Get all locations from the system
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
# Get location rating from the system
@abroad_programs.route('/location_rating/{programID}', methods=['GET'])
def get_location_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(locRating) 
        FROM Rating
        WHERE programID = str{programID}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get professor rating from the system
@abroad_programs.route('/professor_rating/{programID}', methods=['GET'])
def get_professor_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(profRating) 
        FROM Rating
        WHERE programID = str{programID}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get atmosphere rating from the system
@abroad_programs.route('/abroad_programs', methods=['GET'])
def get_atmosphere_rating(programID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT AVG(atmosphereRating) 
        FROM Rating
        WHERE programID = str{programID}'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response
