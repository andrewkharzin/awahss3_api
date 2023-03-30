import graphene
from graph import queries
# import api.apps.ibase.gql.schema as imsgcodes 
import api.apps.directory.airlines.gql.schema as airlines
# import api.apps.directory.airports.gql.schema as airports



class Query(airlines.Query):
    pass

schema = graphene.Schema(query=Query)
