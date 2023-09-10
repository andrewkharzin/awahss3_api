import re
import json
from datetime import datetime
# from django.utils.timezone import make_aware

# Define a test message
test_message = """
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


def parse_custom_date(date_str):
    if date_str is None:
        return None
    # Define a mapping of month abbreviations to their numeric representation
    month_abbr_to_num = {
        'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
        'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
    }
    # Extract the date portion from the message
    # date_str = date_str[6:15]

    # Split the input date string into day, month abbreviation, and year
    day, month_abbr, year_time = date_str[:2], date_str[2:5], date_str[6:15]

    # Get the numeric representation of the month abbreviation
    month_num = month_abbr_to_num.get(month_abbr)

    if not month_num:
        raise ValueError(f"Invalid month abbreviation: {month_abbr}")

    # Get the current year
    current_year = datetime.now().year

    # Combine the extracted components into the desired format
    formatted_date = f"{current_year}-{month_num}-{day} {year_time[:2]}:{year_time[2:4]}:00"

    return formatted_date


def parse_message(message):

    # Define a regular expression pattern to match the header with the MULTILINE flag
    header_pattern = r'^FFM/\d+\n(\d+)/([A-Z0-9]+)/(\d{2}[A-Z]{3}\d{4})/([A-Z]+)/([A-Z0-9]+)\n'

    # Match the header information
    header_match = re.search(header_pattern, message, re.MULTILINE)

    if header_match:
        version, flight, date, iata, registration = header_match.groups()
    else:
        version, flight, date, iata, registration = None, None, None, None, None

    # Define a regular expression pattern to match the ULD information line
    uld_pattern = r'ULD/([A-Z0-9]+)\n(\d+-\d+)(HKG|SVO)([A-Z]+)/(S|P|T)(\d+)K(\d+)MC(\d+)T(\d+)/(.+?)\n/(SPX|ELI/SPX)?'

    # Match ULD information
    matches = re.finditer(uld_pattern, message)

    date = parse_custom_date(date)
    parsed_data_list = []

    for match in matches:
        uld_number, awb, route_from, route_to, pieces_type, numeric_pieces, kilos, cubic_meter, last_pics, goods, special_handling = match.groups()

        parsed_data_list.append({
            'version': version,
            'flight_number': flight,
            'date': date,
            'iata': iata,
            'registration_number': registration,
            'uld_number': uld_number,
            'awb': awb,
            'route_from': route_from,
            'route_to': route_to,
            'pieces_type': pieces_type + numeric_pieces,
            'kilos': int(kilos),
            'cubic_meter': int(cubic_meter),
            'last_pics': int(last_pics),
            'goods': goods,
            'special_handling_code': special_handling if special_handling else None,
        })

        # Append the parsed data to the list
        # parsed_data_list.append(parsed_data_list)

    # Convert the parsed data list to JSON format
    parsed_data_json = json.dumps(parsed_data_list)

    return parsed_data_json


# Call the parse_message function with the test message
parsed_data_json = parse_message(test_message)

# Print the parsed data (as JSON)
print(parsed_data_json)
