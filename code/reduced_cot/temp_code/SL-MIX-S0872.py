import re
from functools import reduce

def calculate_entropy(hex_string):
    return sum(int(c, 16) for c in hex_string) % 10

def is_suspicious_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

firewall_logs = [
    "192.168.1.100: CONNECTED - HEX_PAYLOAD: a3f2c1",
    "10.0.0.5: BLOCKED - HEX_PAYLOAD: deadbeef",
    "172.16.0.25: SUSPICIOUS - HEX_PAYLOAD: cafebabe",
    "INVALID_LOG_ENTRY",
    "192.168.1.1: CONNECTED - HEX_PAYLOAD: 1a2b3c",
    "203.0.113.5: ALERT - HEX_PAYLOAD: 9f8e7d"
]

payload_hashes = [re.search(r'HEX_PAYLOAD: ([0-9a-f]+)', log).group(1) for log in firewall_logs if re.search(r'HEX_PAYLOAD: ([0-9a-f]+)', log)]
suspicious_ips = [log.split(':')[0] for log in firewall_logs if 'SUSPICIOUS' in log or 'ALERT' in log]
valid_suspicious_ips = list(filter(is_suspicious_ip, suspicious_ips))

entropy_scores = list(map(calculate_entropy, payload_hashes))
threat_indicators = [(1 if ip.endswith('5') else 0) for ip in valid_suspicious_ips]
combined_score = reduce(lambda x, y: x + y, entropy_scores, 0) if entropy_scores else 0
ip_threat_factor = reduce(lambda acc, indicator: acc + (indicator * 3), threat_indicators, 0) if threat_indicators else 0

is_high_risk = len(valid_suspicious_ips) > 1 and combined_score > 15
aggregated_threat_level = (combined_score + ip_threat_factor) * (2 if is_high_risk else 1) if valid_suspicious_ips or payload_hashes else 0

print(f"Result: {aggregated_threat_level}")