import re
from datetime import datetime

message = """
SCR
/SVOKW7X@SVO.AERO
S23
29AUG
SVO
KKAF3217 30AUG 0030000 (0 pax) C17 KWI1120 H
K KAF3217 31AUG 0004000 (0 pax) C17 0855KWI  P
/TA.B TD.C/
SI REG: 30001A (alternate 30002A) / KUWAIT AIR FORCE / KUWAIT
SI A/C: C17 / MTOW: 265,352 KG
SI PURPOSE: MILITARY FLIGHT / PURP FLT –CARGO SEGMENTS IN   / WITHOUT  PAX
SI LANDING PERMIT: MID51/0308
SI CARGO DETAILS: KWI-SVO /DETAILED DESCRIPTION/ DIPLOMATIC SUPPORT CARGO, OFFICE SUPPLIES

SI SHIPPER : KUWAIT AIR FORCE
SI CONSIGNEE : KUWAIT EMBASSY
SI ON SECTION SVO-KWI - EMPTY
SI HEREBY WE CONFIRM THAT THERE ARE NO AMMUNITIONS NO DG HAZARDOUS GOODS ON BOARD
SI TOW BAR ON BOARD
SI "Moscow Cargo" is cargo handling agent
"""


# Define patterns for extracting flight information for arrival and departure
flight_pattern_arrival = r'\s*([A-Z]+)([A-Z]+\d+)\s+(\d{2}[A-Z]{3})\s+\d+\s+\(\d+pax\)\s+(\w+)\s+(\w+)\s+(\d{2})(\d{2})([A-Z]{3})\s+'
flight_pattern_departure = r'\s*([A-Z]) ([A-Z]+\d+)\s+(\d{2}[A-Z]{3})\s+\d+\s+\(\d+pax\)\s+(\w+)\s+(\d{2})(\d{2})([A-Z]{3})\s+'
si_pattern = r'SI (\w+[^:]+): ([^\n]+)'

# Extract flight information for arrival
flight_match_arrival = re.search(flight_pattern_arrival, message)
if flight_match_arrival:
    action_code_arrival = flight_match_arrival.group(1)
    flight_number_arrival = flight_match_arrival.group(2)
    flight_date_arrival = datetime.strptime(flight_match_arrival.group(3), '%d%b').replace(year=datetime.now().year)
    aircraft_type_arrival = flight_match_arrival.group(4)
    airport_code_arrival = flight_match_arrival.group(5)
    time_hour_arrival = int(flight_match_arrival.group(6))
    time_minute_arrival = int(flight_match_arrival.group(7))
    time_indicator_arrival = flight_match_arrival.group(8)

# Extract flight information for departure
flight_match_departure = re.search(flight_pattern_departure, message)
if flight_match_departure:
    action_code_dep = flight_match_departure.group(1)
    flight_number_dep = flight_match_departure.group(2)
    flight_date_dep = datetime.strptime(flight_match_departure.group(3), '%d%b').replace(year=datetime.now().year)
    aircraft_type_dep = flight_match_departure.group(4)
    time_hour_dep = int(flight_match_departure.group(5))
    time_minute_dep = int(flight_match_departure.group(6))
    airport_code_dep = flight_match_departure.group(7)

# Extract SI details
si_parts = re.findall(si_pattern, message)
si_details = {si_key: si_value for si_key, si_value in si_parts}

# Print the extracted information
if flight_match_arrival:
    print("Arrival Information:")
    print(f"Action Code (Arrival): {action_code_arrival}")
    print(f"Flight Number (Arrival): {flight_number_arrival}")
    print(f"Flight Date (Arrival): {flight_date_arrival}")
    print(f"Aircraft Type (Arrival): {aircraft_type_arrival}")
    print(f"Airport Code (Arrival): {airport_code_arrival}")
    print(f"Time (Arrival): {time_hour_arrival}:{time_minute_arrival} {time_indicator_arrival}")

if flight_match_departure:
    print("Departure Information:")
    print(f"Action Code (Departure): {action_code_dep}")
    print(f"Flight Number (Departure): {flight_number_dep}")
    print(f"Flight Date (Departure): {flight_date_dep}")
    print(f"Aircraft Type (Departure): {aircraft_type_dep}")
    print(f"Time (Departure): {time_hour_dep}:{time_minute_dep}")
    print(f"Airport Code (Departure): {airport_code_dep}")

print("SI Details:")
for si_key, si_value in si_details.items():
    print(f"SI {si_key}: {si_value}")
