import strawberry
from strawberry import auto
from typing import List, Optional
from apps.flights.models.flight_model import CharterFlight
from apps.directory.airlines.models.airline import Airline, Aircraft
from apps.flights.models.project import FlightProject
from api.apps.directory.airlines.gql.schema import AirlineType, AircraftType


@strawberry.django.type(CharterFlight)
class CharterFlightType:
    airline: AirlineType
    aircraft: AircraftType
    flight_number: str
    flight_date: Optional[str] 
    flight_time: Optional[str] 
    aircraft_type: Optional[str] 
    registration_number: Optional[str]
    flight_route: Optional[str] 
    iata: Optional[str] 
    icao: Optional[str] 
    action_code: Optional[str] 
    slot_msg: Optional[str]
    state_status: str
    hand_status: str
    trip_status: str # Note the quotes here

# Define the FlightProject model type
@strawberry.django.type(FlightProject)
class FlightProjectType:
    flight: CharterFlightType
    # Add other fields for FlightProject as needed
