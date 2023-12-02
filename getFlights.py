from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load flights data from JSON file
with open('flights.json') as f:
    flights_data = json.load(f)

@app.route('/getAvailableFlights', methods=['GET'])
def get_available_flights():
    return jsonify({'flights': flights_data['flights']})

@app.route('/<flightNumber>', methods=['GET'])
def get_flight_details(flightNumber):
    # Return information for the specific flight if it exists
    selected_flight = next((flight for flight in flights_data['flights'] if flight['flightNumber'] == flightNumber), None)

    if selected_flight:
        return jsonify({'flight': selected_flight})
    else:
        return jsonify({'error': 'Flight not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
