from django.contrib import admin
from django.utils import timezone
from django.forms.models import inlineformset_factory
import datetime
from apps.directory.airlines.models.airline import Airline
from .models.flight_model import Flight, LDM
from .models.file_model import File
from .models.note_model import Note
from .models.document_model import Document
from django.urls import reverse
from django import forms
from django.utils.html import format_html
from .models.project import FlightProject
from apps.flights.models.flight_model import CharterFlight
from django.utils.translation import gettext_lazy as _
from apps.flights.utils.vda_parser import parse_msg_slot

class LDMInlineForm(forms.ModelForm):
    class Meta:
        model = LDM
        fields = '__all__'

    parse_success = forms.BooleanField(label='Parse Success', required=False, disabled=True)

LDMInlineFormSet = inlineformset_factory(Flight, LDM, form=LDMInlineForm, extra=1)

class LDMInline(admin.TabularInline):
    model = LDM
    form = LDMInlineForm
    extra = 1  # Начальное количество инлайновых форм
    max_num = 1  # Максимальное количество инлайновых форм
    can_add = False
    template = 'admin/ldm_inline.html'
    formset = LDMInlineFormSet

    def get_media(self, request):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'https://code.jquery.com/jquery-3.6.0%s.js' % extra,
            'js/admin_parse_button.js',  # Create this file in your app's static/js directory
        ]
        return Media(js=js)

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
    list_display = ['fprj_id', 'flight', 'get_create_by']
    inlines = [DocumentInline, FileInline, NoteInline]

    def get_create_by(self, obj):
        if obj.created_by:
            return obj.created_by.email
        return None

    get_create_by.short_description = 'Created By'

class FlightProjectInline(admin.StackedInline):
    model = FlightProject
    extra = 1


class FlightAdmin(admin.ModelAdmin):
    actions = ['parse_and_update']

    list_display = ['flight_number', 'airline', 'formatted_rout', 'formatted_date',  'flight_type', 'get_documents_count', 'get_files_count', 'flight_project_link', 'handling_status']
    list_filter = ['flight_type']
    search_fields = ['flight_number', 'airline__codeIataAirline']
    date_hierarchy = 'date_time'
    inlines = [LDMInline]

    class Media:
        js = ['js/admin_parse_button.js']

    def formatted_date(self, obj):
        return obj.get_formatted_date()

    formatted_date.short_description = _('Formatted Date')

    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M')

    formatted_time.short_description = _('Formatted Time')

    def get_documents_count(self, obj):
        return obj.document_set.count()

    get_documents_count.short_description = _('Documents')

    def get_files_count(self, obj):
        return obj.file_set.count()

    get_files_count.short_description = _('Files')

    def formatted_rout(self, obj):
        if obj.flight_type == 'departure':
            return f"To {obj.flight_route}"
        elif obj.flight_type == 'arrival':
            return f"From {obj.flight_route}"
        else:
            return ''

    formatted_rout.short_description = _('From/To')

    def flight_project_id(self, obj):
        if obj.flight_project:
            return obj.flight_project.id
        else:
            return ''

    flight_project_id.short_description = _('Flight Project ID')

    def flight_project_link(self, obj):
        if obj.flight_project:
            url = reverse('admin:flights_flightproject_change', args=[obj.flight_project.id])
            return format_html('<a href="{}">{}</a>', url, obj.flight_project.fprj_id)
        else:
            return ''

    flight_project_link.short_description = _('Flight Project')

    flight_project_link.short_description = _('Flight Project')

    def changelist_view(self, request, extra_context=None):
        if 'action' not in request.GET:
            if 'flight_type__exact' in request.GET:
                # Override the header based on the flight_type__exact filter
                flight_type = request.GET['flight_type__exact']
                if flight_type == 'departure':
                    self.formatted_rout.short_description = _('To')
                elif flight_type == 'arrival':
                    self.formatted_rout.short_description = _('From')
                else:
                    self.formatted_rout.short_description = _('From/To')

        return super().changelist_view(request, extra_context=extra_context)

    
    # def save_model(self, request, obj, form, change):
    #     print("Before saving Flight model...")
        
    #     super().save_model(request, obj, form, change)

    #     if obj.create_flight_project and not obj.flight_project:
    #         print("Creating Flight Project")
    #         # Create FlightProject instance with automated name
    #         flight_project = FlightProject.objects.create(flight=obj)
    #         obj.flight_project = flight_project
    #         obj.save()
        
    #     if obj.ldm_telexes.exists():
    #         ldm_instance = obj.ldm_telexes.first()
    #         if ldm_instance.text:
    #             parsed_flights = parse_msg_slot(ldm_instance.text)
                
    #             create_flights_from_code(parsed_flights)
    #             print("Parsing and creating Flight instances...")

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         if instance.flight:
    #             try:
    #                 ldm_instance = LDM.objects.get(id=instance.flight.ldm_telex)
    #                 if ldm_instance.text:
    #                     print("Parsing and creating Flight instances...")
    #                     parsed_flights = parse_msg_slot(ldm_instance.text)
    #                     print("Parsed Flights:", parsed_flights)
    #                     if parsed_flights:
    #                         parsed_flight = parsed_flights[0]
    #                         print("Parsed Flight:", parsed_flight)
    #                         instance.flight_number = parsed_flight['flight_number']
    #                         instance.flight_route = parsed_flight['flight_route']
    #                         instance.date = parsed_flight['date_time'].split()[0]
    #                         instance.time = parsed_flight['date_time'].split()[1]
    #             except LDM.DoesNotExist:
    #                 pass  # Handle the case where the related LDM instance does not exist
    #     formset.save()



admin.site.register(Flight, FlightAdmin)
admin.site.register(Document)
admin.site.register(File)
admin.site.register(Note)
admin.site.register(FlightProject, FlightProjectAdmin)



class CharterFlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'aircraft_type', 'action_code', 'registration_number', 'iata')
    actions = ['process_and_create_flights']
    list_filter = ['iata', 'action_code']



    def save_model(self, request, obj, form, change):
        if obj.message_code:
            parsed_flights = parse_msg_slot(obj.message_code)
            print("Parsed flights:", parsed_flights)

            # flight_date = None
            # flight_time = None
            # flight_date_time = None 
            
            for parsed_flight in parsed_flights:
                print("Parsing flight:", parsed_flight)
                action_code = parsed_flight.get('action_code', '')
                flight_route = parsed_flight.get('flight_route', '')
                # flight_date_time_str = parsed_flight.get('date_time', '')
                
                if ('РАЗГРУЗКА' in action_code or 'ЗАГРУЗКА' in action_code) and 'MOSCOW/SHEREMET (SVO/UUEE) ETA' and 'MOSCOW/SHEREMET (SVO/UUEE) ETD' in flight_route:
                    # flight_date_time = datetime.datetime.strptime(flight_date_time_str, '%Y-%m-%d %H:%M:%S')
                    # if flight_date_time_str:  # Check if the flight_date_time_str is not empty
                    #     flight_date_time = datetime.datetime.strptime(flight_date_time_str, '%Y-%m-%d %H:%M:%S')
                    #     flight_date = flight_date_time.date()
                    #     flight_time = flight_date_time.time()
                    
                    # Только если условия выполняются, создаем запись
                    flight_number = parsed_flight.get('flight_number', '')
                    aircraft_type = parsed_flight.get('aircraft_type', '')
                    registration_number = parsed_flight.get('registration_number', '')
                    departure_iata = parsed_flight.get('departure_iata', '')
                    arrival_iata = parsed_flight.get('arrival_iata', '')
                    flight_data_time = parsed_flight.get('date_time', '')
                    if flight_data_time:
                        formatted_date_time = flight_data_time.strftime('%d.%m.%Y %H:%M')
                    else:
                        formatted_date_time = None

                    slot_msg = f"{flight_number} {aircraft_type} {registration_number} {flight_route} {action_code}"

                    print("Parsed Values:")
                    print("flight_data_time:", flight_data_time)
                    print("flight_number:", flight_number)
                    print("aircraft_type:", aircraft_type)
                    print("registration_number:", registration_number)
                    print("flight_route:", flight_route)
                    print("departure_iata:", departure_iata)
                    print("arrival_iata:", arrival_iata)
                    print("action_code:", action_code)

                    charter_flight = CharterFlight.objects.create(
                        flight_number=flight_number,
                        aircraft_type=aircraft_type,
                        registration_number=registration_number,
                        flight_route=flight_route,
                        iata=departure_iata,
                        icao=arrival_iata,
                        message_code=obj.message_code,
                        action_code=action_code,
                        slot_msg=slot_msg,
                        # flight_data_time=formatted_date_time
                        # flight_date=flight_date,  # Use flight_date instead of flight_data
                        # flight_time=flight_time
                    )
                    print("Created CharterFlight:", charter_flight)

        super().save_model(request, obj, form, change)

    

admin.site.register(CharterFlight, CharterFlightAdmin)