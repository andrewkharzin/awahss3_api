from django.db import models
import uuid
from apps.users.models import User
from django.utils import timezone
# from .flight_model import CharterFlight
from apps.flights.models.file_model import File
from apps.flights.models.flight_model import CharterFlight


class TripFile(models.Model):
    charter_flight = models.ForeignKey(
        CharterFlight,
        on_delete=models.CASCADE,  # Adjust the on_delete behavior as needed
        related_name='tripfile',
        blank=True,
        null=True  # You can customize the related_name
    )

    trip_number = models.CharField(max_length=100, unique=True, editable=False)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.trip_number:
            # Generate a unique serial number (max length 6) using UUID
            serial_number = str(uuid.uuid4().int)[:6]

            # Format the trip_number using flight_number, createAt, and serial_number
            self.trip_number = f"{self.charter_flight.flight_number}-{serial_number}"

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
