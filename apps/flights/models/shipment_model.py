from django.db import models
import json
from datetime import timezone
from apps.flights.utils.ffm_tomodel import parse_message
from apps.flights.models.flight_model import CharterFlight

class ShipmentFlight(models.Model):
    flight = models.ForeignKey(CharterFlight, on_delete=models.CASCADE)


class ULD(models.Model):
    uld_number = models.CharField(max_length=20)
    # Add other ULD-related fields here

    def __str__(self):
        return self.uld_number

class Shipment(models.Model):
    version = models.CharField(max_length=10, null=True, blank=True)
    awb = models.CharField(max_length=20, null=True, blank=True)
    flight_number = models.CharField(max_length=10, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    iata = models.CharField(max_length=10, null=True, blank=True)
    registration_number = models.CharField(
        max_length=10, null=True, blank=True)
    route_from = models.CharField(max_length=10, null=True, blank=True)
    route_to = models.CharField(max_length=10, null=True, blank=True)
    pieces_type = models.CharField(max_length=3, null=True, blank=True)
    pieces = models.IntegerField(null=True, blank=True)
    kilos = models.IntegerField(null=True, blank=True)
    cubic_meter = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    last_pics = models.IntegerField(null=True, blank=True)
    goods = models.CharField(max_length=100, null=True, blank=True)
    special_handling_code = models.CharField(
        max_length=10, null=True, blank=True)

    uld = models.ForeignKey(ULD, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Shipment {self.uld} - {self.awb}"