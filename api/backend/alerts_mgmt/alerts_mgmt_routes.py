from flask import Blueprint
from flask import request, jsonify, make_response, current_app
from backend.db_connection import db

alerts = Blueprint('alerts', __name__)

# get all alerts
@alerts.route('/alerts', methods=['GET'])
def get_all_alerts():
    query = '''
        SELECT alertID, locationID, message, datePosted
        FROM Alerts
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    alerts_data = cursor.fetchall()

    response = make_response(jsonify(alerts_data))
    response.status_code = 200
    return response

# add a new alert
@alerts.route('/alerts', methods=['POST'])
def add_alert():
    data = request.json
    location_id = data['locationID']
    message = data['message']

    query = f'''
        INSERT INTO Alerts (locationID, message, datePosted)
        VALUES ({location_id}, '{message}', NOW())
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Alert added successfully", 201)
    return response

# update an alert
@alerts.route('/alerts/<alert_id>', methods=['PUT'])
def update_alert(alert_id):
    data = request.json
    updates = []
    if 'message' in data:
        updates.append(f"message = '{data['message']}'")

    if not updates:
        return make_response("No fields provided for update", 400)

    query = f'''
        UPDATE Alerts
        SET {", ".join(updates)}
        WHERE alertID = {alert_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Alert updated successfully", 200)
    return response

# delete an alert
@alerts.route('/alerts/<alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    query = f'''
        DELETE FROM Alerts
        WHERE alertID = {alert_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Alert deleted successfully", 200)
    return response
