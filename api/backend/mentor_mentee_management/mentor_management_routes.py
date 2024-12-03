from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

mentors = Blueprint('mentors', __name__)

#------------------------------------------------------------
# Get all mentors from the system
@mentors.route('/mentors', methods=['GET'])
def get_all_mentors():

    cursor = db.get_db().cursor()
    query = '''SELECT sID, fName, lName, email, blurb, role FROM Students
    WHERE role = 'mentor' '''
    cursor.execute(query)
    
    mentors = cursor.fetchall()
    
    the_response = make_response(jsonify(mentors))
    the_response.status_code = 200
    return the_response