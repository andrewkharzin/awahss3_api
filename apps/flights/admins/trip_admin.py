from django.contrib import admin
from apps.flights.models.flight_model import CharterFlight
from apps.flights.models.tripfile_model import TripFile, Msgs, Telex, Event, Attachment


class AttchInline(admin.StackedInline):
    model = Attachment
    extra = 1
    classes = ['collapse']

class EventInline(admin.StackedInline):
    model = Event
    extra =1
    classes = ['collapse']

class MsgStoreInline(admin.StackedInline):
    model = Msgs
    extra = 1
    classes = ['collapse']

class TelexInline(admin.TabularInline):
    model = Telex
    extra = 1
    classes = ['collapse']

class TripFileAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [MsgStoreInline, TelexInline, EventInline, AttchInline]


