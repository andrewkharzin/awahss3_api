import strawberry

from api.apps.flights.gql.schema import schema as flight_schema
from api.apps.directory.airlines.gql.schema import schema as directory_schema

# Combine types from schema1 and schema2
combined_types = [directory_schema.query, flight_schema.query]

# Define a root query that includes all queries from schema1 and schema2
@strawberry.type
class RootQuery:
    # Include queries from schema1
    query1: directory_schema.query

    # Include queries from schema2
    query2: flight_schema.query

# Combine the schemas into one root schema
root_schema = strawberry.Schema(query=RootQuery, types=combined_types)
