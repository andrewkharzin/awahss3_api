import strawberry
from strawberry import auto
from typing import List, Optional
from apps.flights.models.flight_model import Flight
from apps.flights.models.project import FlightProject
from api.apps.directory.airlines.gql.schema import AirlineType


@strawberry.django.type(Flight)
class FlightType:
    flight_number: str
    airline: AirlineType
    date: str
    time: str
    flight_type: str
    handling_status: str
    flight_route: str
    eta_time: str
    etd_time: str
    flight_project: Optional["FlightProjectType"]  # Note the quotes here

# Define the FlightProject model type
@strawberry.django.type(FlightProject)
class FlightProjectType:
    fprj_id: str
    flight: FlightType
    # Add other fields for FlightProject as needed
