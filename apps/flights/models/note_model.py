from django.db import models
from .flight_model import CharterFlight



class Note(models.Model):
    flight = models.ForeignKey(CharterFlight, on_delete=models.CASCADE)
    text = models.TextField()
    flight_project = models.ForeignKey('FlightProject', on_delete=models.CASCADE) 

    def __str__(self):
        return f"Note for {self.flight}"