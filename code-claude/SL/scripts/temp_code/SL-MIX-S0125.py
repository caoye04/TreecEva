def process_packet(packet_data, priority_level=0):
    # Process network packet and extract useful metrics
    packet_size = sum([ord(c) % 7 for c in packet_data[:5]])
    error_bits = bin(hash(packet_data) & 0xFFFF).count('1')
    
    # Apply priority weighting (unused in main calculation)
    weighted_priority = packet_size * (priority_level + 1)
    
    # Calculate packet efficiency score
    if error_bits > 10:
        return packet_size / (error_bits * 0.8)
    else:
        return packet_size / max(1, error_bits * 0.4)

def calculate_routing_overhead(nodes, connections):
    # This function calculates theoretical network overhead
    # but is not used in the final calculation
    base_overhead = len(nodes) * 3.5
    connection_factor = len(connections) * 0.75
    
    redundancy_paths = 0
    for node in nodes:
        if node in connections:
            redundancy_paths += len(connections[node])
    
    return base_overhead + connection_factor + (redundancy_paths * 0.25)

def analyze_traffic_patterns(data_points):
    # Analyze distribution but not used in main calculation
    if not data_points:
        return 0
        
    patterns = {}
    for point in data_points:
        key = point % 5
        if key in patterns:
            patterns[key] += 1
        else:
            patterns[key] = 1
    
    return max(patterns.values()) / len(data_points)

def calculate_network_efficiency(data_streams):
    # Main function to calculate network efficiency
    transmission_data = {}
    routing_nodes = set()
    
    # Extract and organize data
    for stream_id, packets in data_streams.items():
        transmission_data[stream_id] = []
        for packet in packets:
            # Only consider packets with even length (distraction rule)
            if len(packet) % 2 == 0:
                transmission_data[stream_id].append(packet)
            routing_nodes.add(packet[:2])
    
    # Calculate baseline metrics (some are distractions)
    baseline_load = sum(len(packets) for packets in data_streams.values())
    theoretical_capacity = len(routing_nodes) * 25
    unused_capacity = theoretical_capacity - baseline_load
    
    # Process each stream
    efficiency_scores = []
    latency_factors = []
    
    for stream_id, packets in transmission_data.items():
        # Skip processing for streams with IDs divisible by 7 (distraction)
        if int(stream_id) % 7 == 0:
            continue
            
        # Calculate stream efficiency
        if not packets:
            continue
            
        # Process packets and calculate efficiency metrics
        packet_scores = []
        for i, packet in enumerate(packets):
            # Only process packets at even indices
            if i % 2 == 0:
                score = process_packet(packet, i % 3)
                packet_scores.append(score)
        
        # Skip empty streams
        if not packet_scores:
            continue
            
        # Calculate stream efficiency and latency
        stream_efficiency = sum(packet_scores) / len(packet_scores)
        efficiency_scores.append(stream_efficiency)
        
        # Calculate fake latency factor (distraction)
        stream_latency = len(packets) * 0.05 * int(stream_id[0])
        latency_factors.append(stream_latency)
    
    # Calculate unused connection mappings (distraction)
    connection_map = {}
    for node in routing_nodes:
        connection_map[node] = [n for n in routing_nodes if n != node]
    
    # Calculate routing overhead (distraction)
    routing_overhead = calculate_routing_overhead(routing_nodes, connection_map)
    
    # Calculate traffic patterns (distraction)
    traffic_distribution = analyze_traffic_patterns([len(p) for stream in data_streams.values() for p in stream])
    
    # Final network efficiency calculation
    if not efficiency_scores:
        return 0
        
    # The key calculation is just the average of efficiency scores
    network_efficiency = sum(efficiency_scores) / len(efficiency_scores)
    
    # These adjustments are all distractions and not used
    adjusted_efficiency = network_efficiency * (1 - traffic_distribution/10)
    overhead_factor = 1 - (routing_overhead / (theoretical_capacity * 2))
    latency_impact = sum(latency_factors) / len(latency_factors) if latency_factors else 0
    
    return round(network_efficiency, 3)

# Define test data
data_streams = {
    "103": ["AB123", "CD456", "EF789", "GH012"],
    "245": ["JK345", "LM678", "NO901", "PQ234"],
    "307": ["RS567", "TU890", "VW123"],
    "421": ["XY456", "ZA789", "BC012", "DE345", "FG678"],
    "539": ["HI901", "JK234", "LM567"],
    "614": ["NO890", "PQ123", "RS456", "TU789"],
    "728": ["VW012", "XY345", "ZA678", "BC901"]
}

# Calculate and display network efficiency
network_efficiency = calculate_network_efficiency(data_streams)
print(f"Result: {network_efficiency}")