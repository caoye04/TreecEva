from collections import defaultdict
import itertools

# Packet header analysis for threat detection
packet_headers = [
    {'proto': 'TCP', 'flags': 0b00010010, 'size': 1420, 'ttl': 64},
    {'proto': 'UDP', 'flags': 0b00000000, 'size': 512, 'ttl': 128},
    {'proto': 'TCP', 'flags': 0b00010001, 'size': 890, 'ttl': 32},
    {'proto': 'ICMP', 'flags': 0b00000000, 'size': 76, 'ttl': 255}
]

# Threat scoring rules
threat_score = 0
protocol_weights = {'TCP': 3, 'UDP': 1, 'ICMP': 2}
flag_danger_bits = 0b00010010  # SYN and URG flags
size_threshold = 1000

# Process each packet
for packet in packet_headers:
    score = 0
    # Protocol weight
    score += protocol_weights.get(packet['proto'], 0)
    
    # Flag analysis - check if any danger bits are set
    if packet['flags'] & flag_danger_bits:
        score += 5
    
    # Size analysis
    if packet['size'] > size_threshold:
        score += 2
    
    # TTL anomaly detection (suspicious if TTL is power of 2 minus 1, common in some scans)
    if packet['ttl'] == 2**5 - 1 or packet['ttl'] == 2**7 - 1 or packet['ttl'] == 2**8 - 1:
        score += 3
    
    threat_score += score

# Additional correlation analysis using itertools
# Check all pairs of packets for suspicious protocol combinations
suspicious_combinations = [('TCP', 'ICMP')]
correlation_penalty = 0

for pkt1, pkt2 in itertools.combinations(packet_headers, 2):
    combo = tuple(sorted([pkt1['proto'], pkt2['proto']]))
    if combo in suspicious_combinations:
        correlation_penalty += 7

# Final aggregation with logical conditions
aggregated_threat_score = 0
if threat_score > 10 and correlation_penalty > 0:
    aggregated_threat_score = threat_score + correlation_penalty
elif threat_score <= 10:
    aggregated_threat_score = threat_score - correlation_penalty
else:
    aggregated_threat_score = threat_score

print(f"Result: {aggregated_threat_score}")