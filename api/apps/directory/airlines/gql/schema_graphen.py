from django.db.models import Count
import graphene
from django_filters import FilterSet
from graphene import ObjectType, List, String, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from apps.directory.airlines.models.airline import Airline

class AirlineFilter(FilterSet):
    class Meta:
        model = Airline
        fields = [
            'codeIataAirline',
            'codeIcaoAirline',
            'iataPrefixAccounting',
        ]
        filter_fields = {
            'codeIataAirline': ['exact', 'icontains'],
            'codeIcaoAirline': ['exact', 'icontains'],
            'iataPrefixAccounting': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )


  
class AirlineType(DjangoObjectType):
    def resolve_arl_logo(self, info):
        """Resolve product image absolute path"""
        if self.arl_logo:
            self.arl_logo = info.context.build_absolute_uri(self.arl_logo.url)
        return self.arl_logo
    def resolve_cntr_logo(self, info):
        """Resolve product image absolute path"""
        if self.cntr_logo:
            self.cntr_logo = info.context.build_absolute_uri(self.cntr_logo.url)
        return self.cntr_logo
    class Meta:
        model = Airline
        interfaces = (graphene.relay.Node,)
        filterset_class = AirlineFilter
        fields = '__all__'

class StatusAirlineType(ObjectType):
    value = String()
    count = Int()

class Query(graphene.ObjectType):
    airlines = DjangoFilterConnectionField(AirlineType)
    airlines_count = graphene.Int()
    airlines_status = List(AirlineType, statusAirline=String())
    airlines_status_counts = List(Int)
    airlines_status_list = List(AirlineType)

    airlines_active_count = Int()
    airlines_historical_count = Int()

    def resolve_airlines_count(self, info):
      return Airline.objects.count()
    
    def resolve_airlines_status(self, info, statusAirline=None):
        qs = Airline.objects.all()
        if type:
            qs = qs.filter(statusAirline=statusAirline)
        return qs
    
    def resolve_airlines_active_count(self, info):
        return Airline.objects.filter(statusAirline='active').count()

    def resolve_airlines_historical_count(self, info):
        return Airline.objects.filter(statusAirline='historical').count()


schema = graphene.Schema(query=Query)