import re
from collections import Counter
import math

def decode_telemetry(hex_string):
    # Remove hex prefix if present
    clean_hex = re.sub(r'^0x', '', hex_string)
    # Convert hex to integer
    value = int(clean_hex, 16)
    # Apply decoding formula: (value^3) mod 1009
    decoded = pow(value, 3, 1009)
    return decoded

# Telemetry readings
readings = ['0xFF', '0x1A2B', '0x3C4D', '0x5E6F']

# Process readings
processed_values = []
for reading in readings:
    decoded_val = decode_telemetry(reading)
    processed_values.append(decoded_val)

# Calculate checksum using Counter
freq_counter = Counter(processed_values)
checksum_components = []
for val, count in freq_counter.items():
    # For each unique value, add (value * log(count)) to checksum
    if count > 0:
        component = val * math.log(count)
        checksum_components.append(int(component))

checksum_result = sum(checksum_components) % 1000000
print(f"Result: {checksum_result}")