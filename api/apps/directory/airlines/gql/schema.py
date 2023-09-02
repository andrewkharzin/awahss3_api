import strawberry
from strawberry import Private
from typing import List, Any, Optional
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

@strawberry.django.type(Airline)
class AircraftType:
    airline: AirlineType
    codeIataAirline: str
    registrationNumber: str
    acCode: str
    model: str
    image: strawberry.Private[str]
    

@strawberry.type
class DirectoryQuery:
    airlines: List[AirlineType] = optimized_django_field()
    # aircrafts: List[AircraftType] = optimized_django_field()
    
    # def allAircrafts(self, info) -> [AircraftType]:
    #     return Aircraft.objects.all()
    # def resolve_all_airlines(self, info) -> List[AirlineType]:
    #     airlines = Airline.objects.all()
    #     request: HttpRequest = info.context

    #     for airline in airlines:
    #         if airline.arl_logo:
    #             airline.arl_logo = request.build_absolute_uri(airline.arl_logo.url)
    #         if airline.cntr_logo:
    #             airline.cntr_logo = request.build_absolute_uri(airline.cntr_logo.url)
    #         if airline.banner_img:
    #             airline.banner_img = request.build_absolute_uri(airline.banner_img.url)

    #     return airlines

schema = strawberry.Schema(
    query=DirectoryQuery,
)