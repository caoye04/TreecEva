from collections import defaultdict
import itertools

def decode_hex_header(hex_str):
    return int(hex_str, 16)

def compute_checksum(bits):
    checksum = 0
    for b in bits:
        checksum ^= b
    return checksum

def process_packets(packet_headers):
    section_checksums = []
    for i in range(0, len(packet_headers), 4):
        segment = packet_headers[i:i+4]
        decoded_segment = [decode_hex_header(h) for h in segment]
        checksum = compute_checksum(decoded_segment)
        section_checksums.append(checksum)
    return section_checksums

# Simulated packet headers in hex
network_packets = ['1A3F', 'B2C4', 'D5E6', '7890', '1234', '5678', '9ABC', 'DEF0']

with defaultdict(int) as stats:
    section_values = process_packets(network_packets)
    if len(section_values) > 1:
        # Divide and conquer aggregation
        mid = len(section_values) // 2
        left_checksum = compute_checksum(section_values[:mid])
        right_checksum = compute_checksum(section_values[mid:])
        aggregated_checksum = left_checksum ^ right_checksum
    else:
        aggregated_checksum = section_values[0] if section_values else 0

print(f"Result: {aggregated_checksum}")