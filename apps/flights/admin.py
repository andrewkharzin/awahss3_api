from django.contrib import admin
from django.utils import timezone
from django.forms.models import inlineformset_factory
import datetime
from apps.directory.airlines.models.airline import Airline
from .models.file_model import File
from .models.note_model import Note
from .models.document_model import Document
from django.urls import reverse
from django import forms
from django.utils.html import format_html
from .models.project import FlightProject
from apps.flights.models.flight_model import CharterFlight
from django.utils.translation import gettext_lazy as _
from apps.flights.utils.vda_parser_bb import parse_msg_slot
from apps.flights.admins.trip_admin import TripFileAdmin
from apps.flights.models.tripfile_model import TripFile
from apps.flights.admins.flight_admin import CharterFlightAdmin
from apps.flights.models.shipment_model import Shipment
from apps.flights.admins.shipment_admin import ShipmentAdmin


# class LDMInline(admin.TabularInline):
#     model = LDM
#     form = LDMInlineForm
#     extra = 1  # Начальное количество инлайновых форм
#     max_num = 1  # Максимальное количество инлайновых форм
#     can_add = False
#     template = 'admin/ldm_inline.html'
#     formset = LDMInlineFormSet

#     def get_media(self, request):
#         extra = '' if settings.DEBUG else '.min'
#         js = [
#             'https://code.jquery.com/jquery-3.6.0%s.js' % extra,
#             'js/admin_parse_button.js',  # Create this file in your app's static/js directory
#         ]
#         return Media(js=js)

class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1  # Начальное количество инлайновых форм
    max_num = 3  # Максимальное количество инлайновых форм
    can_add = False


class FileInline(admin.TabularInline):
    model = File
    extra = 1  # Начальное количество инлайновых форм
    max_num = 3  # Максимальное количество инлайновых форм
    can_add = False


class NoteInline(admin.TabularInline):
    model = Note
    extra = 1  # Начальное количество инлайновых форм
    max_num = 10  # Максимальное количество инлайновых форм
    can_add = False


class FlightProjectAdmin(admin.ModelAdmin):
    list_display = ['flight', 'get_create_by']
    inlines = [DocumentInline, FileInline, NoteInline]

    def get_create_by(self, obj):
        if obj.created_by:
            return obj.created_by.email
        return None

    get_create_by.short_description = 'Created By'


class FlightProjectInline(admin.StackedInline):
    model = FlightProject
    extra = 1


admin.site.register(Document)
admin.site.register(File)
admin.site.register(Note)
admin.site.register(FlightProject, FlightProjectAdmin)
admin.site.register(TripFile, TripFileAdmin)
admin.site.register(CharterFlight, CharterFlightAdmin)
admin.site.register(Shipment, ShipmentAdmin)
