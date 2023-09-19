from strawberry import Schema
from strawberry.tools import merge_types
from api.apps.directory.airlines.gql.schema import Query as QueryA
from api.apps.directory.aviastates.shc.schema import Query as SHCQuery
from api.apps.directory.aviastates.dgr.schema import Query as DGClassesQuery
from api.apps.flights.gql.schema import Query as QueryB

# Add your query types to the query tuple
queries = (QueryB, SHCQuery, DGClassesQuery, QueryA)

# Add your mutation types to the mutation tuple
# mutations = (MutationB, MutationA)

# Do not touch these
Query = merge_types("Query", queries)
# Mutation = merge_types("Mutation", mutations)
schema = Schema(query=Query)
