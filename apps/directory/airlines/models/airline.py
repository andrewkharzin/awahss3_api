from django.db import models
import os
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe


def aircraft_image_path(instance, filename):
    # Dynamic upload path logic using the airline and registration_number
    return f'airlines/banners/{instance.airline}/{instance.registrationNumber}/{filename}'


def airline_banner_directory_path(instance, filename):
    codeIataAirline = slugify(instance.codeIataAirline)
    codeIcaoAirline = slugify(instance.codeIcaoAirline)
    _, extension = os.path.splitext(filename)
    return f"airlines/banners/{codeIataAirline}/{codeIcaoAirline}{extension}"


class Airline(models.Model):

    # class params:
    #     db = 'atlas'

    ageFleet = models.IntegerField(null=True)
    founding = models.IntegerField(null=True)
    sizeAirline = models.IntegerField(null=True)
    statusAirline = models.CharField(
        _("StatusAirline"), max_length=155, default="", blank=True)
    iataPrefixAccounting = models.IntegerField(null=True)
    callsign = models.CharField(
        _("Callsign"), max_length=155, default="", blank=True, null=True)
    codeHub = models.CharField(
        _("CodeHUB"), max_length=5, default="", blank=True, null=True)
    codeIso2Country = models.CharField(
        _("CodeIso2Country"), max_length=4, default="", blank=True)
    codeIataAirline = models.CharField(
        _("Iata"), max_length=3, default="", blank=True, null=True)
    codeIcaoAirline = models.CharField(
        _("Icao"), max_length=4, default="", blank=True, null=True)
    nameAirline = models.CharField(
        _("Description eng"), max_length=85, default="", blank=True)
    nameCountry = models.CharField(
        _("Country"), max_length=85, default="", null=True, blank=True)
    type = models.CharField(_("Type"), max_length=155, default="", blank=True)
    arl_logo = models.ImageField(
        upload_to='airlines/square/')
    cntr_logo = models.ImageField(
        upload_to='countries/logos/')
    banner_img = models.ImageField(
        upload_to=airline_banner_directory_path, blank=True, null=True)

    @property
    def thumbnail_preview(self):
        if self.arl_logo:
            return mark_safe('<img src="{}" width="80" />'.format(self.arl_logo.url))
        return ""

    @property
    def thumbnail_country_preview(self):
        if self.cntr_logo:
            return mark_safe('<img src="{}" width="80" />'.format(self.cntr_logo.url))
        return ""

    def __str__(self):
        return f"{self.codeIataAirline.upper()}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)


class Aircraft(models.Model):
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, null=True, blank=True)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True
    codeIataAirline = models.CharField(max_length=4, null=True, blank=True)
    registrationNumber = models.CharField(
        max_length=20, blank=True, null=True)
    acCode = models.CharField(
        max_length=4, blank=True, null=True)  # Add ICAO field
    # iata = models.CharField(max_length=3, null=True, blank=True)  # Add IATA field
    model = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=aircraft_image_path,
                              default="airlines/banners/default_ac.jpeg")  # Add image field

    def __str__(self):
        return f"{self.model}-{self.registrationNumber}"
