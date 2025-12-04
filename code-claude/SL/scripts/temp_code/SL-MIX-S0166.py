def calculate_network_priority(packets, traffic_patterns):
    # Network traffic simulation with priority calculation
    routing_table = {"high": 8, "medium": 4, "low": 2, "background": 1}
    congestion_levels = [3, 1, 4, 1, 5, 9]
    dropped_packets = 0
    
    # Process traffic patterns (unused in final calculation)
    pattern_weights = {}
    for i, pattern in enumerate(traffic_patterns):
        pattern_weights[pattern] = (i + 1) * 2
        if "urgent" in pattern:
            pattern_weights[pattern] += 5
    
    # Track active connections (distraction)
    active_connections = 0
    for packet in packets:
        if packet.get("active", False):
            active_connections += 1
    
    # Calculate bit flags for priority determination
    priority_flags = 0
    for i, packet in enumerate(packets):
        priority = packet.get("priority", "low")
        size = packet.get("size", 0)
        
        # Set bits based on packet properties
        if priority == "high":
            priority_flags |= (1 << 3)
        elif priority == "medium":
            priority_flags |= (1 << 2)
        elif size > 1000:
            priority_flags |= (1 << 1)
        else:
            priority_flags |= 1
    
    # Process congestion (misleading calculation)
    congestion_factor = sum(congestion_levels) / len(congestion_levels)
    adjusted_congestion = int(congestion_factor * 2)
    
    # Extract bit values from priority flags
    bit_values = []
    temp_flags = priority_flags
    position = 0
    while temp_flags > 0:
        if temp_flags & 1:
            bit_values.append(position)
        temp_flags >>= 1
        position += 1
    
    # Calculate theoretical throughput (distraction)
    throughput = 0
    for i, level in enumerate(congestion_levels):
        throughput += (10 - level) * (i + 1)
        if level > 5:
            dropped_packets += level - 5
    
    # Calculate network efficiency (unused)
    if active_connections > 0:
        efficiency = (throughput / active_connections) * (1 - (dropped_packets / 20))
    else:
        efficiency = 0
    
    # Calculate final priority index
    priority_index = sum(bit_values)
    
    # Misleading adjustment that doesn't get used
    adjusted_index = priority_index * (1 + (dropped_packets / 10))
    
    print(f"Network metrics - Throughput: {throughput}, Efficiency: {efficiency:.2f}")
    print(f"Priority flags: {bin(priority_flags)}, Dropped: {dropped_packets}")
    print(f"Result: {priority_index}")
    
    return priority_index

# Test data
packets = [
    {"priority": "high", "size": 512, "active": True},
    {"priority": "low", "size": 1024, "active": True},
    {"priority": "medium", "size": 2048, "active": False}
]

traffic_patterns = ["periodic", "burst", "urgent_voice", "streaming"]

# Execute function
result = calculate_network_priority(packets, traffic_patterns)