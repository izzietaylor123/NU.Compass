from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

mentees = Blueprint('mentees', __name__)


#------------------------------------------------------------
# Get all mentors from the system
@mentees.route('/mentees', methods=['GET'])
def get_all_mentees():

    cursor = db.get_db().cursor()
    query = '''SELECT sID, fName, lName, email, blurb, role FROM Students
    WHERE role = mentee'''
    cursor.execute(query)
    
    mentees = cursor.fetchall()
    
    the_response = make_response(jsonify(mentees))
    the_response.status_code = 200
    return the_response