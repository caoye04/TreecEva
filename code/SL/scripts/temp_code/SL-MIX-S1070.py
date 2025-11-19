import re
from collections import defaultdict, Counter

def calculate_packet_threat(header_data):
    score = 0
    protocol = header_data.get('protocol', '').lower()
    src_port = header_data.get('src_port', 0)
    dst_ip = header_data.get('dst_ip', '')
    payload = header_data.get('payload', '')
    
    # Protocol scoring
    if protocol == 'tcp':
        score += 5
    elif protocol == 'udp':
        score += 3
    elif protocol == 'icmp':
        score += 7
    
    # Port-based scoring with early return
    if src_port > 1024:
        if src_port % 2 == 0:
            score += 2
        else:
            return score  # Early return for odd high ports
    elif 20 <= src_port <= 25:
        score += 10
    
    # Destination IP class scoring
    ip_parts = dst_ip.split('.')
    if len(ip_parts) == 4:
        first_octet = int(ip_parts[0])
        if 224 <= first_octet <= 239:  # Multicast
            score += 8
        elif first_octet == 10 or first_octet == 127:  # Private or loopback
            score += 1
    
    # Payload analysis with regex
    suspicious_patterns = [
        r'\b(?:exec|eval|system)\s*\(',
        r'\bselect\s+[*]\s+from\s+\w+',
        r'\bunion\s+select\b'
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, payload, re.IGNORECASE):
            score += 15
            break
    
    # Payload size scoring
    if len(payload) > 1000:
        score += 5
    
    return score

# Packet stream analysis
packet_headers = [
    {'protocol': 'TCP', 'src_port': 80, 'dst_ip': '192.168.1.100', 'payload': 'GET /index.html'},
    {'protocol': 'UDP', 'src_port': 53, 'dst_ip': '10.0.0.1', 'payload': 'DNS query response'},
    {'protocol': 'TCP', 'src_port': 4444, 'dst_ip': '225.10.20.30', 'payload': 'exec(suspicious_code)'},
    {'protocol': 'ICMP', 'src_port': 0, 'dst_ip': '127.0.0.1', 'payload': 'ping request'},
    {'protocol': 'TCP', 'src_port': 22, 'dst_ip': '200.50.30.40', 'payload': 'SSH connection'}
]

# Initialize threat tracking
threat_scores = defaultdict(int)
protocol_counter = Counter()

# Process packets
for i, header in enumerate(packet_headers):
    packet_score = calculate_packet_threat(header)
    threat_scores[i] = packet_score
    protocol_counter[header['protocol'].upper()] += 1

# Calculate final threat score
final_threat_score = 0
for idx, score in threat_scores.items():
    protocol = packet_headers[idx]['protocol'].upper()
    # Apply protocol frequency multiplier
    multiplier = 1.0
    if protocol_counter[protocol] > 1:
        multiplier = 1.5
    
    adjusted_score = int(score * multiplier)
    final_threat_score += adjusted_score
    
    # Early termination condition
    if final_threat_score > 50:
        final_threat_score -= 10
        break

print(f"Result: {final_threat_score}")