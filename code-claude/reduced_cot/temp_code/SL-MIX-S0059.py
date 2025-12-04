def calculate_node_importance(node_id, connections):
    # Calculate importance score based on connections and node_id
    potential_score = len(connections) * 2
    actual_score = sum([(c % 10) for c in connections]) if connections else 0
    return (node_id * 3) % 10 + actual_score

def optimize_routing(paths, traffic_levels):
    # Optimize network routing based on traffic levels
    optimized = []
    for path, traffic in zip(paths, traffic_levels):
        if traffic > 75:
            optimized.append(path[::-1])  # Reverse high traffic paths
        elif traffic < 25:
            optimized.append(path[::2])   # Take every other node for low traffic
        else:
            optimized.append(path)        # Keep medium traffic paths as is
    return optimized

def analyze_packet_loss(transmission_data):
    # Calculate packet loss percentage
    sent = sum(t['sent'] for t in transmission_data)
    received = sum(t['received'] for t in transmission_data)
    return 100 - (received * 100 / sent) if sent > 0 else 0

def calculate_network_strength(active_nodes, connection_map):
    # Calculate overall network strength based on active nodes and their connections
    if not active_nodes:
        return 0
    
    # Filter relevant connections and compute base metrics
    relevant_connections = {node: connection_map.get(node, []) for node in active_nodes}
    
    # Calculate node importance scores
    importance_scores = {}
    for node, connections in relevant_connections.items():
        # Only consider connections to other active nodes
        active_connections = [c for c in connections if c in active_nodes]
        importance_scores[node] = calculate_node_importance(node, active_connections)
    
    # Network stability factor - misleading calculation
    stability_factor = sum(node % 5 for node in active_nodes) / len(active_nodes)
    
    # Distractor - calculate theoretical max bandwidth
    max_bandwidth = sum(len(connections) * 10 for connections in relevant_connections.values())
    
    # Distractor - simulate packet routing
    routing_paths = [[node] + relevant_connections[node][:2] for node in active_nodes if relevant_connections[node]]
    traffic_levels = [len(path) * 15 for path in routing_paths]
    optimized_paths = optimize_routing(routing_paths, traffic_levels)
    
    # Distractor - analyze simulated transmission data
    transmission_data = [{"sent": 100, "received": 95 - i % 10} for i, _ in enumerate(active_nodes)]
    packet_loss = analyze_packet_loss(transmission_data)
    
    # Calculate actual network strength - this is the core calculation
    connection_density = sum(len(connections) for connections in relevant_connections.values()) / len(active_nodes)
    importance_factor = sum(importance_scores.values()) / len(importance_scores) if importance_scores else 0
    
    # The actual formula for network strength
    network_strength = int((connection_density * 5) + (importance_factor * 3))
    
    # Distractor - advanced metrics that aren't used
    resilience_score = sum([node & 0xF for node in active_nodes]) / len(active_nodes)
    efficiency_index = max_bandwidth / (len(active_nodes) * 10)
    
    # More distractor calculations that seem important but aren't used
    if packet_loss > 5:
        adjusted_strength = network_strength * (100 - packet_loss) / 100
    else:
        adjusted_strength = network_strength * 1.05
    
    # The result is actually just the original network_strength
    return network_strength

# Network configuration
active_nodes = [3, 7, 12, 15, 22, 28]

# Connection map (node_id: [connected_node_ids])
connection_map = {
    3: [7, 12, 28],
    7: [3, 15, 22],
    12: [3, 28],
    15: [7, 22],
    22: [7, 15, 28],
    28: [3, 12, 22],
    # Distractor nodes not in active list
    5: [8, 14],
    8: [5, 14, 19],
    14: [5, 8, 19],
    19: [8, 14]
}

# Calculate secondary metrics - distractors
node_coverage = len(active_nodes) / len(connection_map)
connectivity_ratio = sum(len(v) for v in connection_map.values()) / len(connection_map)

# Calculate potential throughput - another distractor
potential_throughput = sum([len(connection_map.get(node, [])) * 2.5 for node in active_nodes])

# This is our target calculation
network_strength = calculate_network_strength(active_nodes, connection_map)

# Distractor calculations after the target value is computed
scaled_strength = network_strength * (1 + node_coverage)
weighted_strength = network_strength * connectivity_ratio
adjusted_strength = network_strength + (potential_throughput / 100)

print(f"Network metrics:")
print(f"Coverage: {node_coverage:.2f}")
print(f"Connectivity: {connectivity_ratio:.2f}")
print(f"Throughput: {potential_throughput:.1f}")
print(f"Result: {network_strength}")