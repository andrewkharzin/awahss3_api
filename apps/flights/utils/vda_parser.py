import re
from datetime import datetime
import pytz
from  apps.directory.airlines.models.airline import Aircraft

timezone = pytz.timezone('UTC') 

def parse_iata_code(text):
    iata_match = re.search(r'\(([A-Z]{3})/([A-Z]{4})\)', text)
    if iata_match:
        departure_iata = iata_match.group(1)
        arrival_iata = iata_match.group(2)
        return departure_iata, arrival_iata
    print("Failed to parse IATA code in text:", text)
    return None, None

def convert_custom_to_standard(custom_datetime_str):
    print("Input custom_datetime_str:", custom_datetime_str)
    # Convert custom format to standard format
    day = int(custom_datetime_str[:2])
    month_str = custom_datetime_str[2:5]
    month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    month = month_dict.get(month_str)
    year = datetime.now().year
    time_str = custom_datetime_str[6:10]
    hour = int(time_str[:2])
    minute = int(time_str[2:4])
    standard_datetime_str = "{}-{:02d}-{:02d} {:02d}:{:02d}:00".format(year, month, day, hour, minute)
    print("Converted standard_datetime_str:", standard_datetime_str)
    return standard_datetime_str

def parse_datetime(datetime_str):
    try:
        standard_datetime_str = convert_custom_to_standard(datetime_str)
        parsed_datetime = datetime.strptime(standard_datetime_str, '%Y-%m-%d %H:%M:%S')
        print("Parsed datetime:", parsed_datetime)
        return parsed_datetime
    except Exception as e:
        print("Error parsing datetime:", e)
        raise ValueError("Invalid datetime format: {}".format(datetime_str))

def parse_header(text):
    aircraft_type = None
    registration_number = None
    
    header_match = re.search(r'AIRCRAFT:\s*([\w-]+),\s*RA-(\d+)', text)
    if header_match:
        aircraft_type = header_match.group(1)
        registration_number = header_match.group(2)
    
    return aircraft_type, registration_number

def parse_msg_slot(text):
    aircraft_type, registration_number = parse_header(text)
    current_year = datetime.now().year

    lines = text.strip().split('\n')
    flights = []
    current_flight = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("VDA"):
            if current_flight:
                flights.append(current_flight)
           
            flight_info = line.split(maxsplit=1)
            
            current_flight = {
                'flight_number': flight_info[0],
                'aircraft_type': aircraft_type,
                'registration_number': registration_number,
                'action_code': ''
            }

            if len(flight_info) > 1:
                current_flight['flight_route'] = flight_info[1]
                departure_iata, arrival_iata = parse_iata_code(current_flight['flight_route'])
                current_flight['departure_iata'] = departure_iata
                current_flight['arrival_iata'] = arrival_iata
            else:
                current_flight['flight_route'] = ''

        elif current_flight:
            segment_info = line.split(maxsplit=4)
            if len(segment_info) >= 5:
                if 'segments' not in current_flight:
                    current_flight['segments'] = []
                if 'segments' not in current_flight:
                    current_flight['segments'] = []

                date_time = parse_datetime(segment_info[3])
                if date_time:
                    print("Date Time check:", date_time)
                    # date_time = timezone.localize(date_time)
                    print("Localized:", date_time)
                else:
                  continue 
                
                
                current_segment = {
                    'route': segment_info[0],
                    'date_time': date_time,
                    'description': segment_info[4]
                }

                if 'РАЗГРУЗКА' in current_segment['description']:
                    current_flight['action_code'] = 'РАЗГРУЗКА'
                elif 'ЗАГРУЗКА' in current_segment['description']:
                    current_flight['action_code'] = 'ЗАГРУЗКА'

                formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
                print("Formated date time:", formatted_date_time)
                current_segment['date_time'] = formatted_date_time
                
                current_flight['segments'].append(current_segment)
                print(current_flight)

    if current_flight:
        flights.append(current_flight)

     # Now, let's add the aircraft to the Aircraft model
    if registration_number:
        existing_aircraft = Aircraft.objects.filter(registrationNumber=registration_number).first()

        if not existing_aircraft:
            # Create a new instance of Aircraft with the extracted registration_number.
            new_aircraft = Aircraft(
                registration_number=registration_number,
              # You can set other fields as needed.
                # Set other fields as needed.
            )

            # Save the new aircraft instance to the database.
            new_aircraft.save()
    return flights
