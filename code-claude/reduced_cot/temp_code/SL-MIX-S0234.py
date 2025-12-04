def calculate_network_load(connections, traffic_pattern):
    # Calculate simulated network load based on connection patterns
    load_factor = sum(connections.values()) * 0.15
    for pattern in traffic_pattern:
        if pattern > 75:
            load_factor += pattern * 0.25
        else:
            load_factor += pattern * 0.1
    return load_factor

def optimize_route(route_map, start_point):
    # Optimize routing based on historical data
    if start_point not in route_map:
        return 0
    
    efficiency = route_map[start_point] * 2
    hop_count = len(route_map) - 2
    
    # This optimization is not actually used in final calculation
    if hop_count > 5:
        return efficiency * 0.8
    else:
        return efficiency * 1.2

def calculate_final_priority(network_data, active_nodes):
    # Determine communication priority based on node activity
    node_weights = {}
    total_weight = 0
    
    # Process each active node and assign weights
    for node in active_nodes:
        # Skip inactive nodes (but all nodes in active_nodes are actually active)
        if node.startswith('backup'):
            node_weights[node] = 5
        elif node.startswith('primary'):
            node_weights[node] = 20
            # This branch is never taken due to the data
            if node == 'primary_main':
                node_weights[node] = 50
        else:
            node_weights[node] = 10
        
        total_weight += node_weights[node]
    
    # Calculate priority score using node weights and network data
    priority_score = 0
    for node in active_nodes:
        if node in network_data:
            # Process the node data
            node_data = network_data[node]
            latency = node_data.get('latency', 100)
            bandwidth = node_data.get('bandwidth', 10)
            reliability = node_data.get('reliability', 0.5)
            
            # This complex formula has misleading components but determines the actual score
            node_score = (bandwidth / max(1, latency/10)) * reliability
            priority_score += node_score * (node_weights[node] / total_weight)
    
    # Additional calculations that don't affect the final result
    unused_metric = sum(node_weights.values()) * 0.25
    if unused_metric > 100:
        priority_score += 5
    
    # Apply network-wide adjustment factor
    network_factor = 1.0
    for node, data in network_data.items():
        if node in active_nodes and data.get('critical', False):
            network_factor = 1.25
            break
    
    return round(priority_score * network_factor, 2)

# Network simulation data
network_data = {
    'node1': {'latency': 25, 'bandwidth': 100, 'reliability': 0.95},
    'node2': {'latency': 15, 'bandwidth': 80, 'reliability': 0.99, 'critical': True},
    'primary_a': {'latency': 30, 'bandwidth': 120, 'reliability': 0.9},
    'backup_b': {'latency': 50, 'bandwidth': 40, 'reliability': 0.85},
    'node5': {'latency': 35, 'bandwidth': 70, 'reliability': 0.92}
}

# Define active nodes in the network
active_nodes = ['node1', 'node2', 'primary_a', 'backup_b']

# Calculate various network metrics (most not used in final result)
connections = {'A-B': 5, 'B-C': 3, 'A-C': 2, 'C-D': 7}
traffic_pattern = [45, 80, 60, 30]

# Calculate network load (unused in final result)
network_load = calculate_network_load(connections, traffic_pattern)

# Calculate route efficiency (unused in final result)
route_map = {'node1': 0.75, 'node2': 0.85, 'primary_a': 0.65}
route_efficiency = optimize_route(route_map, 'node2')

# This is the key calculation
priority_value = calculate_final_priority(network_data, active_nodes)
print(f"Result: {priority_value}")