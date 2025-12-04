import itertools

def analyze_network_packets(packets, threshold=50):
    # Process packet data (irrelevant for final calculation)
    processed = [(p[0] ^ 0xFF, p[1] & 0x3F) for p in packets]
    
    # Extract packet values using bitwise operations
    packet_values = []
    for header, payload in packets:
        # Complex but irrelevant calculation
        integrity = ((header << 2) | (payload >> 4)) & 0xFF
        timestamp = (header & 0x0F) * (payload & 0x0F)
        
        # The actual relevant value we need
        value = (header & 0x3F) - (payload & 0x1F)
        
        # More irrelevant calculations
        checksum = header ^ payload
        routing = (header + payload) % 256
        
        packet_values.append(value)
    
    # Identify critical packets (misleading calculation)
    potential_critical = [i for i, v in enumerate(packet_values) if v > 0]
    
    # Misleading intermediate results
    error_packets = [i for i, (h, p) in enumerate(packets) if (h + p) % 7 == 0]
    high_priority = [i for i, v in enumerate(packet_values) if v > threshold]
    
    # Calculate parity bits (irrelevant)
    parity_map = {i: bin(packets[i][0]).count('1') % 2 for i in range(len(packets))}
    
    # Dead code path
    if False:
        special_indices = [i for i, (par, val) in enumerate(zip(parity_map.values(), packet_values)) 
                          if par == 1 and val < 0]
        critical_indices = special_indices
    else:
        # The actual critical indices we need
        critical_indices = [1, 3, 5]
    
    # More distracting calculations
    for i, j in itertools.product(high_priority, error_packets):
        if i == j:
            packet_values[i] = packet_values[i] * 2
    
    # Calculate various metrics (mostly irrelevant)
    total_value = sum(packet_values)
    avg_value = total_value / len(packet_values) if packet_values else 0
    max_value = max(packet_values) if packet_values else 0
    
    # The key calculation we're looking for
    final_priority = sum([packet_values[i] for i in critical_indices])
    
    # More misleading calculations after the key result
    adjusted_priority = final_priority
    if error_packets:
        adjusted_priority = final_priority ^ len(error_packets)
    
    weighted_priority = final_priority * 0.75 + total_value * 0.25
    
    return {
        'total': total_value,
        'priority': final_priority,
        'adjusted': adjusted_priority,
        'weighted': weighted_priority
    }

# Network packet data: (header, payload)
packet_data = [
    (76, 24),  # Packet 0
    (42, 15),  # Packet 1
    (63, 51),  # Packet 2
    (29, 8),   # Packet 3
    (84, 32),  # Packet 4
    (57, 22)   # Packet 5
]

# Process packets
results = analyze_network_packets(packet_data)

# Print results (including our target value)
print(f"Network statistics:")
print(f"Total packet value: {results['total']}")
print(f"Result: {results['priority']}")