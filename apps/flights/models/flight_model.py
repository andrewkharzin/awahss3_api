from django.db import models
import logging
from apps.flights.utils.vda_parser_bb import parse_msg_slot
from utility.date_format import format_date_template
from apps.directory.airlines.models.airline import Airline, Aircraft

logger = logging.getLogger(__name__)


class CharterFlight(models.Model):
    STATE_STATUS_CHOICES = [
            ('New', 'New'),
            ('StandBy', 'StandBy'),
            ('Completed', 'Completed'),
            ('Rejected', 'Rejected'),
            ('Canceled', 'Canceled'),
    ]
    RAMP_HANDLING_STATUS_CHOICES = [
            ('New', 'New'),
            ('Accepted', 'Accepted'),
            ('OnObserve', 'OnObserve'),
            ('OnRamp', 'OnRamp'),
            ('GroundCompleted', 'GroundCompleted')
    ]
    TRIP_STATUS_CHOICES = [
            ('Opened', 'Opened'),
            ('Angaged', 'Angaged'),
            ('Closed', 'Closed')
    ]
    
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True, blank=True)
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    flight_date = models.DateField(null=True, blank=True)
    flight_time = models.TimeField(null=True, blank=True)
    # flight_data_time = models.CharField(max_length=20, null=True, blank=True)
    aircraft_type = models.CharField(max_length=50, null=True, blank=True)
    registration_number = models.CharField(max_length=20, null=True, blank=True)
    flight_route = models.CharField(max_length=100, null=True, blank=True)
    iata = models.CharField(max_length=3, blank=True)
    icao = models.CharField(max_length=4, blank=True)
    action_code = models.CharField(max_length=15, blank=True)
    message_code = models.TextField(default="", null=True, blank=True)
    slot_msg = models.CharField(max_length=100, null=True, blank=True)
    state_status = models.CharField(max_length=20, choices=STATE_STATUS_CHOICES, default='New')
    hand_status = models.CharField(max_length=20, choices=RAMP_HANDLING_STATUS_CHOICES, default='New')
    trip_status = models.CharField(max_length=20, choices=TRIP_STATUS_CHOICES, default='Opened')

    def __str__(self):
        return f"{self.flight_number}-{self.registration_number}"
