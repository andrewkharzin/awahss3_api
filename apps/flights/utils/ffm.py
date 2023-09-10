import re
from apps.flights.models.shipment_model import Shipment
from datetime import datetime

message = """
FFM/8
1/HY3123/05SEP2200/TAS/UK67001
SVO
ULD/FQA0362HY
250-91841956HKGSVO/S2K808MC1T51/CABLE FAST LOCK
/SPX
ULD/FQA0372HY
250-91840781HKGSVO/S22K422MC1T158/CPU SOLID STATE
/SPX
"""

# Define a regular expression pattern to match the header with the MULTILINE flag
header_pattern = r'^FFM/\d+\n(\d+)/([A-Z0-9]+)/(\d{2}[A-Z]{3}\d{4})/([A-Z]+)/([A-Z0-9]+)\n'

# Match the header information
header_match = re.search(header_pattern, message, re.MULTILINE)
print(message)

if header_match:
    version, flight, date, iata, registration = header_match.groups()
    print("Version:", version)
    print("Flight Number:", flight)
    print("Date:", date)
    print("IATA From:", iata)
    print("Registration Number:", registration)

# Define a regular expression pattern to match the ULD information line
uld_pattern = r'ULD/([A-Z0-9]+)\n(\d+-\d+)(HKG|SVO)([A-Z]+)/(S|P|T)(\d+)K(\d+)MC(\d+)T(\d+)/(.+?)\n/(SPX|ELI/SPX)?'

# Match ULD information
matches = re.finditer(uld_pattern, message)

for match in matches:

    uld_number, awb, route_from, route_to, pieces_type, numeric_pieces, kilos, cubic_meter, last_pics, goods, special_handling = match.groups()
    print("Flight Number:", flight)
    print("Date:", date)
    print("IATA From:", iata)
    print("Registration Number:", registration)
    print("ULD Number:", uld_number)
    print("AWB:", awb)
    print("Route From:", route_from)
    print("Route To:", route_to)
    # Combine the pieces type and numeric part
    print("Pieces Type:", pieces_type + numeric_pieces)
    print("Kilos:", kilos)
    print("Cubic Meter:", cubic_meter)
    print("Last Pics:", last_pics)
    print("Goods:", goods)

    if special_handling:
        print("Special Handling Code:", special_handling)

    print("---")

# Create Shipment instances for each match
shipments = []
for match in matches:
    uld_number, awb, route_from, route_to, pieces_type, numeric_pieces, kilos, cubic_meter, last_pics, goods, special_handling = match.groups()

    # Create a new Shipment instance
    shipment = Shipment(
        version=version,
        flight_number=flight,
        date=datetime.strptime(date, '%d%b%Y%H%M'),
        iata=iata,
        registration_number=registration,
        uld_number=uld_number,
        awb=awb,
        route_from=route_from,
        route_to=route_to,
        pieces_type=pieces_type + numeric_pieces,
        kilos=int(kilos),
        cubic_meter=int(cubic_meter),
        last_pics=int(last_pics),
        goods=goods,
        special_handling_code=special_handling,
        message=message  # Store the entire message if needed
    )

    # Append the created instance to the list
    shipments.append(shipment)

# Bulk insert the shipments into the database
Shipment.objects.bulk_create(shipments)