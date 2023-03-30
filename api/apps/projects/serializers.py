from django.urls import path, include
from apps.projects.models.flight_project import FlightProject
from apps.projects.models.flight import Flight
from apps.directory.models.airline import Airline
from apps.directory.models.register import Register
from apps.directory.models.airports import Airport
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class FlightProjectSerializer(serializers.HyperlinkedModelSerializer):
    # airline = serializers.StringRelatedField(many=False)
    # registration = serializers.StringRelatedField(many=False)
    # route = serializers.StringRelatedField(many=False)
    class Meta:
        model = FlightProject
        fields = "__all__"

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'number',
            'ac_type',
            'co',
            'mod',
            'g_type',
            'description'

        )
        model = Register

class AirlineSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)
    class Meta:
        fields = (
            'iata',
            'icao',
            'rus_code',
            'comment_eng',
            'comment_rus',
            'country',
            'alliance',
            'lowcost',
            'description',
            'logo',

        )    

        model = Airline

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'iata',
            'icao',
           
        )    

        model = Airport

