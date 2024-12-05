from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

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

# #------------------------------------------------------------
# Get student replies data 
@questions_replies.route('/get_replies/<sID>', methods=['GET'])
def get_student_replies(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT content
        FROM Reply
        WHERE sID = {str(sID)}'''
    cursor.execute(query)

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Get student question data 
@questions_replies.route('/get_questions/<sID>', methods=['GET'])
def get_student_questions(sID):

    cursor = db.get_db().cursor()
    query = f'''SELECT content
        FROM Question
        WHERE sID = {str(sID)}'''

    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# #------------------------------------------------------------
# Add new question  
@questions_replies.route('/add_question', methods=['POST'])
def add_question():

    question_data = request.json

    sID = question_data['sID']
    content = question_data['content']

    query = '''INSERT INTO Question (sID, content)
    VALUES (%s, %s)'''

    current_app.logger.info('Inserting question with ID: %s', sID)

    cursor = db.get_db().cursor()
    cursor.execute(query, (sID, content))
    db.get_db().commit()

    response = make_response("Successfully added new question")
    response.status_code = 200
    return 'question created!'

# #------------------------------------------------------------
# Add new reply  
@questions_replies.route('/add_reply', methods=['POST'])
def add_reply():

    loc_data = request.json

    loc_id = loc_data['locationID']
    city = loc_data['city']
    country = loc_data['country']
    description = loc_data['description']

    query = '''INSERT INTO Location (locationID, city, country, description)
    VALUES (%s, %s, %s, %s)'''

    current_app.logger.info('Inserting location with ID: %s', loc_id)

    cursor = db.get_db().cursor()
    cursor.execute(query, (loc_id, city, country, description))
    db.get_db().commit()

    response = make_response("Successfully added new location")
    response.status_code = 200
    return 'location created!'

#------------------------------------------------------------
# Delete a reply
@questions_replies.route('/delete_reply', methods=['DELETE'])
def delete_reply(reply_id, sID):
    try:
        cursor = db.get_db().cursor()
        query = f'''
            DELETE FROM Reply
            WHERE replyID = {reply_id} AND sID = {sID}
        '''
        cursor.execute(query)
        db.get_db().commit()

        response = make_response("Reply deleted successfully.")
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error deleting reply: {e}")
        response = make_response("Failed to delete reply.", 500)
        return response