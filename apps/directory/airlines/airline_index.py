from elasticsearch_dsl import Document, Integer, Text


class AirlineIndex(Document):
    codeIataAirline = Text()

    class Index:
        name = 'airline_index'
