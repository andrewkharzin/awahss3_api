import requests

def get_in_air_flights():
    params = {
        'access_key': '7c8a729991b6fefbfd9e89863279c947'
    }

    api_result = requests.get('http://api.aviationstack.com/v1/flights', params=params)
    api_response = api_result.json()

    in_air_flights = []

    for flight in api_response['data']:
        if not flight['live']['is_ground']:
            flight_info = {
                'airline': flight['airline']['name'],
                'flight_iata': flight['flight']['iata'],
                'departure_airport': flight['departure']['airport'],
                'departure_iata': flight['departure']['iata'],
                'arrival_airport': flight['arrival']['airport'],
                'arrival_iata': flight['arrival']['iata']
            }
            in_air_flights.append(flight_info)

    return in_air_flights
