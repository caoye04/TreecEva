def calculate_checksum(data):
    # Calculate a simple checksum for packet validation
    checksum = 0
    for byte in data:
        checksum = (checksum + byte) % 256
    return checksum

def analyze_traffic_pattern(traffic_history):
    # Analyze historical traffic patterns (not used in main logic)
    if not traffic_history:
        return 0
    
    peak_values = [max(day) if day else 0 for day in traffic_history]
    trend = sum(peak_values) / len(peak_values) if peak_values else 0
    return trend * 1.5

def optimize_routing(network_map, source, destination):
    # Simulate network routing optimization (distractor)
    if not network_map or source not in network_map or destination not in network_map:
        return 0
    
    # Simplified distance calculation (not used in main calculation)
    distance = abs(network_map[destination] - network_map[source])
    return distance * 2

def process_network_packets(packets, filters):
    # Process network packets based on priority filters
    valid_packets = {}
    packet_stats = {'high': 0, 'medium': 0, 'low': 0}
    bandwidth_usage = []
    
    # First pass: validate packets and collect initial stats
    for packet_id, packet_data in packets.items():
        if calculate_checksum(packet_data['payload']) != packet_data['checksum']:
            continue  # Invalid checksum, skip this packet
            
        # Track bandwidth for monitoring (not used in final calculation)
        bandwidth_usage.append(len(packet_data['payload']))
        
        # Store valid packets
        valid_packets[packet_id] = packet_data
        priority = packet_data['priority']
        packet_stats[priority] += 1
    
    # Apply priority filters (key to the solution)
    priority_scores = {}
    for packet_id, packet_data in valid_packets.items():
        priority = packet_data['priority']
        if priority in filters:
            base_score = 10 if priority == 'high' else (5 if priority == 'medium' else 1)
            multiplier = filters[priority]
            priority_scores[packet_id] = base_score * multiplier
    
    # Calculate network congestion (distractor)
    congestion_factor = sum(bandwidth_usage) / 1000 if bandwidth_usage else 0
    
    # Apply protocol-specific adjustments (misleading calculations)
    protocol_weights = {'TCP': 1.2, 'UDP': 0.8, 'ICMP': 1.5}
    for packet_id in list(priority_scores.keys()):
        if 'protocol' in valid_packets[packet_id]:
            protocol = valid_packets[packet_id]['protocol']
            if protocol in protocol_weights:
                # This appears important but isn't used in the final calculation
                priority_scores[packet_id] *= protocol_weights[protocol]
    
    # Calculate final priority value
    packet_count = len(valid_packets)
    if packet_count == 0:
        return 0
    
    # The key calculation that determines the answer
    total_score = sum(priority_scores.values())
    weighted_priority = total_score / packet_count
    
    # Misleading adjustments that don't affect the final result
    if congestion_factor > 5:
        weighted_priority = weighted_priority * 0.9
    
    # Convert to integer (this is the actual answer)
    return int(weighted_priority * 10)

# Network simulation data
network_map = {
    'server1': 10,
    'server2': 25,
    'server3': 40,
    'client1': 5,
    'client2': 15
}

# Historical traffic data (not used in main calculation)
traffic_history = [
    [45, 67, 89, 102],
    [56, 78, 90, 110],
    [48, 70, 85, 95]
]

# Packet data with priority, payload, and checksums
packets = {
    'pkt001': {'priority': 'high', 'payload': [65, 66, 67], 'checksum': 198, 'protocol': 'TCP'},
    'pkt002': {'priority': 'medium', 'payload': [68, 69, 70], 'checksum': 207, 'protocol': 'UDP'},
    'pkt003': {'priority': 'low', 'payload': [71, 72, 73], 'checksum': 216, 'protocol': 'TCP'},
    'pkt004': {'priority': 'high', 'payload': [74, 75, 76], 'checksum': 225, 'protocol': 'ICMP'},
    'pkt005': {'priority': 'medium', 'payload': [77, 78, 79], 'checksum': 234, 'protocol': 'UDP'},
    'pkt006': {'priority': 'high', 'payload': [80, 81, 82], 'checksum': 999}  # Invalid checksum
}

# Priority filters (multipliers for each priority level)
priority_filters = {
    'high': 3,
    'medium': 2,
    'low': 1
}

# Calculate optimal route (distractor calculation)
optimal_route = optimize_routing(network_map, 'server1', 'client2')

# Analyze traffic patterns (another distractor)
traffic_trend = analyze_traffic_pattern(traffic_history)

# Process packets and get priority value
priority_value = process_network_packets(packets, priority_filters)

# Print results
print(f"Optimal route value: {optimal_route}")
print(f"Traffic trend: {traffic_trend}")
print(f"Priority value: {priority_value}")
