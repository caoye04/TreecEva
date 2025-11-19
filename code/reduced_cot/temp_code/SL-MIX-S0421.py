import re
from functools import reduce

def decode_header_segment(segment):
    decoded_bytes = []
    for i in range(0, len(segment), 2):
        byte_val = int(segment[i:i+2], 16)
        decoded_bytes.append((byte_val ^ 0x5C) % 251)
    return decoded_bytes

packet_headers = ['A1B2C3D4', 'FFEECCBB', '00112233']
threat_patterns = {'malware_sig': [178, 202, 234], 'intrusion_sig': [120, 135, 150]}
threat_index = 0

for header in packet_headers:
    bytes_data = decode_header_segment(header)
    matched_sigs = []
    
    for sig_name, sig_pattern in threat_patterns.items():
        match_count = sum(b == p for b, p in zip(bytes_data, sig_pattern))
        if match_count >= 2:
            matched_sigs.append(sig_name)
    
    if matched_sigs:
        sig_weights = {'malware_sig': 5, 'intrusion_sig': 3}
        weight_sum = sum(sig_weights[sig] for sig in matched_sigs if sig in sig_weights)
        threat_index += weight_sum * (bytes_data[0] & 0x0F)
    else:
        threat_index -= 1

# Adjust final index with a normalization factor
normalization_map = {0: 1, 1: 2, 2: 3, 3: 5, 4: 7}
normalization_key = threat_index % 5
if normalization_key in normalization_map:
    threat_index = threat_index // normalization_map[normalization_key]
else:
    threat_index = 0

print(f"Result: {threat_index}")