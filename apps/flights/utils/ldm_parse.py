import re

def parse_ldm_text(ldm_text):
    pattern = r'(\w{2})(\d+)/(\d+)\.(\w+)\.(\w+)\.(\d+)/(\d+)'
    match = re.search(pattern, ldm_text)

    if match:
        iata_code, flight_number, date, ac_reg_number, index1, index2, number2 = match.groups()

        parsed_data = {
            'iata_code': iata_code,
            'flight_number': flight_number,
            'date': date,
            'ac_reg_number': ac_reg_number,
            'index1': index1,
            'index2': index2,
            'number2': number2,
        }
        print("Parsed Data:", parsed_data)  # Print the parsed data
        return parsed_data

    return None

# Simplae LDM work

# def parse_ldm_text(ldm_text):
#     pattern = r'(\w+)/(\d+)\.(\w+)\.(\w+)\.\d+/(\d+)'
#     match = re.search(pattern, ldm_text)

#     if match:
#         code, flight_number, ac_reg_number, index, number2 = match.groups()

#         parsed_data = {
#             'code': code,
#             'flight_number': flight_number,
#             'ac_reg_number': ac_reg_number,
#         }
#         print("Parsed Data:", parsed_data)  # Print the parsed data
#         return parsed_data

#     return None



# Complex LDM not work

# def parse_ldm_text(ldm_text):
#     pattern = r'(\w+)/(\d+)([A-Z]+)(\d+)\.(\w+)\.(\w+)\.(\w+)\.\d+/(\d+)'
#     match = re.search(pattern, ldm_text)

#     if match:
#         code, number, month, day, ac_reg_number, index1, index2, index3, number2 = match.groups()

#         parsed_data = {
#             'ac_reg_number': ac_reg_number,
#         }
#         print("Parsed Data:", parsed_data)  # Print the parsed data
#         return parsed_data

#     return None



# Modified not work
# import re
# from datetime import datetime

# def parse_ldm_text(ldm_text):
#     pattern = r'(\w{2})(\d{4})/(\d{2})(\d{2})'
#     match = re.search(pattern, ldm_text)

#     if match:
#         code, flight_number, month, day = match.groups()

#         # Get the current year and month
#         current_year = datetime.now().year
#         current_month = datetime.now().month

#         # Convert month and day to integers
#         month = int(month)
#         day = int(day)

#         # Adjust year and month if necessary
#         if month > current_month:
#             current_year -= 1

#         parsed_data = {
#             'code': code,
#             'flight_number': flight_number,
#             'date': f'{current_year}-{month:02d}-{day:02d}',
#         }
#         print("Parsed Data:", parsed_data)
#         return parsed_data

#     return None
