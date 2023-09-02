from django.contrib import admin
from apps.flights.models.flight_model import CharterFlight
from apps.flights.utils.vda_parser import parse_msg_slot


class CharterFlightAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'aircraft_type', 'action_code', 'registration_number', 'iata')
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
                
                # if ('РАЗГРУЗКА' in action_code or 'ЗАГРУЗКА' in action_code) and 'MOSCOW/SHEREMET' in flight_route:
                if 'РАЗГРУЗКА' in action_code or 'ЗАГРУЗКА' in action_code:
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

