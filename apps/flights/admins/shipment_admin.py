import re
import json
from django.urls import path
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import admin
from apps.flights.models.shipment_model import Shipment  # Import your Shipment model
import datetime
from apps.flights.utils.ffm_tomodel import parse_message
# from apps.flights.utils.ffm_to_model_copy import parse_message
import logging

from apps.flights.utils.ffm_tomodel import parse_message
# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)




class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('uld_number', 'awb', 'route_from', 'route_to', 'pieces_type',
                    'kilos', 'cubic_meter', 'last_pics', 'goods', 'special_handling_code')
    search_fields = ('uld_number', 'awb', 'goods')
