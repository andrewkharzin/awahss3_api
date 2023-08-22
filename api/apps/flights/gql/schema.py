
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



@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flight(
        self,
        airline_iatacode: str,
        flight_type: str,
        handling_status: str,
        date: str
    ) -> FlightType:
        flight = Flight.objects.create(
            airline__codeIataAirline=airline_iatacode,
            flight_type=flight_type,
            handling_status=handling_status,
            date=date
        )
        return flight

    @strawberry.mutation
    def update_flight(
        self,
        flight_id: int,
        airline_iatacode: Optional[str] = None,
        flight_type: Optional[str] = None,
        handling_status: Optional[str] = None,
        date: Optional[str] = None
    ) -> FlightType:
        flight = Flight.objects.get(pk=flight_id)

        if airline_iatacode:
            flight.airline__codeIataAirline = airline_iatacode

        if flight_type:
            flight.flight_type = flight_type

        if date:
            flight.date = date

        if handling_status:
            flight.handling_status = handling_status

        flight.save()
        return flight
    
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ],
)