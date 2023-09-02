import graphene
from graphene_django.types import DjangoObjectType
from apps.flights.models.project import FlightProject
from .types import FlightProjectType

class FlightType(DjangoObjectType):
    class Meta:
        model = FlightProject

class Query(graphene.ObjectType):
    flights = graphene.List(
        FlightType,
        state_status=graphene.String(),
        airline_iatacode=graphene.String(),
        hand_status=graphene.String(),
        trip_status=graphene.String(),
    )


schema = graphene.Schema(query=Query)
