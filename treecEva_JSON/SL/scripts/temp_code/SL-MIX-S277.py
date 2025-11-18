import re
from collections import defaultdict

def calculate_octet_score(octet):
    binary_repr = bin(int(octet))[2:].zfill(8)
    xor_result = 0
    for i, bit in enumerate(binary_repr):
        if i % 2 == 0:
            xor_result ^= int(bit)
    return (int(octet) * 3 + xor_result) % 256

def process_log_entries(log_data):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    threat_scores = defaultdict(int)
    
    for entry in log_data:
        ips = re.findall(ip_pattern, entry)
        for ip in ips:
            octets = ip.split('.')
            ip_score = 0
            for i, octet in enumerate(octets):
                if int(octet) > 127 and i < 3:
                    ip_score += calculate_octet_score(octet) << (i*2)
                else:
                    ip_score += calculate_octet_score(octet)
            threat_scores[ip] = max(threat_scores[ip], ip_score)
    
    total_threat_level = 0
    suspicious_ips = frozenset({ip for ip, score in threat_scores.items() if score > 1000})
    
    for ip in suspicious_ips:
        octets = ip.split('.')
        adjustment = sum(int(octet) for octet in octets if int(octet) % 2 == 0)
        total_threat_level += threat_scores[ip] - adjustment
    
    return total_threat_level

network_logs = [
    "Authentication failed from 192.168.1.105 at 14:32:10",
    "Connection established to 203.0.113.195 on port 443",
    "Suspicious activity detected from 198.51.100.17 at 14:32:15",
    "Firewall blocked request from 192.0.2.200 at 14:32:20",
    "Multiple login attempts from 203.0.113.195 and 198.51.100.17"
]

final_security_metric = process_log_entries(network_logs)
print(f"Result: {final_security_metric}")