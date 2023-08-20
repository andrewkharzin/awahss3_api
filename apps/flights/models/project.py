
from django.db import models
from .flight_model import  Flight
from .document_model import Document
from .file_model import File
from .note_model import Note
from django.utils.crypto import get_random_string
from apps.users.models import User


class FlightProject(models.Model):
    fprj_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='flight_project')
    documents = models.ManyToManyField(Document, blank=True)
    files = models.ManyToManyField(File, blank=True)
    notes = models.ManyToManyField(Note, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    
    # def generate_project_id(self):
    #     flight_number = self.flight.flight_number
    #     date_str = self.flight.date.strftime('%y%m%d')
    #     serial_number = get_random_string(length=8, allowed_chars='1234567890')

    #     return f"{flight_number}|{date_str}-{serial_number}"

    # def save(self, *args, **kwargs):
    #     # Set the ID before saving
    #     if not self.pk:
    #         self.id = self.generate_project_id()
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f"Project ID: {self.fprj_id}"
        