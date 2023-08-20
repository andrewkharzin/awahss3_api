import graphene
from graphene_django.types import DjangoObjectType
from apps.flights.models.flight_model import Flight
from apps.flights.models.project import FlightProject
from .types import FlightProjectType

class FlightType(DjangoObjectType):
    class Meta:
        model = Flight

class Query(graphene.ObjectType):
    all_flights = graphene.List(
        FlightType,
        airline_iatacode=graphene.String(),
        flight_type=graphene.String(),
        handling_status=graphene.String(),
        date=graphene.String()
    )


schema = graphene.Schema(query=Query)