import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from apps.directory.models.airports import Airport

class AirportFilter(FilterSet):
    class Meta:
        model = Airport
        fields = [
            'codeIataAirport',
            'codeIcaoAirport',
            'codeIataCity',
            'codeIso2Country',
        ]
        filter_fields = {
            'codeIataAirport': ['exact', 'icontains'],
            'codeIcaoAirport': ['exact', 'icontains'],
            'codeIataCity': ['exact', 'icontains'],
            'codeIso2Country': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )


  
class AirportType(DjangoObjectType):
    # def resolve_arl_logo(self, info):
    #     """Resolve product image absolute path"""
    #     if self.arl_logo:
    #         self.arl_logo = info.context.build_absolute_uri(self.arl_logo.url)
    #     return self.arl_logo
    class Meta:
        model = Airport
        interfaces = (graphene.relay.Node,)
        filterset_class = AirportFilter
        fields = '__all__'


class Query(graphene.ObjectType):
    airports = DjangoFilterConnectionField(AirportType)
    airports_count = graphene.Int()
    airport = graphene.Field(AirportType, id=graphene.Int())

    def resolve_airports_count(self, info):
        return Airport.objects.count()
    
    def resolve_airport(root, info, id):
        return Airport.objects.get(id=id)
       


schema = graphene.Schema(query=Query)