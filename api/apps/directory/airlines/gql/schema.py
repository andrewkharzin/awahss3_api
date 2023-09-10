import strawberry
from strawberry import Private
from typing import List, Any, Optional
from strawberry.types import Info
import graphene
from asgiref.sync import sync_to_async
from django.templatetags.static import static
from django.conf import settings
from graphene_django import DjangoObjectType
# from strawberry import Schema, Query as StrawberryQuery
from django.http import HttpRequest
# from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry_django_optimizer import optimized_django_field
from apps.directory.airlines.models.airline import Airline, Aircraft
from apps.directory.airlines.elasticsearch_helpers import search_airlines
optimized_django_field


@strawberry.django.type(Airline)
class AirlineType:
    ageFleet: int
    founding: int
    sizeAirline: int
    statusAirline: str
    iataPrefixAccounting: Optional[int]
    callsign: str
    codeHub: str
    codeIso2Country: str
    codeIataAirline: str
    codeIcaoAirline: str
    nameAirline: str
    nameCountry: str
    type: str
    arl_logo: strawberry.Private[str]
    cntr_logo: strawberry.Private[str]
    # arl_logo: str
    # cntr_logo: str
    banner_img: str

    @strawberry.field
    async def resolved_arl_logo(self, info) -> str:
        return await resolve_arl_logo(self, info)

    @strawberry.field
    async def resolved_cntr_logo(self, info) -> str:
        return await resolve_cntr_logo(self, info)


@sync_to_async
def resolve_arl_logo(parent, info):
    if parent.arl_logo:
        return parent.arl_logo.url if settings.DEBUG else parent.arl_logo.url.lstrip(settings.STATIC_URL)
    return ""


@sync_to_async
def resolve_cntr_logo(parent, info):
    if parent.cntr_logo:
        return parent.cntr_logo.url if settings.DEBUG else parent.cntr_logo.url.lstrip(settings.STATIC_URL)
    return ""


@strawberry.django.type(Aircraft)
class AircraftType:
    airline: AirlineType
    codeIataAirline: Optional[str]
    registrationNumber: Optional[str]
    acCode: Optional[str]
    model: Optional[str]
    image: strawberry.Private[str]

    @strawberry.field
    async def resolved_image(self, info) -> str:
        return await resolve_image(self, info)


@sync_to_async
def resolve_image(parent, info):
    if parent.image:
        return parent.image.url if settings.DEBUG else parent.image.url.lstrip(settings.STATIC_URL)
    return ""


@strawberry.type
class Query:
    airlines: List[AirlineType] = optimized_django_field()
    # aircrafts: List[AircraftType] = optimized_django_field()

    @strawberry.field(description="Fetch a list of aircrafts.")
    async def resolve_aircrafts(
        self,
        info: Info,
        airlineCode: Optional[str] = None,
        page: int = 1,
        perPage: int = 10
    ) -> List[AircraftType]:
        try:
            # Wrap the database query inside sync_to_async
            queryset = await sync_to_async(Aircraft.objects.all)()

            if airlineCode:
                queryset = await sync_to_async(queryset.filter)(codeIataAirline=airlineCode)

            start = (page - 1) * perPage
            end = start + perPage

            # Fetch the paginated list of aircrafts asynchronously
            aircraft_records = await sync_to_async(list)(queryset[start:end].values())

            # Convert the aircraft records to AircraftType objects
            aircrafts = [AircraftType(
                airline=AirlineType(
                    codeIataAirline=record['codeIataAirline']
                ),
                codeIataAirline=record['codeIataAirline'],
                registrationNumber=record['registrationNumber'],

            ) for record in aircraft_records]

            return aircrafts
        except Aircraft.DoesNotExist:
            return []


schema = strawberry.Schema(
    query=Query,
)
