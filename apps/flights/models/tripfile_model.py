from django.db import models
import uuid
from apps.users.models import User
from django.utils import timezone
# from .flight_model import CharterFlight
from apps.flights.models.file_model import File


class TripFile(models.Model):
    
    trip_number = models.CharField(max_length=20, editable=False)
    createAt = models.DateTimeField(auto_created=True)
    updateAt = models.DateTimeField(auto_now_add=True)
    # unique_id = models.CharField(max_length=100, editable=False, unique=True)  # Auto-generated based on your template
    # charter_flight = models.OneToOneField(CharterFlight, on_delete=models.CASCADE)
    # Add other fields specific to TripFile

    def save(self, *args, **kwargs):
        if not self.trip_number:
            # Generate a unique serial number (max length 6) using UUID
            serial_number = str(uuid.uuid4().int)[:6]

            # Format the trip_number using flight_number, createAt, and serial_number
            self.trip_number = f"{self.charter_flight.flight_number}-{self.createAt.strftime('%Y%m%d')}-{serial_number}"

        super().save(*args, **kwargs)


class Msgs(models.Model):
    trip_file = models.ForeignKey(TripFile, on_delete=models.CASCADE)
    # charter_flight = models.ForeignKey(CharterFlight, on_delete=models.CASCADE)
    tracking_date = models.DateField(default=timezone.now)
    tracking_time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Message for Charter Flight {self.charter_flight.flight_number} at {self.tracking_date} {self.tracking_time}"


class Telex(models.Model):
    MESSAGE_TYPES = [
        ('LDM', 'Load Distribution Message'),
        ('CPM', 'Customs Pre-arrival Message'),
        ('FFM', 'Freight Forwarder Message'),
        ('FWB', 'Freight Waybill'),
        ('FFA', 'Freight Arrival Message'),
        ('MVT', 'Movement Message'),
        # Add more message types as needed
    ]

    trip_file = models.ForeignKey(TripFile, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=3, choices=MESSAGE_TYPES)
    tracking_date = models.DateField(default=timezone.now)
    tracking_time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message_content = models.TextField()

    def __str__(self):
        return f"{self.get_message_type_display()} for Trip File {self.trip_file_id} at {self.tracking_date} {self.tracking_time}"


class Event(models.Model):
    EVENT_CHOICES = [
        ("DMG_A", 'Damage of Aircraft'),
        ("DMG_SHP", 'Damage of shipment'),
        ("DMG_QIP", 'Damage of equipment'),
        ("STF_EVN", 'Stuff events'),
        ("NTCLS", 'Not classified')
    ]
    trip_file = models.ForeignKey(TripFile, on_delete=models.CASCADE)
    event_date = models.DateField(default=timezone.now)
    event_time = models.TimeField(default=timezone.now)
    event_type = models.CharField(
        max_length=10, choices=EVENT_CHOICES, default="")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    attachment = models.ManyToManyField('Attachment')

    def __str__(self):
        return f"{self.event_type} for Tripfile {self.trip_file_id} at {self.event_date} {self.event_time}"


class Attachment(models.Model):
    trip_file = models.ForeignKey(TripFile, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
