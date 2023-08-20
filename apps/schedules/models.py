from django.db import models

class Schedule(models.Model):
    flight_date = models.DateField()
    flight_status = models.CharField(max_length=20)
    departure_airport = models.CharField(max_length=100)
    departure_timezone = models.CharField(max_length=100)
    departure_iata = models.CharField(max_length=3)
    departure_icao = models.CharField(max_length=4)
    departure_terminal = models.CharField(max_length=10)
    departure_gate = models.CharField(max_length=10)
    departure_delay = models.IntegerField()
    departure_scheduled = models.DateTimeField()
    departure_estimated = models.DateTimeField()
    departure_actual = models.DateTimeField()
    departure_estimated_runway = models.DateTimeField()
    departure_actual_runway = models.DateTimeField()
    arrival_airport = models.CharField(max_length=100)
    arrival_timezone = models.CharField(max_length=100)
    arrival_iata = models.CharField(max_length=3)
    arrival_icao = models.CharField(max_length=4)
    arrival_terminal = models.CharField(max_length=10)
    arrival_gate = models.CharField(max_length=10)
    arrival_baggage = models.CharField(max_length=10)
    arrival_delay = models.IntegerField()
    arrival_scheduled = models.DateTimeField()
    arrival_estimated = models.DateTimeField()
    arrival_actual = models.DateTimeField()
    arrival_estimated_runway = models.DateTimeField()
    arrival_actual_runway = models.DateTimeField()
    airline_name = models.CharField(max_length=100)
    airline_iata = models.CharField(max_length=2)
    airline_icao = models.CharField(max_length=3)
    flight_number = models.CharField(max_length=10)
    flight_iata = models.CharField(max_length=10)
    flight_icao = models.CharField(max_length=10)
    aircraft_registration = models.CharField(max_length=10)
    aircraft_iata = models.CharField(max_length=10)
    aircraft_icao = models.CharField(max_length=10)
    aircraft_icao24 = models.CharField(max_length=10)
    live_updated = models.DateTimeField()
    live_latitude = models.FloatField()
    live_longitude = models.FloatField()
    live_altitude = models.FloatField()
    live_direction = models.FloatField()
    live_speed_horizontal = models.FloatField()
    live_speed_vertical = models.FloatField()
    live_is_ground = models.BooleanField()

    def __str__(self):
        return f"Flight {self.flight_number} - {self.departure_iata} to {self.arrival_iata}"
