from django.db import models
from .flight_model import CharterFlight

def file_upload_to(instance, filename):
    return f'flights/{instance.flight.flight_number}{instance.flight.date.strftime("%Y-%m-%d")}/files/{filename}'

class File(models.Model):
    flight = models.ForeignKey(CharterFlight, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=file_upload_to)
    flight_project = models.ForeignKey('FlightProject', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.flight}"
