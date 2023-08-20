from django.contrib import admin
from .models.flight_model import Flight
from .models.file_model import File
from .models.note_model import Note
from .models.document_model import Document
from django.urls import reverse
from django.utils.html import format_html
from .models.project import FlightProject
from django.utils.translation import gettext_lazy as _


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
    list_display = ['flight_number', 'airline', 'formatted_rout', 'formatted_date', 'formatted_time', 'flight_type', 'get_documents_count', 'get_files_count', 'flight_project_link', 'handling_status']
    list_filter = ['flight_type']
    search_fields = ['flight_number', 'airline__codeIataAirline']
    date_hierarchy = 'date'
    inlines = [FlightProjectInline]

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
        super().save_model(request, obj, form, change)

        if obj.create_flight_project and not obj.flight_project:
            # Create FlightProject instance with automated name
            flight_project = FlightProject.objects.create(flight=obj)
            obj.flight_project = flight_project
            obj.save()

admin.site.register(Flight, FlightAdmin)
admin.site.register(Document)
admin.site.register(File)
admin.site.register(Note)
admin.site.register(FlightProject, FlightProjectAdmin)