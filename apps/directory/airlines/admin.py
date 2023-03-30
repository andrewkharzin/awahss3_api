from django.contrib import admin
from django.http import HttpResponseRedirect
from import_export.admin import ImportExportModelAdmin
from apps.directory.airlines.models.airline import Airline
from django.urls import path, reverse



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