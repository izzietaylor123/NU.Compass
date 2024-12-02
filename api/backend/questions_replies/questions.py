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
questions_replies = Blueprint('questions_and_replies', __name__)

#------------------------------------------------------------
# Get all approved questions from the system
@questions_replies.route('/questions_and_replies/questions', methods=['GET'])
def get_approved_questions():

    cursor = db.get_db().cursor()
    query = '''
        SELECT qID, sID, content
        FROM Question
        Where isApproved = 1 '''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all approved replies from the system
@questions_replies.route('/questions_and_replies/replies', methods=['GET'])
def get_approved_replies():

    cursor = db.get_db().cursor()
    query = '''
        SELECT replyID, sID, content
        FROM Reply
        Where isApproved = 1 '''
    cursor.execute(query)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response