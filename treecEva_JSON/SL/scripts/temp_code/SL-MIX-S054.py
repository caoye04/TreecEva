import re
from collections import defaultdict

class PacketHeader:
    def __init__(self, source_ip, dest_ip, flags):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.flags = flags

packet_data = [
    "192.168.1.10:10.0.0.5:SYN",
    "10.0.0.5:192.168.1.10:SYN-ACK",
    "192.168.1.10:10.0.0.5:PSH-ACK|URG",  # Suspicious: URG flag
    "192.168.1.15:10.0.0.5:FIN",           # Suspicious: unexpected FIN
    "192.168.1.10:10.0.0.5:ACK"
]

flag_counter = defaultdict(int)
suspicious_patterns = [r'URG', r'FIN']
suspicious_score = 0

for entry in packet_data:
    parts = entry.split(':')
    if len(parts) == 3:
        src, dst, flag_str = parts
        flags = flag_str.split('|')
        header = PacketHeader(src, dst, flags)
        
        # Count flags
        for f in header.flags:
            flag_counter[f] += 1
        
        # Pattern check with short-circuit: only check if TCP handshake flags aren't dominant
        is_not_handshake_dominant = not (flag_counter['SYN'] > 2 and flag_counter['ACK'] > 2)
        has_suspicious_flag = any(re.search(pattern, flag_str) for pattern in suspicious_patterns)
        
        if is_not_handshake_dominant and has_suspicious_flag:
            suspicious_score += 10
        elif not is_not_handshake_dominant or not has_suspicious_flag:
            suspicious_score -= 1  # Decrease score for normal traffic

# Final adjustment based on flag distribution
if flag_counter['RST'] > 0:
    suspicious_score += 15

print(f"Result: {suspicious_score}")