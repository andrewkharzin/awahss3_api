import re

def parse_scr_message(message):
    # Define the pattern to match the SCR message
    pattern = r'([A-Z])\s*([A-Z0-9]+)\s+(\d{2}[A-Z]{3}\d{2}[A-Z]{3})\s+(\d{7})\s+(\d{7})\s+([A-Z0-9]+)([A-Z]{3})([A-Z])\s+/\s+([A-Z]+)\.([A-Z]+)\.RE\.(\d+)'

    # Attempt to match the pattern
    match = re.match(pattern, message)
    
    if match:
        action_code = match.group(1)
        airline_code = match.group(2)
        flight_number = match.group(2)[3:]
        date_of_flight = match.group(3)
        day_of_week = match.group(4)
        aircraft_code = match.group(5)
        time = match.group(6)
        route_from = match.group(7)
        flight_type = match.group(8)
        registration = match.group(9)
        
        flight_type_descriptions = {
            'A': 'Additional Cargo/Mail',
            'C': 'Charter – Passenger only',
            'E': 'Special VIP Flight (FAA/Government)',
            'F': 'Scheduled – Cargo and/or Mail',
            'G': 'Additional Flights – Passenger Normal Service',
            'H': 'Charter – Cargo and/or Mail',
            'I': 'Ambulance Flight',
            'J': 'Scheduled – Passenger Normal Service',
            'K': 'Training Flights',
            'M': 'Mail Service',
            'O': 'Charter requiring special handling (e.g. migrants, immigrants)',
            'P': 'Positioning Flights – Non Revenue (ferry/delivery/demo)',
            'T': 'Technical Test',
            'W': 'Military',
            'X': 'Technical Stop'
        }

        flight_data = {
            "Action Code": action_code,
            "Airline Code": airline_code,
            "Flight Number": flight_number,
            "Date of Flight": date_of_flight,
            "Day of Week": day_of_week,
            "Aircraft Code": aircraft_code,
            "Time": time,
            "Route From": route_from,
            "Flight Type": flight_type_descriptions.get(flight_type, "Unknown"),
            "Registration": registration
        }

        return flight_data
    else:
        return None

# Test the parser with the example message
example_message = "N NVI320 21SEP21SEP 0004000 000IL7 SZXOVB0830 H / TA.B RE.76503/"
flight_data = parse_scr_message(example_message)
if flight_data:
    print(flight_data)
else:
    print("Failed to parse the message.")
