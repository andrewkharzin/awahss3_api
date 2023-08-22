from django.contrib import admin
from django.utils import timezone
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
from django.utils.translation import gettext_lazy as _
from .utils.ldm_parse import parse_ldm_text

class LDMInlineForm(forms.ModelForm):
    parse_button = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    parse_status = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = LDM
        fields = '__all__'

class LDMInline(admin.TabularInline):
    model = LDM
    form = LDMInlineForm
    extra = 1  # Начальное количество инлайновых форм
    max_num = 1  # Максимальное количество инлайновых форм
    can_add = False

    class Media:
        js = ('flights/ldm_parse.js',)
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

    list_display = ['flight_number', 'airline', 'formatted_rout', 'formatted_date', 'formatted_time', 'flight_type', 'get_documents_count', 'get_files_count', 'flight_project_link', 'handling_status']
    list_filter = ['flight_type']
    search_fields = ['flight_number', 'airline__codeIataAirline']
    date_hierarchy = 'date'
    inlines = [FlightProjectInline, LDMInline]

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


    
    def save_model(self, request, obj, form, change):
        print("save_model method called")
        
        super().save_model(request, obj, form, change)

        if obj.create_flight_project and not obj.flight_project:
            print("Creating Flight Project")
            # Create FlightProject instance with automated name
            flight_project = FlightProject.objects.create(flight=obj)
            obj.flight_project = flight_project
            obj.save()

        # Check if ldm_telex is not None before accessing its attributes
        # if obj.ldm_telex:
        #     print("LDM Telex is set")
        #     ldm_text = obj.ldm_telex.text
        #     parsed_data = parse_ldm_text(ldm_text)
        #     print("Parsed Data in save_model:", parsed_data)  # Print parsed data

        #     if parsed_data:
               
        #         ac_reg_number = parsed_data['ac_reg_number']
        #         obj.ac_reg_number = ac_reg_number
        #         obj.flight_number = flight_number
        #         obj.airline = Airline.objects.get(codeIataAirline=parsed_data['iata_code'])
        #         obj.save()

        if obj.ldm_telex:
            print("Parsing LDM Text:", obj.ldm_telex.text)
            parsed_data = parse_ldm_text(obj.ldm_telex.text)
            print("Parsed Data in save_model:", parsed_data)  # Print parsed data

            if parsed_data:
                obj.iata_code = parsed_data['iata_code']
                obj.flight_number = parsed_data['flight_number']
                obj.ac_reg_number = parsed_data['ac_reg_number']

                # current_year = datetime.date.today().year
                # current_month = datetime.date.today().month
                # day = parsed_data['date']
                # month = int(parsed_data['index1'])

                # year = current_year if month >= current_month else current_year + 1
                # obj.date = datetime.date(year, month, day)
                # obj.date = datetime.date.today()  # Use current server date
    
                obj.save()
                print("Flight Instance:", obj)



    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)

    #     for instance in instances:
    #         if isinstance(instance, LDM):
    #             ldm_text = instance.text
    #             parsed_data = parse_ldm_text(ldm_text)
    #             print("Parsed Data in save_formset:", parsed_data)  # Print parsed data

    #             if parsed_data:
    #                 ac_reg_number = parsed_data['ac_reg_number']
    #                 flight_number = parsed_data['flight_number']
    #                 flight_instance = instance.flight  # Get the related Flight instance
    #                 print("Flight Instance:", flight_instance)  # Print the Flight instance
    #                 flight_instance.ac_reg_number = ac_reg_number
    #                 flight_instance.flight_number = flight_number
    #                 flight_instance.save()

    #     formset.save_m2m()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            if isinstance(instance, LDM):
                ldm_text = instance.text
                parsed_data = parse_ldm_text(ldm_text)
                print("Parsed Data in save_formset:", parsed_data)  # Print parsed data

                if parsed_data:
                    iata_code = parsed_data['iata_code']
                    ac_reg_number = parsed_data['ac_reg_number']
                    flight_number = parsed_data['flight_number']
                    flight_instance = instance.flight  # Get the related Flight instance
                    print("Flight Instance:", flight_instance)  # Print the Flight instance

                    # Search for the Airline instances with the given IATA code
                    airline_instances = Airline.objects.filter(codeIataAirline=iata_code)

                    if airline_instances.exists():
                        airline_instance = airline_instances.first()
                        flight_instance.ac_reg_number = ac_reg_number
                        flight_instance.flight_number = flight_number
                        flight_instance.airline = airline_instance
                        flight_instance.save()
                    else:
                        print(f"No Airline instance found for IATA code: {iata_code}")
                        # You can choose how to handle this situation, e.g., raise an error or use a default value
                        pass

        formset.save_m2m()

    




admin.site.register(Flight, FlightAdmin)
admin.site.register(Document)
admin.site.register(File)
admin.site.register(Note)
admin.site.register(FlightProject, FlightProjectAdmin)