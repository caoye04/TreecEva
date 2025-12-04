def analyze_network_packets(packets):
    # Analyze network packets and return summary statistics
    packet_counts = {}
    total_size = 0
    security_flags = set()
    
    for packet in packets:
        protocol = packet.get('protocol', 'unknown')
        packet_counts[protocol] = packet_counts.get(protocol, 0) + 1
        
        if packet.get('encrypted', False):
            security_flags.add('encrypted')
            
        size = packet.get('size', 0)
        total_size += size
        
        # Track potential security issues (unused)
        if packet.get('malformed', False):
            security_flags.add('malformed')
    
    return {
        'counts': packet_counts,
        'total_size': total_size,
        'security_flags': security_flags
    }

def calculate_checksum(data):
    # Calculate a simple XOR checksum
    checksum = 0
    for value in data:
        checksum ^= value
    return checksum

def optimize_routing(network_map, start_node='A'):
    # Simulated routing optimization (not used in final calculation)
    visited = set([start_node])
    distances = {start_node: 0}
    
    nodes = list(network_map.keys())
    for _ in range(len(nodes)):
        current = min([n for n in nodes if n in distances and n not in visited], 
                     key=lambda x: distances[x], default=None)
        if not current:
            break
            
        visited.add(current)
        for neighbor, distance in network_map.get(current, {}).items():
            if neighbor not in distances or distances[current] + distance < distances[neighbor]:
                distances[neighbor] = distances[current] + distance
                
    return distances

def calculate_priority(network_data):
    # Extract relevant metrics from network data
    latency = network_data.get('latency', 100)
    bandwidth = network_data.get('bandwidth', 10)
    packet_loss = network_data.get('packet_loss', 0.05)
    
    # Process packet data
    packets = network_data.get('packets', [])
    packet_analysis = analyze_network_packets(packets)
    
    # Calculate priority components
    latency_factor = 100 / (latency + 10)  # Lower latency is better
    bandwidth_factor = bandwidth / 10      # Higher bandwidth is better
    
    # Process protocol weights (TCP has higher priority)
    protocol_counts = packet_analysis['counts']
    tcp_count = protocol_counts.get('tcp', 0)
    udp_count = protocol_counts.get('udp', 0)
    
    # Apply security modifiers
    security_level = len(packet_analysis['security_flags'])
    security_modifier = 1.0 + (security_level * 0.1)
    
    # These metrics aren't used in final calculation (distraction)
    reliability_score = (1 - packet_loss) * 100
    congestion_index = (packet_analysis['total_size'] / 1000) * (latency / 50)
    
    # Calculate checksum from important metrics (misleading)
    checksum_data = [int(latency), int(bandwidth * 10), int((1 - packet_loss) * 100)]  
    integrity_check = calculate_checksum(checksum_data)
    
    # Calculate base score
    base_score = (latency_factor * 2) + (bandwidth_factor * 3)
    
    # Apply protocol weighting
    if tcp_count > udp_count:
        protocol_bonus = tcp_count - udp_count
    else:
        protocol_bonus = 0
    
    # Calculate final priority score
    priority = (base_score + protocol_bonus) * security_modifier
    
    # Round to nearest integer
    return round(priority)

# Network configuration data
network_map = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 15, 'E': 20},
    'C': {'E': 35, 'F': 30},
    'D': {'G': 25},
    'E': {'G': 15, 'H': 20},
    'F': {'H': 10},
    'G': {'I': 5},
    'H': {'I': 10},
    'I': {}
}

# Simulated network data
network_data = {
    'latency': 40,
    'bandwidth': 25,
    'packet_loss': 0.02,
    'jitter': 5.2,  # Unused metric (distraction)
    'packets': [
        {'protocol': 'tcp', 'size': 1024, 'encrypted': True},
        {'protocol': 'tcp', 'size': 512, 'encrypted': True},
        {'protocol': 'tcp', 'size': 768, 'encrypted': False},
        {'protocol': 'udp', 'size': 256, 'encrypted': False},
        {'protocol': 'udp', 'size': 128, 'malformed': True}
    ],
    'routes': optimize_routing(network_map)  # Unused calculation (distraction)
}

# Calculate network priority score
priority_score = calculate_priority(network_data)
print(f"Network priority score: {priority_score}")

# Result: {priority_score}