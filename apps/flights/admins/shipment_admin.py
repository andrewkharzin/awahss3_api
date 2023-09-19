import json
from django.contrib import admin
from apps.flights.models.shipment_model import Shipment, ULD
from apps.flights.utils.ffm_tomodel import parse_message

class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 1

class ULDAdmin(admin.ModelAdmin):
    list_display = ('uld_number',)  
    search_fields = ('uld_number',) 
    inlines = [ShipmentInline]  

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('awb', 'route_from', 'route_to', 'pieces_type',
                    'kilos', 'cubic_meter', 'last_pics', 'goods', 'special_handling_code')
    search_fields = ('uld_number', 'awb', 'goods')

    def parse_and_save_shipments(self, request, queryset):
        text_test = """
         AIRCRAFT: IL-76TD-90VD, RA-76950 OR SUBST
           VDA420 ZHENGZHOU/XINZH (CGO/ZHCC) ETD 24AUG/2150Z ЗАГРУЗКА
                  NOVOSIBIRSK/TOL (OVB/UNNT) ETA 25AUG/0320Z
           VDA420 NOVOSIBIRSK/TOL (OVB/UNNT) ETD 25AUG/0620Z
                  MOSCOW/SHEREMET (SVO/UUEE) ETA 25AUG/1050Z РАЗГРУЗКА
         
          VDA2050 MOSCOW/SHEREMET (SVO/UUEE) ETD 26AUG/0600Z ЗАГРУЗКА
                  MUMBAI/CHHATRAP (BOM/VABB) ETA 26AUG/1400Z РАЗГРУЗКА

        """
        
        parsed_data_json = parse_message(text_test)
        parsed_data_list = json.loads(parsed_data_json)

        for data in parsed_data_list:
            shipment = Shipment.objects.create(
                version=data.get('version', ''),
                flight_number=data.get('flight_number', ''),
                date=data.get('date', ''),
                iata=data.get('iata', ''),
                registration_number=data.get('registration_number', ''),
                uld_number=data.get('uld_number', ''),
                awb=data.get('awb', ''),
                route_from=data.get('route_from', ''),
                route_to=data.get('route_to', ''),
                pieces_type=data.get('pieces_type', ''),
                kilos=data.get('kilos', ''),
                cubic_meter=data.get('cubic_meter', ''),
                last_pics=data.get('last_pics', ''),
                goods=data.get('goods', ''),
                special_handling_code=data['special_handling_code'],
                message="Your original message here",
            )
        
        self.message_user(request, f'Successfully parsed and saved {len(parsed_data_list)} shipments.')

    parse_and_save_shipments.short_description = "Parse and Save Shipments from text_test"

    actions = [parse_and_save_shipments]



