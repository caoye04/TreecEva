from collections import defaultdict
import math

def calculate_entropy(data):
    if not data:
        return 0
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    entropy = 0
    data_len = len(data)
    for freq in frequency.values():
        probability = freq / data_len
        entropy -= probability * math.log2(probability)
    return entropy

def transform_header(header_str):
    transformed = ''
    for i, char in enumerate(header_str):
        if i % 2 == 0:
            transformed += char.upper()
        else:
            transformed += char.lower()
    return transformed[::-1]  # Reverse the string

packet_headers = [
    "src=192.168.1.1;dst=10.0.0.1;port=80",
    "src=172.16.0.1;dst=192.168.1.100;port=443",
    "src=10.0.0.5;dst=172.16.0.10;port=22",
    "src=192.168.1.50;dst=8.8.8.8;port=53"
]

# Initialize threat scoring system
threat_scores = defaultdict(lambda: 0)
threat_accumulator = 0

for header in packet_headers:
    # Transform header for analysis
    processed_header = transform_header(header)
    
    # Calculate base threat score using entropy
    base_score = int(calculate_entropy(processed_header) * 10)
    
    # Extract port number for additional scoring
    port_str = header.split('port=')[1]
    port_num = int(port_str)
    
    # Apply port-based modifiers
    if port_num in [22, 443]:  # SSH or HTTPS
        port_modifier = 5
    elif port_num == 80:  # HTTP
        port_modifier = 2
    else:  # Other ports
        port_modifier = 1
    
    # Calculate final packet threat score
    packet_score = base_score + (port_modifier * 3)
    
    # Update accumulator with weighted score
    threat_accumulator += packet_score * len(header) // 10

# Apply final adjustment based on total packets processed
final_adjustment = (len(packet_headers) ** 2) & 0xF  # Bitwise AND with 15
threat_accumulator ^= final_adjustment  # XOR with adjustment

print(f"Result: {threat_accumulator}")