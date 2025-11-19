import re
from collections import defaultdict

def calculate_modular_hash(packet_header):
    hash_val = 0
    for char in packet_header:
        hash_val = (hash_val * 31 + ord(char)) % 1000007
    return hash_val

def compute_threat_level(signature_freq, hash_val):
    base_score = hash_val % 100
    if signature_freq[hash_val] > 2:
        return (base_score * 3) % 100
    elif signature_freq[hash_val] == 2:
        return (base_score * 2) % 100
    else:
        return base_score

packet_headers = [
    "SRC:192.168.1.1|DST:10.0.0.1|PROTO:TCP|PORT:80",
    "SRC:192.168.1.2|DST:10.0.0.2|PROTO:UDP|PORT:53",
    "SRC:192.168.1.1|DST:10.0.0.1|PROTO:TCP|PORT:80",
    "SRC:172.16.0.1|DST:10.0.0.3|PROTO:ICMP|PORT:0",
    "SRC:192.168.1.1|DST:10.0.0.1|PROTO:TCP|PORT:80",
    "SRC:172.16.0.2|DST:10.0.0.4|PROTO:TCP|PORT:443"
]

signature_frequency = defaultdict(int)
cumulative_risk_score = 0

for header in packet_headers:
    # Extract protocol and port using regex
    proto_match = re.search(r'PROTO:(\w+)', header)
    port_match = re.search(r'PORT:(\d+)', header)
    
    if proto_match and port_match:
        protocol = proto_match.group(1)
        port = int(port_match.group(1))
        
        # Create a signature from header parts
        signature = f"{protocol}:{port}"
        hash_signature = calculate_modular_hash(signature)
        
        # Update frequency
        signature_frequency[hash_signature] += 1
        
        # Calculate threat level
        threat = compute_threat_level(signature_frequency, hash_signature)
        cumulative_risk_score = (cumulative_risk_score + threat) % 1000

print(f"Result: {cumulative_risk_score}")