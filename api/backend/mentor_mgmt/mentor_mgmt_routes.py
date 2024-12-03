from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

mentors = Blueprint('mentors', __name__)

# get all mentors
@mentors.route('/mentors', methods=['GET'])
def get_all_mentors():
    query = '''
        SELECT MentorID, Name, Email, Expertise, Availability
        FROM mentors
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    mentors_data = cursor.fetchall()

    response = make_response(jsonify(mentors_data))
    response.status_code = 200
    return response

# add a new mentor
@mentors.route('/mentors', methods=['POST'])
def add_mentor():
    data = request.json
    name = data['Name']
    email = data['Email']
    expertise = data['Expertise']
    availability = data['Availability']

    query = f'''
        INSERT INTO mentors (Name, Email, Expertise, Availability)
        VALUES ('{name}', '{email}', '{expertise}', '{availability}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor added successfully", 201)
    return response

# update mentor
@mentors.route('/mentors/<mentor_id>', methods=['PUT'])
def update_mentor(mentor_id):
    data = request.json
    updates = []
    if 'Name' in data:
        updates.append(f"Name = '{data['Name']}'")
    if 'Email' in data:
        updates.append(f"Email = '{data['Email']}'")
    if 'Expertise' in data:
        updates.append(f"Expertise = '{data['Expertise']}'")
    if 'Availability' in data:
        updates.append(f"Availability = '{data['Availability']}'")

    if not updates:
        return make_response("No fields provided for update", 400)

    query = f'''
        UPDATE mentors
        SET {", ".join(updates)}
        WHERE MentorID = {mentor_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor updated successfully", 200)
    return response

# delete a mentor
@mentors.route('/mentors/<mentor_id>', methods=['DELETE'])
def delete_mentor(mentor_id):
    query = f'''
        DELETE FROM mentors
        WHERE MentorID = {mentor_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Mentor deleted successfully", 200)
    return response
