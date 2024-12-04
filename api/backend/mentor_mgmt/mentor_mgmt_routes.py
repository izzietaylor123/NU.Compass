from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

mentors = Blueprint('mentors', __name__)

# Get all mentors
@mentors.route('/mentors', methods=['GET'])
def get_all_mentors():
    query = '''
        SELECT sID AS MentorID, 
               CONCAT(fName, ' ', lName) AS Name, 
               email AS Email, 
               'Expertise Placeholder' AS Expertise, 
               'Availability Placeholder' AS Availability
        FROM Student
        WHERE role = 'mentor'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    mentors_data = cursor.fetchall()

    current_app.logger.info(f"Mentor data fetched: {mentors_data}")  # Add this line to log data

    response = make_response(jsonify(mentors_data))
    response.status_code = 200
    return response


# @mentors.route('/mentors', methods=['GET'])
# def get_all_mentors():
#     query = '''
#         SELECT sID AS MentorID, 
#                CONCAT(fName, ' ', lName) AS Name, 
#                email AS Email, 
#                'Expertise Placeholder' AS Expertise, 
#                'Availability Placeholder' AS Availability
#         FROM Student
#         WHERE role = 'mentor'
#     '''
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     mentors_data = cursor.fetchall()

#     response = make_response(jsonify(mentors_data))
#     response.status_code = 200
#     return response

# Add a new mentor
@mentors.route('/mentors', methods=['POST'])
def add_mentor():
    data = request.json
    fName, lName = data['Name'].split(' ', 1)
    email = data['Email']
    role = 'mentor'  # Hardcode role as 'mentor'
    blurb = data.get('Blurb', 'No blurb provided')  # Optional field

    query = f'''
        INSERT INTO Student (fName, lName, email, role, blurb)
        VALUES ('{fName}', '{lName}', '{email}', '{role}', '{blurb}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor added successfully", 201)
    return response

# Update mentor
@mentors.route('/mentors/<mentor_id>', methods=['PUT'])
def update_mentor(mentor_id):
    data = request.json
    updates = []
    if 'Name' in data:
        fName, lName = data['Name'].split(' ', 1)
        updates.append(f"fName = '{fName}'")
        updates.append(f"lName = '{lName}'")
    if 'Email' in data:
        updates.append(f"email = '{data['Email']}'")
    if 'Blurb' in data:
        updates.append(f"blurb = '{data['Blurb']}'")

    if not updates:
        return make_response("No fields provided for update", 400)

    query = f'''
        UPDATE Student
        SET {", ".join(updates)}
        WHERE sID = {mentor_id} AND role = 'mentor'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor updated successfully", 200)
    return response

# Delete a mentor
@mentors.route('/mentors/<mentor_id>', methods=['DELETE'])
def delete_mentor(mentor_id):
    query = f'''
        DELETE FROM Student
        WHERE sID = {mentor_id} AND role = 'mentor'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor deleted successfully", 200)
    return response
