import re
from collections import defaultdict, Counter

def calculate_port_threat(port_hex):
    port_num = int(port_hex, 16)
    # Bitwise operations to determine threat level
    if port_num & 0x100:  # Check if privileged port (bit 8 set)
        return (port_num >> 4) ^ 0xF0
    else:
        return (port_num & 0xFF) + ((port_num >> 8) & 0x0F)

log_entries = [
    "192.168.1.10 [1F, 2A0, 80, 4C0, 1FF]",
    "10.0.0.5 [1BB, 2C0, 3D0]",
    "172.16.0.3 [ABC, DEF, 123, 456, 789, 101]",
    "192.168.1.20 [5A5, B0B, C0C]"
]

# Parsing logs and initializing data structures
port_access_count = defaultdict(int)
flagged_ips = []

for entry in log_entries:
    match = re.match(r'(\d+\.\d+\.\d+\.\d+) \[(.*)\]', entry)
    if not match:
        continue
    ip_address = match.group(1)
    ports_str = match.group(2)
    # Tokenize port hex values
    ports = [p.strip() for p in ports_str.split(',')]
    
    # Count unique ports
    unique_ports = set(ports)
    for port in unique_ports:
        port_access_count[port] += 1
    
    # Flag IPs accessing more than 3 ports
    if len(ports) > 3:
        flagged_ips.append(ip_address)

# Calculate threat scores using stack-based processing
threat_stack = []
for port, count in port_access_count.items():
    base_threat = calculate_port_threat(port)
    adjusted_threat = base_threat * count
    threat_stack.append(adjusted_threat)

# Apply final aggregation with queue simulation
from collections import deque
threat_queue = deque(threat_stack)
accumulated_threat_score = 0
while threat_queue:
    current_threat = threat_queue.popleft()
    if current_threat & 0x01:  # If odd threat score
        accumulated_threat_score += current_threat << 1  # Double it
    else:
        accumulated_threat_score += current_threat

print(f"Result: {accumulated_threat_score}")
