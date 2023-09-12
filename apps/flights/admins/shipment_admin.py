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

text = """
FFM/8
1/HY3123/05SEP2200/TAS/UK67001
SVO
ULD/FQA0362HY
250-91841956HKGSVO/S2K808MC1T51/CABLE FAST LOCK
/SPX
ULD/FQA0372HY
250-91840781HKGSVO/S22K422MC1T158/CPU SOLID STATE
/SPX
250-91841956HKGSVO/S2K790MC1T51/CABLE FAST LOCK
/SPX
ULD/FQA18537R7
250-91841956HKGSVO/S2K790MC1T51/CABLE FAST LOCK
/SPX
ULD/FQA18582R7
250-91841956HKGSVO/S2K942MC1T51/CABLE FAST LOCK
/SPX
250-91842251HKGSVO/T19K164MC1/CONNECTOR
/SPX
ULD/FQA18631R7
250-91838434HKGSVO/T2K674MC1/PAD MOBILE PHON
/ELI/SPX
ULD/PAG30348R7
250-91840000HKGSVO/S15K964MC1T276/COMMUNICATION B
/ELM/SPX
250-91840781HKGSVO/S50K684MC1T158/CPU SOLID STATE
/SPX
ULD/PAG55379R7
250-91841956HKGSVO/S4K860MC1T51/CABLE FAST LOCK
/SPX
ULD/PAG57514R7
250-91838563HKGSVO/S24K255MC1T149/PCB ASSEMBLY BA
/SPX
250-91840000HKGSVO/S16K800MC1T276/COMMUNICATION B
/ELM/SPX
250-91841956HKGSVO/S3K829MC1T51/CABLE FAST LOCK
/SPX
ULD/PAG58712R7
250-91829566HKGSVO/T3K26MC1/CAPACITOR CONNE
/SPX
SVO
ULD/PAG58712R7
250-91839
"""


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('uld_number', 'awb', 'route_from', 'route_to', 'pieces_type',
                    'kilos', 'cubic_meter', 'last_pics', 'goods', 'special_handling_code')
    search_fields = ('uld_number', 'awb', 'goods')

    def save_model(self, request, obj, form, change):
        if text:
            # print(obj.test_message)
            parsed_data_json = parse_message(text)
            print("Parsed shipments:", parsed_data_json)
            parsed_data_list = json.loads(parsed_data_json)

            for data in parsed_data_list:
                print("Parsing daya list:", data)
                version = data.get('version', '')
                flight_number = data.get('flight_number', '')
                date = data.get('date', '')
                iata = data.get('iata', '')
                registration_number = data.get('registration_number', '')
                uld_number = data.get('uld_number', '')
                awb = data.get('awb', '')
                route_from = data.get('route_from', '')
                route_to = data.get('route_to', '')
                pieces_type = data.get('pieces_type', '')
                kilos = data.get('kilos', '')
                cubic_meter = data.get('cubic_meter', '')
                last_pics = data.get('last_pics', '')
                goods = data.get('goods', '')
                special_handling_code = data['special_handling_code']
                message = data.get('message', '')

                print("Parsed Values:")
                print("version:", version)
                print("flight_number:", flight_number)
                print("Date:", date)
                print("registration_number:", registration_number)
                print("iata:", iata)
                print("uld_number:", uld_number)
                print("awb:", awb)
                print("route_to:", route_to)
                print("route_from:", route_from)
                print("pieces_type:", pieces_type)
                print("kilos:", kilos)
                print("cubic_meter:", cubic_meter)
                print("last_pics:", last_pics)
                print("goods:", goods)
                print("special_handling_code:", special_handling_code)
                print("message:", message)

                shipment = Shipment.objects.create(
                    version=version,
                    flight_number=flight_number,
                    date=date,
                    registration_number=registration_number,
                    iata=iata,
                    uld_number=uld_number,
                    awb=awb,
                    route_to=route_to,
                    route_from=route_from,
                    pieces_type=pieces_type,
                    kilos=kilos,
                    cubic_meter=cubic_meter,
                    last_pics=last_pics,
                    goods=goods,
                    special_handling_code=special_handling_code,
                    message=obj.message,
                )
                print("Created Shipment:", shipment)

        super().save_model(request, obj, form, change)
