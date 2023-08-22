from django.db import models
from utility.date_format import format_date_template
from apps.directory.airlines.models.airline import Airline, Aircraft

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
    flight_type = models.CharField(max_length=10, choices=FLIGHT_TYPE_CHOICES)
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    flight_route = models.CharField(max_length=3, default="XXX")
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True, blank=True)
    ac_reg_number = models.CharField(max_length=20, null=True, blank=True, default="")
    date = models.DateField()
    time = models.TimeField()
    
    description = models.TextField(blank=True)
    handling_status = models.CharField(max_length=20, choices=HANDLING_STATUS_CHOICES, default='New')
    create_flight_project = models.BooleanField(default=False)
    ldm_telex = models.ForeignKey(LDM, on_delete=models.CASCADE, null=True, blank=True, related_name="flighs")


    def __str__(self):
        return f"{self.airline}{self.flight_number}/{self.get_formatted_date()}-{self.time.strftime('%H:%M')}"

    def get_formatted_date(self):
        return format_date_template(self.date.strftime('%Y-%m-%d'))

