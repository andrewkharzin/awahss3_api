# Sample message
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
250-91841956HKGSVO/S2K790MC1T51/CABLE FAST LOCK
/SPX
"""

# Split the message into lines
lines = message.split('\n')

# Initialize counters for total ULDs and ULDs by type
total_uld_count = 0
uld_type_count = {}

# Initialize a dictionary to store the extracted data
data = {}
current_uld = None

# Loop through each line and extract the relevant information
for line in lines:
    if line.startswith("1/"):
        data["Flight Number"] = line.split('/')[1]
        data["Departure Date/Time"] = line.split('/')[2]
        data["Departure Airport"] = line.split('/')[3]
        data["Destination Airport"] = line.split('/')[4]
    elif line.startswith("ULD/"):
        uld_data = line.split('/')
        uld_number = uld_data[1]
        uld_info = uld_data[2:]
        current_uld = uld_number
        total_uld_count += 1
        
        # Extract the ULD type (e.g., PAG, PMC, PLA, FQA, AKE, etc.)
        uld_type = uld_number[:3]
        uld_type_count[uld_type] = uld_type_count.get(uld_type, 0) + 1
        
        data[f"ULD {uld_number}"] = {"Shipments": []}
    elif line.startswith("250-"):
        if current_uld is not None:
            data[f"ULD {current_uld}"]["Shipments"].append(line)

# Print the extracted data
for key, value in data.items():
    if isinstance(value, dict):
        print(key + ":")
        for shipment in value["Shipments"]:
            print(shipment)
    else:
        print(f"{key}: {value}")

# Print the ULD count by type
print("Total ULDs:", total_uld_count)
print("ULD Count by Type:")
for uld_type, count in uld_type_count.items():
    print(f"{uld_type}: {count}")
