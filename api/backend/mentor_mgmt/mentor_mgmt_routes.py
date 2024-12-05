from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

mentors = Blueprint('mentors', __name__)

# get all mentors
@mentors.route('/mentors', methods=['GET'])
def get_all_mentors():
    query = '''
        SELECT 
            sID AS sID, 
            fName AS fName, 
            lName AS lName, 
            email AS email, 
            blurb AS blurb
        FROM Student
        WHERE role = 'mentor'
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        mentors_data = cursor.fetchall()

        current_app.logger.info(f"Mentor data fetched: {mentors_data}")

        formatted_data = [
            {
                "sID": row["sID"],
                "fName": row["fName"],
                "lName": row["lName"],
                "email": row["email"],
                "blurb": row.get("blurb", "No blurb provided")
            }
            for row in mentors_data
        ]

        response = make_response(jsonify(formatted_data))
        response.status_code = 200
    except Exception as e:
        current_app.logger.error(f"Error fetching mentors: {e}")
        response = make_response("Error fetching mentors", 500)
    return response

# add a new mentor
@mentors.route('/mentors', methods=['POST'])
def add_mentor():
    data = request.json
    try:
        # extract fields
        name = data.get('Name', '')
        if ' ' not in name:
            return make_response("Invalid name format. Provide both first and last name.", 400)
        fName, lName = name.split(' ', 1)
        email = data['Email']
        blurb = data.get('Blurb', 'No blurb provided')

        query = '''
            INSERT INTO Student (fName, lName, email, role, blurb)
            VALUES (%s, %s, %s, %s, %s)
        '''
        values = (fName, lName, email, 'mentor', blurb)

        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        response = make_response("Mentor added successfully", 201)
    except Exception as e:
        current_app.logger.error(f"Error adding mentor: {e}")
        response = make_response("Error adding mentor", 500)
    return response

# update mentor
@mentors.route('/mentors/<mentor_id>', methods=['PUT'])
def update_mentor(mentor_id):
    data = request.json
    try:
        updates = []
        if 'Name' in data:
            name = data['Name']
            if ' ' not in name:
                return make_response("Invalid name format. Provide both first and last name.", 400)
            fName, lName = name.split(' ', 1)
            updates.append(f"fName = %s")
            updates.append(f"lName = %s")
        if 'Email' in data:
            updates.append(f"email = %s")
        if 'Blurb' in data:
            updates.append(f"blurb = %s")

        if not updates:
            return make_response("No fields provided for update", 400)

        # build the query 
        query = f'''
            UPDATE Student
            SET {", ".join(updates)}
            WHERE sID = %s AND role = 'mentor'
        '''
        values = [data.get('fName'), data.get('lName'), data.get('Email'), data.get('Blurb'), mentor_id]

        cursor = db.get_db().cursor()
        cursor.execute(query, tuple(values))
        db.get_db().commit()

        response = make_response("Mentor updated successfully", 200)
    except Exception as e:
        current_app.logger.error(f"Error updating mentor: {e}")
        response = make_response("Error updating mentor", 500)
    return response

@mentors.route('/mentors/<mentor_id>', methods=['DELETE'])
def delete_mentor(mentor_id):
    try:
        current_app.logger.info(f"Attempting to delete mentor with ID: {mentor_id}")
        
        # SQL query to delete the mentor
        query = f'''
            DELETE FROM Student
            WHERE sID = {mentor_id} AND role = 'mentor'
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Check if a row was deleted
        if cursor.rowcount == 0:
            current_app.logger.info(f"No mentor found with ID {mentor_id}")
            return make_response(f"No mentor found with ID {mentor_id}", 404)

        current_app.logger.info(f"Mentor with ID {mentor_id} deleted successfully")
        return make_response("Mentor deleted successfully", 200)

    except Exception as e:
        current_app.logger.error(f"Error deleting mentor: {e}")
        return make_response(f"An error occurred: {str(e)}", 500)

# get all mentees for a mentor
@mentors.route('/get_mentees/<mentorID>', methods=['GET'])
def get_mentees(mentorID):

    cursor = db.get_db().cursor()
    query = f'''
        SELECT menteeID
        FROM mentorshipMatch
        WHERE mentorID = {str(mentorID)}
    '''
    cursor.execute(query)
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
