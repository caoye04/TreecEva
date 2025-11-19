import hashlib
from collections import defaultdict

def encode_header(header_str):
    return hashlib.sha256(header_str.encode()).hexdigest()[:8]

def decode_header(encoded_str):
    return int(encoded_str, 16)

packet_headers = [
    "SRC:192.168.1.1|DST:10.0.0.1|PORT:8080",
    "SRC:192.168.1.2|DST:10.0.0.2|PORT:80",
    "SRC:192.168.1.3|DST:10.0.0.3|PORT:443",
    "SRC:192.168.1.4|DST:10.0.0.4|PORT:22"
]

encoded_packets = [encode_header(header) for header in packet_headers]

decoded_values = [decode_header(packet) for packet in encoded_packets]

threshold_map = defaultdict(lambda: 0x10000000)
threshold_map['high_risk'] = 0x50000000
threshold_map['medium_risk'] = 0x30000000

anomaly_score = 0
for value in decoded_values:
    risk_level = 'high_risk' if value > threshold_map['high_risk'] else \
                 'medium_risk' if value > threshold_map['medium_risk'] else 'low_risk'
    
    is_suspicious = (value & 0xF0000000) != 0
    weight = 3 if risk_level == 'high_risk' else (2 if risk_level == 'medium_risk' else 1)
    
    anomaly_score += weight if is_suspicious else 0

anomaly_score = anomaly_score if anomaly_score > 0 else -1
print(f"Result: {anomaly_score}")