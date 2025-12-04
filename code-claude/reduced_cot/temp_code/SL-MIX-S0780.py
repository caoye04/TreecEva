def calculate_latency(packets, overhead=0.05):
    # Simulate network latency based on packet size and overhead
    latency_base = sum(p['size'] for p in packets) * overhead
    return latency_base + sum(p.get('priority', 0) for p in packets)

def optimize_route(nodes, start_idx=0):
    # Attempt to optimize network path (not used in main calculation)
    if not nodes:
        return []
    
    path = [start_idx]
    visited = {start_idx}
    
    for _ in range(len(nodes) - 1):
        current = path[-1]
        next_node = (current + 1) % len(nodes)
        while next_node in visited:
            next_node = (next_node + 1) % len(nodes)
        path.append(next_node)
        visited.add(next_node)
    
    return path

def calculate_efficiency(traffic_data):
    # Network efficiency calculation based on traffic patterns
    packet_count = len(traffic_data)
    dropped_packets = sum(1 for p in traffic_data if p.get('dropped', False))
    
    # Calculate bandwidth utilization
    total_bandwidth = 0
    used_bandwidth = 0
    
    for packet in traffic_data:
        # Extract packet data with defaults
        size = packet.get('size', 0)
        priority = packet.get('priority', 1)
        encrypted = packet.get('encrypted', False)
        
        # Track bandwidth metrics
        packet_bandwidth = size * (2 if encrypted else 1)  # Encrypted packets use double bandwidth
        total_bandwidth += packet_bandwidth
        
        if not packet.get('dropped', False):
            used_bandwidth += size  # Only count successfully transmitted packets
    
    # Calculate theoretical max throughput (misleading calculation)
    theoretical_max = total_bandwidth * 1.5
    
    # Calculate QoS factor (Quality of Service)
    qos_factor = 0
    for idx, packet in enumerate(traffic_data):
        if idx % 3 == 0:  # Every third packet affects QoS differently (distraction)
            qos_factor += packet.get('priority', 0) * 0.1
        elif idx % 2 == 0:  # Even packets
            qos_factor += 0.05
    
    # Path optimization simulation (not relevant to final calculation)
    nodes = [i for i in range(min(5, packet_count))]
    optimal_path = optimize_route(nodes)
    path_length = len(optimal_path)
    
    # Calculate delivery ratio (successful packets / total packets)
    delivery_ratio = (packet_count - dropped_packets) / packet_count if packet_count > 0 else 0
    
    # Protocol overhead calculation (distraction)
    protocol_overhead = sum(p.get('header_size', 2) for p in traffic_data) / max(1, total_bandwidth)
    
    # Network efficiency score (main calculation)
    if delivery_ratio > 0:
        network_efficiency = round(delivery_ratio * 100 - (dropped_packets * 2), 2)
    else:
        network_efficiency = 0
    
    return network_efficiency

# Network traffic simulation data
traffic_data = [
    {'size': 64, 'priority': 1, 'dropped': False, 'encrypted': True, 'header_size': 8},
    {'size': 128, 'priority': 2, 'dropped': False, 'encrypted': False, 'header_size': 12},
    {'size': 256, 'priority': 1, 'dropped': True, 'encrypted': False, 'header_size': 8},
    {'size': 512, 'priority': 3, 'dropped': False, 'encrypted': True, 'header_size': 16},
    {'size': 128, 'priority': 2, 'dropped': False, 'encrypted': False, 'header_size': 12}
]

# Calculate alternative metrics (distraction)
alternative_metric = calculate_latency(traffic_data)

# Main efficiency calculation
network_efficiency = calculate_efficiency(traffic_data)

# Calculate congestion index (distraction)
congestion_index = sum(p['size'] for p in traffic_data if not p.get('dropped', False)) / 1024

print(f"Network congestion: {congestion_index:.2f}")
print(f"Alternative metric: {alternative_metric:.2f}")
print(f"Result: {network_efficiency}")