def filter_connections(node_list, connection_map, priority_level=3):
    """Filter connections based on priority level (distractor function)"""
    filtered = {}
    for node, connections in connection_map.items():
        if node in node_list:
            filtered[node] = [c for c in connections if c[1] >= priority_level]
    return filtered

def optimize_routing(nodes, paths):
    """Optimize routing paths (distractor function)"""
    routing_table = {}
    for node in nodes:
        distances = []
        for path in paths:
            if node in path:
                distances.append(len(path))
        if distances:
            routing_table[node] = min(distances)
        else:
            routing_table[node] = float('inf')
    return routing_table

def calculate_network_efficiency(nodes, connections):
    """Calculate network efficiency score based on active nodes and their connections"""
    if not nodes or not connections:
        return 0
    
    # Count valid connections between active nodes
    valid_connections = 0
    potential_connections = 0
    
    for i, node1 in enumerate(nodes):
        for node2 in nodes[i+1:]:
            potential_connections += 1
            if node2 in connections.get(node1, []):
                valid_connections += 1
    
    # Calculate base efficiency (core calculation for the answer)
    if potential_connections == 0:
        return 0
    base_efficiency = (valid_connections / potential_connections) * 100
    
    # Apply network size factor (relevant)
    size_factor = min(1.0, len(nodes) / 10)
    
    # Calculate redundancy bonus (distractor)
    redundancy_score = sum(len(conn) for conn in connections.values()) / max(1, len(connections))
    
    # Latency penalty calculation (distractor)
    latency_values = []
    for node, conn_list in connections.items():
        if node in nodes and conn_list:
            latency_values.append(len(conn_list) * 2.5)
    latency_penalty = sum(latency_values) / max(1, len(latency_values)) if latency_values else 0
    
    # Calculate stability modifier (distractor)
    stability_factor = 1.0
    if len(nodes) > 5:
        stability_factor = 1.2
    elif len(nodes) < 3:
        stability_factor = 0.8
    
    # Final calculation with size factor (only base_efficiency and size_factor matter)
    network_efficiency = base_efficiency * size_factor
    
    return round(network_efficiency, 2)

# Network topology definition
all_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
all_connections = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E', 'G'],
    'D': ['B', 'F'],
    'E': ['A', 'C', 'G'],
    'F': ['D', 'G'],
    'G': ['C', 'E', 'F']
}

# Network analysis parameters (distractors)
packet_loss = {'A': 0.01, 'B': 0.02, 'C': 0.015, 'D': 0.03, 'E': 0.01, 'F': 0.025, 'G': 0.02}
bandwidth = {'A': 100, 'B': 150, 'C': 200, 'D': 100, 'E': 300, 'F': 100, 'G': 200}

# Active nodes determination
load_thresholds = [45, 60, 75, 90]
node_loads = [55, 30, 85, 40, 65, 75, 50]

# Process node status (relevant)
active_nodes = []
for i, (node, load) in enumerate(zip(all_nodes, node_loads)):
    if load < load_thresholds[2]:  # Using threshold index 2 (75)
        active_nodes.append(node)

# Filter connections to only include active nodes (relevant)
connections = {}
for node in active_nodes:
    if node in all_connections:
        # Only include connections to other active nodes
        connections[node] = [n for n in all_connections[node] if n in active_nodes]

# Distractor calculations
network_paths = [
    ['A', 'B', 'D', 'F'],
    ['A', 'C', 'G', 'F'],
    ['A', 'E', 'G'],
    ['B', 'C', 'E'],
    ['D', 'F', 'G', 'C']
]

routing = optimize_routing(active_nodes, network_paths)
avg_distance = sum(routing.values()) / len(routing) if routing else 0

# The key calculation
network_efficiency = calculate_network_efficiency(active_nodes, connections)
print(f"Result: {network_efficiency}")
