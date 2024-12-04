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
locations = Blueprint('locations', __name__)


#------------------------------------------------------------
# Get all locations from the system
@locations.route('/locations', methods=['GET'])
def get_all_locations():

    cursor = db.get_db().cursor()
    query = '''SELECT locationID, city, country, description FROM Location'''
    cursor.execute(query)
    
    locations = cursor.fetchall()
    
    the_response = make_response(jsonify(locations))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Update location info for location with particular locationID
@locations.route('/locations', methods=['PUT'])
def update_locations():
    current_app.logger.info('PUT /locations route')
    loc_info = request.json
    loc_id = loc_info['locationID']
    city = loc_info['city']
    country = loc_info['country']
    description = loc_info['description']

    query = 'UPDATE locations SET city = %s, country = %s, description = %s where locationID = %s'
    data = (city, country, description, loc_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'location updated!'

#------------------------------------------------------------
# Add a new location to the database

@locations.route('/locations', methods=['POST'])
def add_locations():

    loc_data = request.json

    # extract variables
    loc_id = loc_data['locationID']
    city = loc_data['city']
    country = loc_data['country']
    description = loc_data['description']

    query = '''INSERT INTO locations (locationID, city, country, description)
    VALUES (%s, %s, %s, %s)'''

    current_app.logger.info('Inserting location with ID: %s', loc_id)

    cursor = db.get_db().cursor()
    cursor.execute(query, (loc_id, city, country, description))
    db.get_db().commit()

    response = make_response("Successfully added new location")
    response.status_code = 200
    return 'location created!'


#------------------------------------------------------------
# Get location details for location with particular locationID

@locations.route('/locations/<locationID>', methods=['GET'])
def get_locations(locationID):
    current_app.logger.info('GET /locations/<locationID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT locationID, city, country, description FROM Location WHERE id = {0}'.format(locationID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------