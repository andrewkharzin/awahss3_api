from django.contrib import admin
from tablib import Dataset
from import_export.results import RowResult
from django.http import HttpResponseRedirect
from import_export.admin import ImportExportModelAdmin
from apps.directory.airlines.models.airline import Airline, Aircraft
from django.urls import path, reverse
from import_export import resources



@admin.register(Airline)
class AilineAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'thumbnail_preview',
        'banner_img',
        "ageFleet",
        "callsign",
        "codeHub",
        "codeIataAirline",
        "codeIcaoAirline",
        "codeIso2Country",
        "founding",
        "iataPrefixAccounting",
        "nameAirline",
        "nameCountry",
        "thumbnail_country_preview",
        "sizeAirline",
        "statusAirline",
        "type",

        
    ]
    search_fields = ['codeIataAirline', 'nameAirline', 'codeIcaoAirline', 'codeIso2Country', 'iataPrefixAccounting',]

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    def thumbnail_country_preview(self, obj):
        return obj.thumbnail_country_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    thumbnail_country_preview.short_description = 'Thumbnail Country Preview'
    thumbnail_country_preview.allow_tags = True



class AircraftResource(resources.ModelResource):
    class Meta:
        model = Aircraft
        fields = ('id', 'registration_number', 'ac_code', 'codeIataAirline', 'model',)

    # def get_import_id_fields(self):
    #     return ['id']

@admin.register(Aircraft)
class AircraftAdmin(ImportExportModelAdmin):
    # resource_class = [AircraftResource]
    resource_class = AircraftResource
    list_display = ('registration_number', 'airline', 'ac_code', 'model',)
    list_filter = ('airline',)
    search_fields = ('registration_number', 'model',)

    def before_import_row(self, row, **kwargs):
        # Get the airline code from the Excel row
        airline_code_excel = row.get('airline')
        
        # Find the matching Airline instance using the airline code
        try:
            airline = Airline.objects.get(codeIataAirline=airline_code_excel)
            row['airline'] = airline.id  # Set the correct Airline instance for the row
        except Airline.DoesNotExist:
            # If no matching airline found, skip this row during import
            kwargs['skip'] = True