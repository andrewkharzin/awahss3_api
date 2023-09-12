
import strawberry
from asgiref.sync import sync_to_async
from typing import List, Optional
from django.db.models import QuerySet
from strawberry_django_optimizer import optimized_django_field
from apps.flights.models.flight_model import CharterFlight
from apps.flights.models.tripfile_model import TripFile
from apps.flights.models.project import FlightProject
from .types import CharterFlightType, TripFileType


@strawberry.type
class Query:

    @strawberry.field
    async def flights(
        self,
        airline_iatacode: Optional[str] = None,
        state_status: Optional[str] = None,
        hand_status: Optional[str] = None,
        trip_status: Optional[str] = None
    ) -> List[CharterFlightType]:
        # Wrap the database query in sync_to_async
        queryset = CharterFlight.objects.all()
        # queryset = FlightProject.objects.all()

        if airline_iatacode:
            queryset = queryset.filter(
                airline__codeIataAirline=airline_iatacode)

        if state_status:
            queryset = queryset.filter(state_status=state_status)
        if hand_status:
            queryset = queryset.filter(hand_status=hand_status)
        if trip_status:
            queryset = queryset.filter(trip_status=trip_status)

        # Use await to execute the query asynchronously
        flights = await sync_to_async(list)(queryset)

        return flights
    
    @strawberry.field
    async def tripfiles(
        self,
        flight_number: Optional[str] = None,
        # Add more filters as needed
    ) -> List[TripFileType]:
        # Wrap the database query in sync_to_async
        queryset = TripFile.objects.all()

        if flight_number:
            queryset = queryset.filter(charter_flight__flight_number=flight_number)

        # Use await to execute the query asynchronously
        tripfiles = await sync_to_async(list)(queryset)

        return tripfiles

    # Query to get all flight projects

    # @strawberry.field
    # def all_flight_projects(self) -> List[FlightProjectType]:
    #     return FlightProject.objects.all()


schema = strawberry.Schema(
    query=Query,
)
