import re
from dataclasses import dataclass
from typing import List

@dataclass
class Packet:
    flags: int
    payload: str
    size: int

packets = [
    Packet(0b10101010, "GET /admin.php HTTP/1.1", 128),
    Packet(0b11110000, "POST /login SQL_INJECTION_ATTEMPT", 256),
    Packet(0b00001111, "Normal user traffic data", 64),
    Packet(0b10100101, "EXEC xp_cmdshell -- dangerous", 512)
]

# Suspicious flag patterns (SYN+URG+PSH)
suspicious_flags = 0b10100000

# Malicious signature patterns
malicious_patterns = [
    r'SQL_INJECTION',
    r'xp_cmdshell',
    r'/admin\.[a-z]{3}'
]

intrusion_score = 0

for packet in packets:
    # Check if suspicious flags are set (bitwise AND)
    if packet.flags & suspicious_flags == suspicious_flags:
        intrusion_score += 10
    
    # Check for small packets with suspicious flags (potential scanning)
    if packet.size < 100 and (packet.flags & 0b10000000):
        intrusion_score += 5
    
    # Scan payload for malicious patterns
    pattern_matches = sum(1 for pattern in malicious_patterns if re.search(pattern, packet.payload))
    
    # Weight pattern matches by packet size (larger payloads with bad content are worse)
    intrusion_score += pattern_matches * (packet.size // 64)
    
    # Additional penalty for packets with both high flags and malicious content
    if (packet.flags & 0b11000000) and pattern_matches > 0:
        intrusion_score += 15

# Final adjustment - if total score is high, apply exponential penalty
if intrusion_score > 30:
    intrusion_score = int(intrusion_score * 1.5)

print(f"Result: {intrusion_score}")