import re
from collections import deque

def base36_decode(encoded_str):
    return int(encoded_str, 36)

def extract_location_codes(log_entry):
    # Pattern matches base-36 strings of exactly 4 characters
    pattern = r'\b([0-9A-Z]{4})\b'
    return re.findall(pattern, log_entry)

# Simulated log entries with encoded location data
log_entries = [
    "IN: Z9A1 OUT: 1K2L",
    "IN: 3M4N TEMP: B5C6 OUT: D7E8",
    "IN: F9G0 H1J2 OUT: K3L4 M5N6"
]

# Initialize inventory tracking structures
incoming_stack = []
outgoing_queue = deque()
location_inventory = {}

# Process each log entry
for entry in log_entries:
    codes = extract_location_codes(entry)
    for code in codes:
        decoded_value = base36_decode(code)
        # Even values go to incoming, odd to outgoing
        if decoded_value % 2 == 0:
            incoming_stack.append(decoded_value)
        else:
            outgoing_queue.append(decoded_value)

# Location inventory map initialization
location_ids = [base36_decode(c) for entry in log_entries for c in extract_location_codes(entry)]
unique_locations = {lid: 0 for lid in set(location_ids)}

# Transfer from incoming stack to location inventory
while incoming_stack:
    item = incoming_stack.pop()
    unique_locations[item] = unique_locations.get(item, 0) + 1

# Process outgoing queue (FIFO)
while outgoing_queue:
    item = outgoing_queue.popleft()
    if item in unique_locations:
        unique_locations[item] = max(0, unique_locations[item] - 1)

# Calculate final inventory as sum of all location counts
final_inventory = sum(unique_locations.values())
print(f"Result: {final_inventory}")