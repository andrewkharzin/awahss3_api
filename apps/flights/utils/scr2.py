import re

def parse_message(message):
    # Define a regex pattern to match the message format
    pattern = r'([A-Z]+\d+)\s+(\d+[A-Z]+\d+)\s+(\d+)\s+([A-Z0-9]+)\s+([A-Z]+[A-Z0-9]+)\s+([A-Z])\s+/[A-Z]+\s+([A-Z.]+\d+)/'

    match = re.match(pattern, message)
    
    if match:
        groups = match.groups()
        parsed_data = {
            'Identifier': groups[0],
            'Date Range': groups[1],
            'Time or Duration': groups[2],
            'Identifier 2': groups[3],
            'Details': groups[4],
            'Status or Type': groups[5],
            'Reference': groups[6]
        }
        return parsed_data
    else:
        return None

# Example usage:
message = "KVI7162 12SEP12SEP 0200000 000A4F DWCKRW0900 H / TA.B RE.82081/"
parsed_data = parse_message(message)
if parsed_data:
    print(parsed_data)
else:
    print("Message format doesn't match the expected pattern.")
