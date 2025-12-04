def analyze_packet_headers(headers, filter_criteria=None):
    # Analyze packet headers for potential security issues
    risk_score = 0
    suspicious_ports = {22: 'SSH', 23: 'Telnet', 3389: 'RDP', 445: 'SMB'}
    
    for header in headers:
        if header.get('port') in suspicious_ports:
            risk_score += 10
        if header.get('encrypted') == False:
            risk_score += 15
    
    # This filtering is never used in our calculation
    if filter_criteria:
        filtered_headers = [h for h in headers if filter_criteria(h)]
        risk_score = len(filtered_headers) * 5
    
    return risk_score / max(1, len(headers))

def optimize_routing(nodes, paths):
    # Optimize network routing - unused function
    best_path = None
    min_latency = float('inf')
    
    for path in paths:
        latency = sum(path.get('delay', 0) for _ in range(len(nodes)))
        if latency < min_latency:
            min_latency = latency
            best_path = path
    
    return best_path

def calculate_priority(traffic, protocols):
    # Calculate priority value for network traffic processing
    base_value = 0
    multiplier = 1
    threshold = 75
    
    # Process different protocols with varying weights
    protocol_weights = {'HTTP': 1, 'HTTPS': 2, 'FTP': 3, 'DNS': 4, 'SMTP': 2}
    
    # Misleading intermediate calculation
    potential_priority = sum(protocol_weights.get(p, 0) * 5 for p in protocols)
    
    # Calculate traffic metrics
    total_packets = sum(t.get('packets', 0) for t in traffic)
    dropped_packets = sum(t.get('dropped', 0) for t in traffic)
    
    # Calculate packet loss percentage (0-100)
    packet_loss = (dropped_packets / total_packets * 100) if total_packets > 0 else 0
    
    # Misleading calculation that's never used
    traffic_score = total_packets - (dropped_packets * 3)
    
    # Adjust multiplier based on packet loss
    if packet_loss > 5:
        multiplier = 2
    if packet_loss > 15:
        multiplier = 3
    
    # Base value calculation from active protocols
    for protocol in protocols:
        weight = protocol_weights.get(protocol, 1)
        base_value += weight
        
        # Special case for DNS protocol
        if protocol == 'DNS':
            base_value *= 2
    
    # Apply threshold modulation
    if base_value > threshold:
        base_value = threshold + ((base_value - threshold) // 2)
    
    # Apply multiplier from packet loss
    result = base_value * multiplier
    
    # Final priority value (modulo 100 to keep in reasonable range)
    return result % 100

# Network traffic data
network_traffic = [
    {'packets': 1200, 'dropped': 60, 'protocol': 'HTTP'},
    {'packets': 800, 'dropped': 40, 'protocol': 'HTTPS'},
    {'packets': 400, 'dropped': 100, 'protocol': 'FTP'}
]

# Active protocols in the network
active_protocols = ['HTTP', 'HTTPS', 'DNS', 'FTP']

# Misleading security scan results
security_scan = {
    'vulnerabilities': 12,
    'patched': 8,
    'critical': 3
}

# Calculate network reliability score - not used in final result
reliability = 100 - (sum(t.get('dropped', 0) for t in network_traffic) / 
                    sum(t.get('packets', 0) for t in network_traffic) * 100)

# Analyze headers - not used in final result
packet_headers = [
    {'port': 80, 'encrypted': False},
    {'port': 443, 'encrypted': True},
    {'port': 22, 'encrypted': True}
]
risk_level = analyze_packet_headers(packet_headers)

# Calculate priority value for traffic processing
priority_value = calculate_priority(network_traffic, active_protocols)

# Apply security adjustment - not used in final calculation
adjusted_priority = priority_value + (security_scan['critical'] * 5)

print(f"Network reliability: {reliability:.2f}%")
print(f"Security risk level: {risk_level:.2f}")
print(f"Priority value: {priority_value}")
