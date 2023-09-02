import graphene
# import api.apps.ibase.gql.schema as imsgcodes 
import api.apps.directory.airlines.gql.schema_graphen as airlines
import api.apps.flights.gql.schema_graphene as flights
# import api.apps.directory.airports.gql.schema as airports
import api.apps.flights.gql.flight_schema as tripfile



class Query(airlines.Query, tripfile.Query, flights.Query):
    pass

schema = graphene.Schema(query=Query)