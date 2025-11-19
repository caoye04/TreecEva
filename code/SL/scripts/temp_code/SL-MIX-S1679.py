import re
from functools import reduce
from collections import defaultdict

def compute_custom_checksum(data):
    checksum = 0
    for byte_val in data:
        checksum ^= (byte_val << 3) & 0xFF
        checksum = (checksum >> 1) | ((checksum & 1) << 7)
    return checksum % 256

def extract_protocol_version(header):
    match = re.search(r'PROTO:(\d+)', header)
    return int(match.group(1)) if match else 0

packet_headers = [
    "ID:0x1A|PROTO:4|SIZE:128",
    "ID:0x2B|PROTO:6|SIZE:256",
    "ID:0x3C|PROTO:4|SIZE:512",
    "ID:0x4D|PROTO:6|SIZE:1024"
]

protocol_stats = defaultdict(int)
anomaly_score = 0

for header in packet_headers:
    proto_version = extract_protocol_version(header)
    size_match = re.search(r'SIZE:(\d+)', header)
    packet_size = int(size_match.group(1)) if size_match else 0
    
    # Convert header hex ID to bytes for checksum
    id_hex = re.search(r'ID:(0x[0-9A-F]+)', header).group(1)
    id_bytes = [int(id_hex[i:i+2], 16) for i in range(2, len(id_hex), 2)]
    
    checksum = compute_custom_checksum(id_bytes)
    protocol_stats[proto_version] += 1
    
    # Anomaly detection logic
    if (checksum & 0xF0) != 0 and packet_size > 256:
        anomaly_score |= (1 << proto_version)
    elif checksum % 16 == 0:
        anomaly_score &= ~(1 << proto_version)
    else:
        anomaly_score ^= proto_version
    
    # Apply modular adjustment
    anomaly_score = (anomaly_score * 3 + proto_version) % 128

# Final adjustment based on protocol distribution
if protocol_stats[4] > protocol_stats[6]:
    anomaly_score = (anomaly_score << 2) & 0xFF
else:
    anomaly_score = (anomaly_score >> 1) ^ 0xAA

print(f"Result: {anomaly_score}")