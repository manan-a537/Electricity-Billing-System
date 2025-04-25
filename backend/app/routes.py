from flask import Blueprint, jsonify, request
from .services import ElectricityManagementSystem

api = Blueprint('api', __name__)
ems = ElectricityManagementSystem()

@api.route('/readings', methods=['POST'])
def add_reading():
    data = request.json
    reading = Reading(
        timestamp=datetime.fromisoformat(data['timestamp']),
        consumption=float(data['consumption']),
        peak_demand=float(data['peak_demand'])
    )
    ems.add_reading(reading)
    return jsonify({'message': 'Reading added successfully'}), 201

@api.route('/bills/<int:year>/<int:month>', methods=['GET'])
def get_bill(year, month):
    bill = ems.generate_bill(month, year)
    return jsonify(bill.__dict__)

@api.route('/consumption/history', methods=['GET'])
def get_consumption_history():
    months = request.args.get('months', 6, type=int)
    history = ems.get_consumption_history(months)
    return jsonify(history)

@api.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = ems.get_usage_alerts()
    return jsonify(alerts)