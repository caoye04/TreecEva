import re
from functools import reduce

def packet_threat_level(flags, payload):
    # Bitwise analysis of TCP flags
    syn_flag = (flags & 0x02) != 0
    fin_flag = (flags & 0x01) != 0
    rst_flag = (flags & 0x04) != 0
    
    # Pattern matching in payload
    sql_injection_pattern = bool(re.search(r'(UNION|SELECT|DROP).*', payload))
    shellcode_pattern = bool(re.search(r'[\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f]', payload))
    
    # Threat calculation using logical operations
    flag_anomaly = syn_flag and fin_flag and not rst_flag
    payload_threat = sql_injection_pattern or shellcode_pattern
    
    return (flag_anomaly << 2) | (payload_threat << 1) | (len(payload) > 100)

# Network packet data
packets = [
    {'flags': 0x12, 'payload': 'GET /index.html'},
    {'flags': 0x13, 'payload': 'SELECT * FROM users; DROP TABLE logs;'},
    {'flags': 0x06, 'payload': 'Normal traffic pattern'},
    {'flags': 0x17, 'payload': '\x90\x90\x90\x90\x90\x90\x90\x90' + 'A' * 92}
]

# Packet processing pipeline with dictionary comprehension
threat_scores = {i: packet_threat_level(pkt['flags'], pkt['payload']) for i, pkt in enumerate(packets)}

# Advanced filtering based on composite conditions
suspicious_packets = {k: v for k, v in threat_scores.items() if v > 2 and (v & 0x04) != 0}

# Calculate weighted intrusion score
base_score = sum(suspicious_packets.values())
weight_factor = len([p for p in packets if re.search(r'[A-Z]{4,}', p['payload'])])

# Final intrusion calculation with logical operations
intrusion_conditions = [
    base_score > 10,
    weight_factor >= 2,
    len(suspicious_packets) > 1
]

intrusion_score = base_score
if all(intrusion_conditions):
    intrusion_score *= 3
elif any(intrusion_conditions):
    intrusion_score *= 2
else:
    intrusion_score //= 2

print(f"Result: {intrusion_score}")