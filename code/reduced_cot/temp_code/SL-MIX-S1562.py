import re
from functools import reduce
from collections import namedtuple

Packet = namedtuple('Packet', ['src_port', 'dst_port', 'flags'])

packets = [
    Packet(22, 54321, 'SYN'),
    Packet(80, 45678, 'ACK'),
    Packet(443, 12345, 'SYN|ACK'),
    Packet(21, 55555, 'FIN'),
    Packet(23, 33333, 'RST')
]

intrusion_score = 0

for pkt in packets:
    # Check for suspicious source ports (well-known ports < 1024 used as source)
    if pkt.src_port < 1024 and pkt.dst_port > 32768:
        intrusion_score += 5
    
    # Check for SYN flood pattern
    if 'SYN' in pkt.flags and not 'ACK' in pkt.flags:
        intrusion_score += 3
    
    # Check for port scanning (multiple connections to different high ports)
    if pkt.dst_port > 32768:
        intrusion_score += 1
    
    # Early return if score exceeds threshold
    if intrusion_score > 15:
        intrusion_score *= 2
        break

# Apply regex pattern matching on flag combinations
flag_patterns = [pkt.flags for pkt in packets]
syn_ack_count = len([f for f in flag_patterns if re.match(r'SYN\|ACK|ACK\|SYN', f)])
intrusion_score += syn_ack_count * 2

# Final adjustment using functional programming
adjustments = list(map(lambda x: x % 3, [pkt.src_port for pkt in packets]))
final_intrusion_score = reduce(lambda acc, val: acc + val, adjustments, intrusion_score)

print(f'Result: {final_intrusion_score}')