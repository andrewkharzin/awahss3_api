import graphene
from graph import queries
# import api.apps.ibase.gql.schema as imsgcodes 
import api.apps.directory.airlines.gql.schema_graphen as airlines
import api.apps.flights.gql.schema_graphene as flights
# import api.apps.directory.airports.gql.schema as airports



class Query(airlines.Query):
    pass

schema = graphene.Schema(query=Query)