from django.db import models
import logging
from apps.flights.utils.msg_text import parse_ldm_text
from utility.date_format import format_date_template
from apps.directory.airlines.models.airline import Airline, Aircraft

logger = logging.getLogger(__name__)

class LDM(models.Model):
    text = models.TextField()
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='ldm_telexes')

class Flight(models.Model):
    FLIGHT_TYPE_CHOICES = [
        ('arrival', 'Arrival'),
        ('departure', 'Departure'),
    ]

    HANDLING_STATUS_CHOICES = [
        ('New', 'New'),
        ('StandBy', 'StandBy'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
        ('Canceled', 'Canceled'),
    ]
    flight_type = models.CharField(max_length=10, choices=FLIGHT_TYPE_CHOICES, default="")
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    flight_route = models.CharField(max_length=3, null=True, blank=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True, blank=True)
    ac_reg_number = models.CharField(max_length=20, null=True, blank=True, default="")
    date_time = models.DateTimeField(null=True, blank=True)
    
    
    description = models.TextField(blank=True)
    handling_status = models.CharField(max_length=20, choices=HANDLING_STATUS_CHOICES, default='New')
    create_flight_project = models.BooleanField(default=False)
    ldm_telex = models.ForeignKey(LDM, on_delete=models.CASCADE, null=True, blank=True, related_name="flighs")


    def __str__(self):
        return f"{self.airline}{self.flight_number}/{self.get_formatted_date()}"

    def get_formatted_date(self):
        if self.date_time:
            return self.date_time.strftime('%Y-%m-%d %H:%M')
        return ""

class CharterFlight(models.Model):
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    flight_data_time = models.DateTimeField(null=True, blank=True)
    aircraft_type = models.CharField(max_length=50, null=True, blank=True)
    registration_number = models.CharField(max_length=20, null=True, blank=True)
    flight_route = models.CharField(max_length=100, null=True, blank=True)
    iata = models.CharField(max_length=3, blank=True)
    icao = models.CharField(max_length=4, blank=True)
    action_code = models.CharField(max_length=15, blank=True)
    message_code = models.TextField(default="")
    slot_msg = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Charter Flight {self.flight_number}"

    def save_parsed_flights(self):
        parsed_flights = parse_ldm_text(self.message_code)
        
        for parsed_flight in parsed_flights:
            flight_number = parsed_flight.get('flight_number', '')
            aircraft_type = parsed_flight.get('aircraft_type', '')
            registration_number = parsed_flight.get('registration_number', '')
            flight_route = parsed_flight.get('flight_route', '')
            departure_iata = parsed_flight.get('departure_iata', '')
            arrival_iata = parsed_flight.get('arrival_iata', '')
            action_code = parsed_flight.get('action_code', '')
            
            try:
                charter_flight = CharterFlight.objects.create(
                    flight_number=flight_number,
                    aircraft_type=aircraft_type,
                    registration_number=registration_number,
                    flight_route=flight_route,
                    departure_iata=departure_iata,
                    arrival_iata=arrival_iata,
                    message_code=self.message_code,
                    action_code=action_code
                )
                logger.info("Saved CharterFlight: %s", charter_flight)
            except Exception as e:
                logger.error("Error while saving CharterFlight: %s", e)
                # Обработка ошибки (если требуется)
