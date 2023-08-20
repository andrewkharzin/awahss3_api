from django.shortcuts import render
from .utils import get_in_air_flights

def in_air_flights_view(request):
    in_air_flights = get_in_air_flights()

    context = {
        'in_air_flights': in_air_flights
    }

    return render(request, 'flights/in_air_flights.html', context)

# views.py

import requests
from django.shortcuts import render
from .models import Schedule
from datetime import datetime
from .models import Schedule

def map_flight_data_to_schedule(flight_data):
    departure = flight_data['departure']
    arrival = flight_data['arrival']
    airline = flight_data['airline']
    flight = flight_data['flight']

    return {
        'flight_date': flight_data['flight_date'],
        'flight_status': flight_data['flight_status'],
        'departure_airport': departure['airport'],
        'departure_timezone': departure['timezone'],
        'departure_iata': departure['iata'],
        'departure_icao': departure['icao'],
        'departure_terminal': departure['terminal'],
        'departure_gate': departure['gate'],
        'departure_delay': departure['delay'],
        'departure_scheduled': departure['scheduled'],
        'departure_estimated': departure['estimated'],
        'departure_actual': departure['actual'],
        'departure_estimated_runway': departure['estimated_runway'],
        'departure_actual_runway': departure['actual_runway'],
        'arrival_airport': arrival['airport'],
        'arrival_timezone': arrival['timezone'],
        'arrival_iata': arrival['iata'],
        'arrival_icao': arrival['icao'],
        'arrival_terminal': arrival['terminal'],
        'arrival_gate': arrival['gate'],
        'arrival_baggage': arrival['baggage'],
        'arrival_delay': arrival['delay'],
        'arrival_scheduled': arrival['scheduled'],
        'arrival_estimated': arrival['estimated'],
        'arrival_actual': arrival['actual'],
        'arrival_estimated_runway': arrival['estimated_runway'],
        'arrival_actual_runway': arrival['actual_runway'],
        'airline_name': airline['name'],
        'airline_iata': airline['iata'],
        'airline_icao': airline['icao'],
        'flight_number': flight['number'],
        'flight_iata': flight['iata'],
        'flight_icao': flight['icao'],
    }



def load_flight_data(request):
    access_key = '7c8a729991b6fefbfd9e89863279c947'
    arr_iata = 'SVO'
    api_url = f'http://api.aviationstack.com/v1/flights?access_key={access_key}&arr_iata={arr_iata}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        flights = data.get('data', [])
        
        context = {
            'flights': flights
        }
        return render(request, 'flights/flight_list.html', context)

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching flight data: {e}"
        return render(request, 'flights/error.html', {'error_message': error_message})
