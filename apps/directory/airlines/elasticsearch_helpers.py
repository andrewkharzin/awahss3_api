# elasticsearch_helpers.py
from elasticsearch_dsl import Search
from .airline_index import AirlineIndex  # Import your AirlineIndex class


def search_airlines(query):
    s = Search(using='default').index(AirlineIndex._doc_type.index)
    s = s.query('multi_match', query=query, fields=['codeIataAirline'])
    response = s.execute()

    # Assuming you want to return the Elasticsearch results as is
    return response

# You may add more functions or customize the search as needed
