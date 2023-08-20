from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.flight_model import Flight
from .models.project import FlightProject
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.db.models.signals import pre_save

@receiver(post_save, sender=Flight)
def create_flight_project(sender, instance, created, **kwargs):
    if created and instance.create_flight_project:
        flight_project = FlightProject.objects.create(flight=instance)
        instance.flight_project = flight_project
        instance.save()

# Signal handler to generate and set the custom ID before saving FlightProject instance
@receiver(pre_save, sender=FlightProject)
def set_flight_project_fprj_id(sender, instance, **kwargs):
    if not instance.fprj_id:
        flight_number = instance.flight.flight_number
        date_str = instance.flight.date.strftime('%y%m%d')
        serial_number = get_random_string(length=8, allowed_chars='1234567890')
        instance.fprj_id = f"{flight_number}|{date_str}-{serial_number}"