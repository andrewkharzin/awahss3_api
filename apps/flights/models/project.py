
from django.db import models
from .flight_model import  CharterFlight
from .document_model import Document
from .file_model import File
from .note_model import Note
from django.utils.crypto import get_random_string
from apps.users.models import User


class FlightProject(models.Model):
    # fprj_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    flight = models.ForeignKey(CharterFlight, on_delete=models.CASCADE, related_name='flight_project')
    documents = models.ManyToManyField(Document, blank=True)
    files = models.ManyToManyField(File, blank=True)
    notes = models.ManyToManyField(Note, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def __str__(self):
        return f"Project ID: {self.flight.flight_number}"
        