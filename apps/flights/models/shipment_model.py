from django.db import models
import json
from datetime import timezone
from apps.flights.utils.ffm_tomodel import parse_message


class Shipment(models.Model):
    version = models.CharField(max_length=10, null=True, blank=True)
    flight_number = models.CharField(max_length=10, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    iata = models.CharField(max_length=10, null=True, blank=True)
    registration_number = models.CharField(
        max_length=10, null=True, blank=True)
    uld_number = models.CharField(max_length=20, null=True, blank=True)
    awb = models.CharField(max_length=20, null=True, blank=True)
    route_from = models.CharField(max_length=10, null=True, blank=True)
    route_to = models.CharField(max_length=10, null=True, blank=True)
    pieces_type = models.CharField(max_length=3, null=True, blank=True)
    kilos = models.IntegerField(null=True, blank=True)
    cubic_meter = models.IntegerField(null=True, blank=True)
    last_pics = models.IntegerField(null=True, blank=True)
    goods = models.CharField(max_length=100, null=True, blank=True)
    special_handling_code = models.CharField(
        max_length=10, null=True, blank=True)

    message = models.TextField()

    def __str__(self):
        return f"Shipment {self.awb}"

    # def save(self, *args, **kwargs):
    #     if self.message:
    #         print("Message RAW:", self.message)
    #         parsed_data_json = parse_message(self.message)
    #         print("JSON DATA:", parsed_data_json)
    #         parsed_data_list = json.loads(parsed_data_json)
    #         print("Parsed list:", parsed_data_list )

    #         for data in parsed_data_list:
    #             print("DATA", data)
    #             print(f"Saving data: {data}")
    #             Shipment.objects.create(
    #                 version=data['version'],
    #                 flight_number=data['flight_number'],
    #                 date=data['date'],
    #                 iata=data['iata'],
    #                 registration_number=data['registration_number'],
    #                 uld_number=data['uld_number'],
    #                 awb=data['awb'],
    #                 route_from=data['route_from'],
    #                 route_to=data['route_to'],
    #                 pieces_type=data['pieces_type'],
    #                 kilos=data['kilos'],
    #                 cubic_meter=data['cubic_meter'],
    #                 last_pics=data['last_pics'],
    #                 goods=data['goods'],
    #                 special_handling_code=data['special_handling_code'],
    #                 message=self.message
    #             )
    #     super(Shipment, self).save(*args, **kwargs)

    # def save_model(self, request, obj, form, change):
    #     if obj.message:
    #         parsed_data_json = parse_message(obj.message)
    #         print("Parsed flights:", parsed_data_json)
    #         parsed_data_list = json.loads(parsed_data_json)

    #         # flight_date = None
    #         # flight_time = None
    #         # flight_date_time = None

    #         for data in parsed_data_list:
    #             print("Parsing daya list:", data)
    #             version = data.get('version', '')
    #             flight_number = data.get('flight_number', '')
    #             date = data.get('date', '')
    #             iata = data.get('iata', '')
    #             registration_number = data.get('registration_number', '')
    #             uld_number = data.get('uld_number', '')
    #             awb = data.get('awb', '')
    #             route_from = data.get('route_from', '')
    #             route_to = data.get('route_to', '')
    #             pieces_type = data.get('pieces_type', '')
    #             kilos = data.get('kilos', '')
    #             cubic_meter = data.get('cubic_meter', '')
    #             last_pics = data.get('last_pics', '')
    #             goods = data.get('goods', '')
    #             special_handling_code = data('special_handling_code', '')
    #             message = data.get('message', '')

    #             print("Parsed Values:")
    #             print("version:", version)
    #             print("flight_number:", flight_number)
    #             print("Date:", date)
    #             print("registration_number:", registration_number)
    #             print("iata:", iata)
    #             print("uld_number:", uld_number)
    #             print("awb:", awb)
    #             print("route_to:", route_to)
    #             print("route_from:", route_from)
    #             print("pieces_type:", pieces_type)
    #             print("kilos:", kilos)
    #             print("cubic_meter:", cubic_meter)
    #             print("last_pics:", last_pics)
    #             print("goods:", goods)
    #             print("special_handling_code:", special_handling_code)
    #             print("message:", message)

    #             shipment = Shipment.objects.create(
    #                 version=version,
    #                 flight_number=flight_number,
    #                 date=date,
    #                 registration_number=registration_number,
    #                 iata=iata,
    #                 uld_number=uld_number,
    #                 awb=awb,
    #                 route_to=route_to,
    #                 route_from=route_from,
    #                 pieces_type=pieces_type,
    #                 kilos=kilos,
    #                 cubic_meter=cubic_meter,
    #                 last_pics=last_pics,
    #                 goods=goods,
    #                 special_handling_code=special_handling_code,
    #                 message=obj.message,
    #             )
    #             print("Created Shipment:", shipment)

    #     super().save_model(request, obj, form, change)
