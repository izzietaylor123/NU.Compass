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
# Get location details for italy

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
# Makes use of the very simple ML model in to predict a value
# and returns it to the user - NOT SURE IF WE NEED THIS FOR OUR PROJ
''''
@customers.route('/prediction/<var01>/<var02>', methods=['GET'])
def predict_value(var01, var02):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')

    returnVal = predict(var01, var02)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
'''