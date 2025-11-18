import itertools

# Connection log data for a specific IP
connection_logs = [
    {'port': 22, 'protocol': 'TCP'},
    {'port': 80, 'protocol': 'TCP'},
    {'port': 443, 'protocol': 'TCP'},
    {'port': 21, 'protocol': 'TCP'},
    {'port': 25, 'protocol': 'TCP'},
    {'port': 5000, 'protocol': 'TCP'},
    {'port': 8080, 'protocol': 'UDP'},
    {'port': 12345, 'protocol': 'ICMP'},
]

# Well-known ports
well_known_ports = frozenset([20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995])

# Initialize threat score
threat_score = 0

# Extract ports and protocols
connected_ports = list(map(lambda conn: conn['port'], connection_logs))
protocols_used = list(map(lambda conn: conn['protocol'], connection_logs))

# Count connections to well-known ports
well_known_connections = len(list(filter(lambda port: port in well_known_ports, connected_ports)))

# Count unique ports
unique_ports = len(set(connected_ports))

# Check for suspicious behavior
if well_known_connections > 3 and unique_ports > 5:
    threat_score += 10

# Check for uncommon protocols
uncommon_protocols = ['ICMP', 'GRE', 'ESP', 'AH']
has_uncommon_protocol = any(protocol in uncommon_protocols for protocol in protocols_used)

if has_uncommon_protocol:
    threat_score += 5

# Additional check: if more than 7 unique ports with at least one uncommon protocol
if unique_ports > 7 and has_uncommon_protocol:
    threat_score += 3

print(f"Result: {threat_score}")