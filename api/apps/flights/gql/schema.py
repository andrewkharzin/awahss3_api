
import strawberry
from asgiref.sync import sync_to_async
from typing import List, Optional
from strawberry_django.optimizer import DjangoOptimizerExtension
from apps.flights.models.flight_model import Flight
from apps.flights.models.project import FlightProject
from .types import FlightType, FlightProjectType



# ... Other code ...
# Define the Query
@strawberry.type
class Query:
    # Query to get all flights
    # @strawberry.field
    # def all_flights(self) -> List[FlightType]:
    #     return Flight.objects.all()
    
    @strawberry.field
    def all_flights(self, airline_iatacode: Optional[str] = None, flight_type: Optional[str] = None, handling_status: Optional[str] = None, date: Optional[str] = None) -> List[FlightType]:
        flights = Flight.objects.all()
        
        if airline_iatacode:
            flights = flights.filter(airline__codeIataAirline=airline_iatacode)
        
        if flight_type:
            flights = flights.filter(flight_type=flight_type)
        
        if date:
            flights = flights.filter(date=date)
        
        if handling_status:
            flights = flights.filter(handling_status=handling_status)

        return flights
    
        
    

    # Query to get all flight projects
    @strawberry.field
    def all_flight_projects(self) -> List[FlightProjectType]:
        return FlightProject.objects.all()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)