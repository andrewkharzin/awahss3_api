import re
import json
from datetime import datetime

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
"""

def parse_custom_date(date_str):
    if date_str is None:
        return None

    month_abbr_to_num = {
        'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
        'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
    }

    day, month_abbr, year_time = date_str[:2], date_str[2:5], date_str[6:15]
    month_num = month_abbr_to_num.get(month_abbr)

    if not month_num:
        raise ValueError(f"Invalid month abbreviation: {month_abbr}")

    current_year = datetime.now().year
    formatted_date = f"{current_year}-{month_num}-{day} {year_time[:2]}:{year_time[2:4]}:00"
    return formatted_date

def parse_uld_info(uld_info):
    uld_pattern = r'ULD/([A-Z0-9]+)\n(\d+-\d+)(HKG|SVO)([A-Z]+)/(S|P|T)(\d+)K(\d+)MC(\d+)T(\d+)/(.+?)\n/([A-Z/]+)?'
    matches = re.finditer(uld_pattern, uld_info)

    uld_data_list = []

    for match in matches:
        uld_number, awb, route_from, route_to, pieces_type_raw, numeric_pieces, kilos, cubic_meter_raw, last_pics, goods, special_handling = match.groups()
        numeric_part = re.match(r'(\d+)', pieces_type_raw).group(1) if re.match(r'(\d+)', pieces_type_raw) else None
        cubic_meter = f'{float(cubic_meter_raw):.3f}' if cubic_meter_raw else None
        pieces_type = numeric_part if numeric_part else pieces_type_raw

        uld_data_list.append({
            'uld_number': uld_number,
            'awb': awb,
            'route_from': route_from,
            'route_to': route_to,
            'pieces_type': pieces_type,
            'pieces': numeric_pieces,
            'kilos': int(kilos),
            'cubic_meter': cubic_meter,
            'last_pics': int(last_pics),
            'goods': goods,
            'special_handling_code': special_handling if special_handling else None,
        })

    return uld_data_list

def parse_message(text):
    header_pattern = r'^FFM/\d+\n(\d+)/([A-Z0-9]+)/(\d{2}[A-Z]{3}\d{4})/([A-Z]+)/([A-Z0-9]+)\n'
    header_match = re.search(header_pattern, text, re.MULTILINE)

    if header_match:
        version, flight, date, iata, registration = header_match.groups()
    else:
        version, flight, date, iata, registration = None, None, None, None, None

    date = parse_custom_date(date)
    uld_info_pattern = r'ULD/([A-Z0-9]+)\n(.+?)(?=\nULD/|\Z)'
    uld_info_matches = re.finditer(uld_info_pattern, text, re.DOTALL)

    parsed_data_list = []

    for uld_info_match in uld_info_matches:
        uld_number, uld_info = uld_info_match.groups()
        uld_data_list = parse_uld_info(uld_info)

        for uld_data in uld_data_list:
            uld_data.update({
                'version': version,
                'flight_number': flight,
                'date': date,
                'iata': iata,
                'registration_number': registration,
                'uld_number': uld_number,
            })
            parsed_data_list.append(uld_data)

    parsed_data_json = json.dumps(parsed_data_list)
    return parsed_data_json



parsed_data_json = parse_message(test_message)
print(parsed_data_json)
